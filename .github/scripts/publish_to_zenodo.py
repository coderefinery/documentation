# Based on examples on https://developers.zenodo.org/

import json
import os
import requests
import yaml

ACCESS_TOKEN = os.environ["ZENODO_TOKEN"]
CONCEPT_ID = os.environ["ZENODO_CONCEPT_ID"]

print(CONCEPT_ID)
print(ACCESS_TOKEN)

BASE_URL = "https://zenodo.org/api"


json_headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

upload_headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

def load_citation():
    with open("CITATION.cff", encoding="utf-8") as f:
        return yaml.safe_load(f)


def cff_to_creators(authors):
    creators = []

    for author in authors:
        if "family-names" in author:
            creators.append(
                {
                    "name": (
                        f"{author['family-names']}, "
                        f"{author['given-names']}"
                    )
                }
            )
        else:
            creators.append({"name": author["name"]})

    return creators



# Load metadata from CITATION.cff

cff = load_citation()

metadata = {
    "title": cff["title"],
    "upload_type": "dataset",
    "description": cff.get("abstract", ""),
    "creators": cff_to_creators(cff["authors"]),
    "keywords": cff.get("keywords", []),
    "version": str(cff.get("version")) if cff.get("version") is not None else None,
    "license": cff.get("license")
}


# Discard any unpublished draft left over from a previous failed run.
# Zenodo only allows one unpublished new-version draft per concept at
# a time, so a stray one would make the newversion call below fail.

r = requests.get(
    f"{BASE_URL}/deposit/depositions",
    params={"q": f"conceptrecid:{CONCEPT_ID}", "all_versions": "true"},
    headers=json_headers,
)

r.raise_for_status()

for dep in r.json():
    if not dep.get("submitted"):
        print(f"Discarding leftover draft {dep['id']}")
        requests.delete(dep["links"]["self"], headers=json_headers).raise_for_status()


# Find the current latest version of this concept.
# newversion only works when called on the latest version's own
# deposit ID, and that ID changes with every new release.

r = requests.get(
    f"{BASE_URL}/records",
    params={"q": f"conceptrecid:{CONCEPT_ID}", "all_versions": "true"},
    headers=json_headers,
)

r.raise_for_status()

hits = r.json()["hits"]["hits"]

latest_id = hits[0]["id"]
for hit in hits[1:]:
    if hit["id"] > latest_id:
        latest_id = hit["id"]

print(f"Latest existing version: {latest_id}")


# Create new version of existing concept DOI

r = requests.post(
    f"{BASE_URL}/deposit/depositions/{latest_id}/actions/newversion",
    headers=json_headers)

r.raise_for_status()

latest_draft = r.json()["links"]["latest_draft"]


# Get draft deposition information

r = requests.get(
    latest_draft,
    headers=json_headers,
)

r.raise_for_status()

deposition = r.json()

deposition_id = deposition["id"]
bucket_url = deposition["links"]["bucket"]

print(f"Draft deposition: {deposition_id}")


# Upload release archive


tag = os.environ["GITHUB_REF_NAME"]
repo_name = os.environ['GITHUB_REPOSITORY']


archive_url = (
    f"https://github.com/"
    f"{repo_name}"
    f"/archive/refs/tags/{tag}.zip"
)

archive_name = f"{tag}.zip"

download = requests.get(archive_url)
download.raise_for_status()

with open(archive_name, "wb") as fp:
    fp.write(download.content)

with open(archive_name, "rb") as fp:
    r = requests.put(
        f"{bucket_url}/{archive_name}",
        data=fp,
        headers=upload_headers
    )

r.raise_for_status()

print(f"Uploaded {archive_name}")


# Update metadata

data = {
    "metadata": metadata
}

r = requests.put(
    f"{BASE_URL}/deposit/depositions/{deposition_id}",
    data=json.dumps(data),
    headers=json_headers
)

r.raise_for_status()

print("Metadata updated")


# Publish


r = requests.post(
    f"{BASE_URL}/deposit/depositions/{deposition_id}/actions/publish",
    headers=json_headers,
)

r.raise_for_status()

record = r.json()

print(f"Published DOI: {record.get('doi')}")
print(f"Record URL: {record['links']['html']}")
