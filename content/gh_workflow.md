# Deploying Sphinx documentation to GitHub Pages

```{objectives}
- Create a basic workflow which you can take home and adapt for your project.
```

## [GitHub Pages](https://pages.github.com/)

- Serve websites from a GitHub repository
- It is no problem to serve using your own URL `http://myproject.org` instead of `http://myuser.github.io/myproject`


## [GitHub Actions](https://github.com/features/actions/)

- Automatically runs code when your repository changes
- We will run Sphinx build and make the result available to GitHub Pages
- Equations and images no problem
- Can use Sphinx styles

## Typical workflow

- Host source code with documentation sources on a public Git repository.
- Each time you `git push` to the repository, a GitHub action triggers to
  rebuild the documentation.
- The documentation is pushed to a separate branch called 'gh-pages'.

---

## Exercise - Deploy Sphinx documentation to GitHub Pages

``````{exercise} gh-pages-1: Deploy Sphinx documentation to GitHub Pages
In this exercise we will create an example repository on GitHub and
deploy it to GitHub Pages. The example project contains a script for
counting the frequency distribution of words in a given file and some
documentation generated using Sphinx. For bigger projects, we can have
more source files.

**Step 1:** Go to the [word-count project template](https://github.com/coderefinery/word-count/generate)
on GitHub and create a copy to your namespace ("Generate", since this
is a template repository).

**Clone the repository**

The repository contains following two folders, among few other files and folders:
- **source** folder contains the source code
- **doc** folder contains the Sphinx documentation

The doc folder contains the Sphinx configuration file (`conf.py`) and the index file (`index.rst`) and some contents (Markdown files).
The `conf.py` file has been adjusted to be able to autogenerate documentation from sources.


**Build HTML pages locally**

Inside the cloned repository, build the documentation and verify the result in your browser:

```console
$ sphinx-build doc _build
```

**Test HTML pages links**

Inside the cloned repository, check the integrity of all internal and external links:

```console
$ sphinx-build doc -W -b linkcheck -d _build/doctrees _build/html
```

**Step 2:** Add the GitHub Action

- Create a new file at `.github/workflows/documentation.yaml` with the contents

```yaml
name: Docs
on: [push, pull_request, workflow_dispatch]
jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - name: Install dependencies
        run: |
          pip install sphinx sphinx_rtd_theme
      - name: Sphinx build
        run: |
          sphinx-build doc _build
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        if: ${{ github.event_name == 'push' && github.ref == 'refs/heads/master' }}
        with:
          publish_branch: gh-pages
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: _build/
          force_orphan: true
```

You don't need to understand all of the above, but you
might spot familiar commands in the `run:` sections.

- Add, commit and push to GitHub
- Check the action at `https://github.com/<myuser>/word-count/actions`.
Replace `<myuser>` with your GitHub username.

**Step 2:** Enable GitHub Pages

- Go to `https://github.com/<myuser>/word-count/settings/pages`
- In the "Source" section, choose "gh-pages" in the dropdown menu and click
  save
- (You should be able to verify the pages deployment in the Actions list)


**Verify the result**

That's it! Your site should now be live on
`https://<myuser>.github.io/word-count/` (replace username).

**Verify refreshing the documentation**

Finally, make some changes to your documentation
- Add documentation related to other functions
- Prerequisites and how to use the program
- Rules for contribution
- Some example results (figures, tables, ...)
- Commit and push them, and verify that the documentation website refreshes after your changes (can take few seconds or a minute)
``````

```{callout} Do not add the generated build directory to your repository
The `_build` directory is generated locally with the command `sphinx-build
doc _build` and allows you to check the content locally but it should not be
part of the Git repository.  We recommend to add `_build` to `.gitignore` to
prevent you from accidentally adding files below `_build` to the Git
repository.
```


## Alternatives to GitHub Pages

[GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/) and [GitLab CI](https://docs.gitlab.com/ee/ci/) can create a very similar workflow.

[Read the Docs](https://readthedocs.org) is the most common alternative to
hosting in GitHub Pages.

Sphinx simply builds HTML files, and you can host them anywhere, for
example your university's web space or own web server.  This is the
whole point of **static site generators**.


## Migrating your own documentation to Sphinx

- First convert your documentation to markdown using [Pandoc](https://pandoc.org)
- Create a file `index.rst` which lists all other RST files and provides the
  table of contents.
- Add a `conf.py` file. You can generate a starting point for `conf.py` and
  `index.rst` with `sphinx-quickstart`, or you can take the examples in this
  lesson as inspiration.
- Test building the documentation locally with `sphinx-build`.
- Once this works, follow the above steps to build and deploy to GitHub Pages.



---

```{keypoints}
- Sphinx makes simple HTML (and more) files, so it is easy to find a place to host them.
- Github Pages + Github Actions provides a convenient way to make
  sites and host them on the web.
```
