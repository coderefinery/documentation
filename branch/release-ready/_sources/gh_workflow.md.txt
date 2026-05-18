# Deploying Sphinx documentation to GitHub Pages

```{objectives}
- Create a basic workflow which you can take home and adapt for your project.
```

## [GitHub Pages](https://pages.github.com/)

- Serve websites from a GitHub repository.
- It is no problem to serve using your own URL `https://myproject.org` instead of `https://myuser.github.io/myproject`.


## [GitHub Actions](https://github.com/features/actions/)

- Automatically runs code when your repository changes.
- We will let it run `sphinx-build` and make the result available to GitHub Pages.


## Our goal: putting it all together

- Host source code with documentation sources on a public Git repository.
- Each time we `git push` to the repository, a GitHub action triggers to
  rebuild the documentation.
- The documentation is pushed to a separate branch called 'gh-pages'.

---

## Demonstration - Deploy Sphinx documentation to GitHub Pages

````{exercise} GH-Pages-1: Deploy Sphinx documentation to GitHub Pages
In this exercise we will create an example repository on GitHub and
deploy it to GitHub Pages.

**Step 1**: Go to the [documentation-example](https://github.com/coderefinery/documentation-example/generate) project template
on GitHub and create a copy to your namespace.
- Give it a name, for instance "documentation-example".
- You don't need to "Include all branches"
- Click on "Create a repository".

**Step 2**: Browse the new repository.
- It will look very familar to the previous episode.
- However, we have moved the documentation part under `doc/` (many projects do it this
  way). But it is still a Sphinx documentation project.
- The source code for your project could then go under `src/`.


**Step 3**: Add the GitHub Action to your new Git repository.
- Add a new file at `.github/workflows/documentation.yml` (either through terminal or web interface), containing:
```{code-block} yaml
:linenos:
:emphasize-lines: 16,19
name: documentation

on: [push, pull_request, workflow_dispatch]

permissions:
  contents: write

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - name: Install dependencies
        run: |
          pip install sphinx sphinx_rtd_theme myst_parser
      - name: Sphinx build
        run: |
          sphinx-build doc _build
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        if: ${{ github.event_name == 'push' && github.ref == 'refs/heads/main' }}
        with:
          publish_branch: gh-pages
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: _build/
          force_orphan: true
```
- You don't need to understand all of the above
  -- you should mainly pay attention the highlighted lines
  which are shell commands (we know this because they are part of a `run: |` section).
  The first uses `pip` to install the dependencies and the second runs `sphinx-build`
  to actually build the documentation (as we saw in the previous episode).
- After the file has been committed (and pushed),
  check the action at `https://github.com/USER/documentation-example/actions`
  (replace `USER` with your GitHub username).

**Step 4**: Enable GitHub Pages
- On GitHub go to "Settings" -> "Pages".
- Under "Build and deployment"
  - In the **Source** section: choose "Deploy from a branch" in the dropdown menu
  - In the **Branch** section: choose "gh-pages" and "/ (root)" in the dropdown menus
  and click the **Save** button.
- You should now be able to verify the pages deployment in the "Actions" list 
  ([this is how it looks like](https://github.com/coderefinery/documentation/actions)
  for this lesson material).

**Step 5**: Verify the result
- Your site should now be live on `https://USER.github.io/documentation-example/` (replace USER).

**Step 6 (optional)**: Verify refreshing the documentation
- Commit some changes to your documentation
- Verify that the documentation website refreshes after your changes (can take few seconds or a minute)
````

## Exercise - Sphinx documentation on GitHub Pages
````{exercise} GH-Pages-2: Putting it all together 

1. Follow the above instructions to create a new repository with a Sphinx documentation project;
2. Try adding one or more of the following to your Sphinx project:  
   1. API documentation (see [previous exercise](#api-exercise) on API references) which requires the `sphinx-autodoc2` package.
   2. a Jupyter notebook (see [previous exercise](#jupyter-exercise) on Jupyter notebooks) which requires the `myst-nb` package.
   3. change the theme (see the end of [the quickstart](#quickstart)). You can browse themes and find their package names on the [Sphinx themes gallery](https://sphinx-themes.org/#themes).

   ```{important}
      The computer on which the GitHub actions run is *not* your local machine,
      and might not have the libraries you need to build the project.
      Make sure you update the dependencies (installed with `pip` in the demonstration) appropriately.      
   ```
   ```{important}
      Make sure the correct file paths are used. This will require adjusting paths from the example from the previous episode to the new layout. Note many paths, including e.g. the `autodoc2_packages` preference are now relative to the `doc/` directory.
   ```
What do you need to change in the workflow file?

```{solution} Solution
1. **API documentation**
   1. Change line 16 of `.github/workflows/documentation.yml` from `pip install sphinx sphinx_rtd_theme myst_parser` to `pip install sphinx sphinx_rtd_theme myst_parser sphinx-autodoc2`.
   2. Follow the instructions in [Sphinx-3](#api-exercise) changing paths so that:
      1. `multiply.py` is `src/multiply.py` and is specified as `../src/multiply.py` in the `autodoc2_packages` preference in `conf.py`
      2. `conf.py` is `doc/conf.py`
      3. `index.md` is `doc/index.md`.
   3. Commit and push your changes, verify the action has run successfully, and view the built site in your browser.
2. **a Jupyter notebook**
   1. Change line 16 of `.github/workflows/documentation.yml` from `pip install sphinx sphinx_rtd_theme myst_parser` to `pip install sphinx sphinx_rtd_theme myst_parser myst-nb`.
   2. Follow the instructions in [Sphinx-4](#jupyter-exercise) changing paths so that:
      1. `flower.md` is `docs/flower.md`
      2. `conf.py` is `doc/conf.py`
      3. `index.md` is `doc/index.md`.
   3. Commit and push your changes, verify the action has run successfully, and view the built site in your browser.
3. **change the theme**
   1. Change line 16 of `.github/workflows/documentation.yml` and add the theme package if necessary.
   2. In `docs/config.py` change `html_theme = 'sphinx_rtd_theme'` to the name of your chosen theme.
   3. Commit and push your changes, verify the action has run successfully, and view the built site in your browser.
```
````

## Alternatives to GitHub Pages

- [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/)
  and [GitLab CI](https://docs.gitlab.com/ee/ci/) can create a very similar workflow.

- [Read the Docs](https://readthedocs.org) is the most common alternative to
  hosting in GitHub Pages.

- Sphinx builds HTML files (this is what static site generators do), and you
  can host them anywhere, for example your university's web space or own web server.


## Migrating your own documentation to Sphinx

- First convert your documentation to Markdown using [Pandoc](https://pandoc.org).
- Create a file `index.rst` which lists all other Markdown files and provides the
  table of contents.
- Add a `conf.py` file. You can generate a starting point for `conf.py` and
  `index.rst` with `sphinx-quickstart`, or you can take the examples in this
  lesson as inspiration.
- Test building the documentation locally with `sphinx-build`.
- Once this works, follow the above steps to build and deploy to GitHub Pages or some other web space.

---

```{keypoints}
- Sphinx makes simple HTML (and more) files, so it is easy to find a place to host them.
- Github Pages + Github Actions provides a convenient way to make
  sites and host them on the web.
```
