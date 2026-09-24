# Deploying Sphinx documentation 

```{objectives}
- Create a basic workflow which you can take home and adapt for your project.
```

## [GitHub Pages](https://pages.github.com/) and [GitLab Pages](https://docs.gitlab.com/user/project/pages/)

- Serve websites from a Git repository.
- It is no problem to serve using your own URL `https://myproject.org` instead of `https://myuser.github.io/myproject`.



## [GitHub Actions](https://github.com/features/actions/) and [GitLab CI/CD](https://docs.gitlab.com/topics/build_your_application/)

- Automatically runs code when your repository changes.
- We will let it run `sphinx-build` and make the result available to GitHub Pages.


## Our goal: putting it all together

- Host source code with documentation sources on a public Git repository.
- Each time we `git push` to the repository, 
  a GitHub workflow or a Gitlab pipeline 
  triggers to
  rebuild the documentation.

---

## Demonstration - Deploy Sphinx documentation to GitHub/GitLab Pages

::::::{exercise} GH-Pages-1: Deploy Sphinx documentation to GitHub Pages
In this exercise we will create an example repository on a software forge
(GitHub or GitLab) 
and deploy it to the corresponding "Page" service
(GitHub Pages or GitLab Pages).

**Preliminary: Verify the "Pages" feature is available on  your forge**

:::::{tabs}
::::{group-tab} GitHub
On `github.com`, the feature is typically available.
::::
::::{group-tab} GitLab
On GitLab servers, it depends on the configuration. 
- On `gitlab.com`, the feature is typically available.
- On other instances, you have to check.
  You can verify that in a project you have on that GitLab instance.
  Go to the page of a project, on **Settings** -> **General** -> **Visibility, project features, permissions** and check if the  **Pages** can be activated. 
  If not, then your GitLab instance might not allow you to host pages,
  and you will need another instance or service to host your static website.
::::
:::::

**Step 1**: 

Generate the repository to be used as the starting point. 
Repositories can be generated from templates,
created from imports, or created as empty and filled with a push
from you own machine.


:::::{tabs}
:::{group-tab} GitHub
On GitHub the most convenient way is to generate the repository from a template.

Go to the [documentation-example](https://github.com/coderefinery/documentation-example/generate) project template
on GitHub and create a copy to your namespace.
- Give it a name, for instance "documentation-example".
- You don't need to "Include all branches"
- Click on "Create a repository".
:::
:::{group-tab} GitLab
Oh GitLab, althoug a "template" feature is present, 
its use is more constrained, so we will instead *import*
the template repository from GitHub.

- Go to your account on the GitLab instance you plan to use,
click on the `+` icon at the top of the page on the right,
and click on "New Project/Repository".
- Click on the "Import Project" tile, then on "Repository by URL"
- In the "Git repository URL" field, paste `https://github.com/coderefinery/documentation-example`,
  and click the "Check connection" button, which is immediately on the right.
- You also need to choose:
  - a project name, for instance "documentation-example"
  - an appropriate group or namespace. Your personal namespace is fine.
  - a visibility level: choose "public", 
    otherwise the pipelines you create 
    will not be able to run on "public" infrastructure.

After that, click on "Create Project". 
You will see that GitLab is basically cloning the GitHub project.

:::
:::::


**Step 2**: Browse the new repository.
- It will look very familar to the previous episode.
- However, we have moved the documentation part under `doc/` (many projects do it this
  way). But it is still a Sphinx documentation project.
- The source code for your project could then go under `src/`.


**Step 3**: Automate the generation of the documentation.
:::::{tabs}
::::{group-tab} GitHub
- Add a new file at `.github/workflows/documentation.yml` (either through terminal or web interface), containing:
:::{code-block} yaml
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
          pip install -r requirements.txt
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
:::
- You don't need to understand all of the above
  -- you should mainly pay attention the highlighted lines
  which are shell commands (we know this because they are part of a `run: |` section).
  The first uses `pip` to install the dependencies and the second runs `sphinx-build`
  to actually build the documentation (as we saw in the previous episode).
- After the file has been committed (and pushed),
  check the action at `https://github.com/USER/documentation-example/actions`
  (replace `USER` with your GitHub username).
::::
::::{group-tab} GitLab

On GitLab, automation is typically managed by the `.gitlab-ci.yml` file 
at the top directory of your repository. 

Create that file (if not existing), and add the definition of a new job in it:
:::{code-block} yaml
:linenos:
:emphasize-lines: 4,5
create-pages:
  image: python:latest
  script:
    - pip install -r requirements.txt 
    - sphinx-build doc public 
  pages: true
:::
::::
:::::


**Step 4**: Enable Pages feature and verify it's running

:::::{tabs}
::::{group-tab} GitHub
Note that once the documentation created 
it is pushed to a separate branch called 'gh-pages'
(this is what the action `peaceiris/actions-gh-pages` does).

- Go to "Settings" -> "Pages".
- Under "Build and deployment"
  - In the **Source** section: choose "Deploy from a branch" in the dropdown menu
  - In the **Branch** section: choose "gh-pages" and "/ (root)" in the dropdown menus
  and click the **Save** button.
- You should now be able to verify the pages deployment in the "Actions" list 
  ([this is how it looks like](https://github.com/coderefinery/documentation/actions)
  for this lesson material).
- You can verify that the repository has now a branch named `gh-pages`
  which contains the generated documentation
  (and only that).
::::
::::{group-tab} GitLab
 With the default settings, on a GitLab server with the Pages feature enabled 
everything should work. To check:

- Go to Build -> Pipelines. 
  There should be a running (or complete) pipeline at the top of the list,
  with two stages.

  - if you see only one stage, the "Pages" feature might not be active for your repository or for the whole instance 
  - if you see no pipelines, then the CI/CD feature might be disabled, or you might have misnamed the `.gitlab-ci.yml` file.

  (the project features can be checked in **Settings**->**General**->***Visibility, project features, permissions**)

::::
:::::




**Step 5**: Verify the result
:::::{tabs}
::::{group-tab} GitHub
Your site should now be live at 
`https://USER.github.io/documentation-example/` (replace USER).

::::
::::{group-tab} GitLab
Your site should be live. 
To find out the exact URL, 
go to the main page of your project
and on the right 
(under the "Project Information" header)
click on the "GitLab Pages" link).
::::
:::::

**Step 6 (optional)**: Verify refreshing the documentation
- Commit some changes to your documentation
- Verify that the documentation website refreshes after your changes (can take few seconds or a minute)
::::::

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
   1. Edit the `requirements.txt` file in the repository, adding the  `sphinx-autodoc2` package.
   2. Follow the instructions in [Sphinx-3](#api-exercise) changing paths so that:
      1. `multiply.py` is `src/multiply.py` and is specified as `../src/multiply.py` in the `autodoc2_packages` preference in `conf.py`
      2. `conf.py` is `doc/conf.py`
      3. `index.md` is `doc/index.md`.
   3. Commit and push your changes, verify the action has run successfully, and view the built site in your browser.
2. **a Jupyter notebook**
   1. Edit the `requirements.txt` file in the repository, adding the `myst-nb` package.
   2. Follow the instructions in [Sphinx-4](#jupyter-exercise) changing paths so that:
      1. `flower.md` is `doc/flower.md`
      2. `conf.py` is `doc/conf.py`
      3. `index.md` is `doc/index.md`.
   3. Commit and push your changes, verify the action has run successfully, and view the built site in your browser.
3. **change the theme**
   1. Change line 16 of `.github/workflows/documentation.yml` and add the theme package if necessary.
   2. In `doc/conf.py` change `html_theme = 'sphinx_rtd_theme'` to the name of your chosen theme.
   3. Commit and push your changes, verify the action has run successfully, and view the built site in your browser.
```
````

## Alternatives to GitHub and GitLab Pages

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
  sites and host them on the web, and GitLab offers a similar workflow.
```
