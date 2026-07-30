"""Fill bioschemas.yml with metadata sourced from CITATION.cff."""

import json
from datetime import date, datetime

import yaml

CITATION_FILE = "CITATION.cff"
BIOSCHEMAS_FILE = "bioschemas.yml"

SPDX_LICENSE_URLS = {
    "CC-BY-4.0": "https://creativecommons.org/licenses/by/4.0/"
}


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def cff_to_authors(authors):
    result = []
    for author in authors:
        if "family-names" in author:
            result.append(
                {
                    "@type": "Person",
                    "name": f"{author['given-names']} {author['family-names']}",
                }
            )
        else:
            result.append({"@type": "Organization", "name": author["name"]})
    return result


def license_url(spdx_id):
    return SPDX_LICENSE_URLS.get(spdx_id, spdx_id)


def stringify(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return value


def main():
    cff = load_yaml(CITATION_FILE)
    bioschemas = load_yaml(BIOSCHEMAS_FILE)

    bioschemas["name"] = cff["title"]
    bioschemas["description"] = cff.get("abstract", "")
    bioschemas["author"] = cff_to_authors(cff["authors"])
    bioschemas["version"] = stringify(cff.get("version", ""))
    bioschemas["url"] = cff.get("url", "")
    bioschemas["license"] = license_url(cff.get("license", ""))
    if cff.get("doi"):
        bioschemas["identifier"] = f"https://doi.org/{cff['doi']}"

    with open(BIOSCHEMAS_FILE, "w", encoding="utf-8") as f:
        json.dump(bioschemas, f, indent=4)
        f.write("\n")


if __name__ == "__main__":
    main()
