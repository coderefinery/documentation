# Deploying Sphinx documentation to Read the Docs

```{questions}
- How do Python projects deploy their documentation?
- Can we use their solutions for projects which do not use Python?
```

```{objectives}
- Create a basic workflow which you can take home and adapt for your project.
```

## [Read the Docs](https://readthedocs.org)

- Runs Sphinx and converts RST or Markdown to HTML and PDF and hosts them for you
- Equations and images no problem
- Layout can be styled
- Many projects use [Read the Docs](https://readthedocs.org) as their main site
- It is no problem to serve using your own URL `http://myproject.org` instead of `http://myproject.readthedocs.io`

### Typical Read the Docs workflow

- Host source code with documentation sources on a public Git repository.
- Each time you `git push` to the repository, a `post-receive` hook triggers
  Read the Docs to rebuild the documentation.
- Read the Docs then clones the repository, runs Sphinx,
  and rebuilds HTML and PDF.
- No problem to build several branches (versions) of your documentation.

---

``````{challenge} Exercise: Deploy Sphinx documentation to Read the Docs

  In this exercise we will fork an example repository on GitHub/GitLab and
  deploy it to Read the Docs. The example project contains a script for counting the frequency distribution of words in a given file and some documentation generated using Sphinx. For bigger projects, we will have much more source files.

  We will use GitHub/GitLab for this exercise but it will also work with any Git repository with public read access.

  1. In the first step, we will fork the example repository and then clone the newly created repository to our laptop.
  2. In the second step, we will enable the project on Read the Docs, then commit and push some changes and check that the documentation is automatically rebuilt.

  `````{tabs}
    ````{tab} GitHub

    **Step 1:** Go to the [word-count project template](https://github.com/coderefinery/word-count/generate)
    and fork it to your namespace
    ````

    ````{tab} Gitlab

    **Step 1:** Go to the [word-count project template](https://gitlab.com/svenvanderburg/word-count)
    and fork it to your namespace
    ````
  `````

  **Clone the repository**

  The repository contains following two folders, among few other files and folders:
  - **source** folder contains the source code
  - **doc** folder contains the Sphinx documentation

  The doc folder contains the Sphinx configuration file (`conf.py`) and the index file (`index.rst`) and some contents (other RST files).
  The `conf.py` file has been adjusted to be able to autogenerate documentation from sources.


  **Build HTML pages locally**

  Inside the cloned repository, build the documentation and verify the result in your browser:

  ```shell
  $ sphinx-build doc _build
  ```

  **Test HTML pages links**

  Inside the cloned repository, check the integrity of all external links:

  ```
  $ sphinx-build doc -W -b linkcheck -d _build/doctrees _build/html
  ```

  `````{tabs}
    ````{tab} GitHub

    **Step 2:** Enable the project on [Read the Docs](https://readthedocs.org)

    **Import a project to Read the Docs by connecting to GitHub**

    - Log into [Read the Docs](https://readthedocs.org) and visit your [dashboard](https://readthedocs.org/dashboard/)
    - Click "Import a Project"
    - Select "Connect to GitHub", and choose the word-count repository
      (if you don't see this check your [connections](https://readthedocs.org/accounts/social/connections/)
    - Rename the project to user-word-count (replacing "user" with your GitHub username: we need a unique project name)
    - Click "Next"
    ````

    ````{tab} GitLab

    **Step 2:** Enable the project on [Read the Docs](https://readthedocs.org)

    **Import a project to Read the Docs by connecting to GitLab**

    - Log into [Read the Docs](https://readthedocs.org) and visit your [dashboard](https://readthedocs.org/dashboard/)
    - Click "Import a Project"
    - Select "Connect to GitLab", and choose the word-count repository
      (if you don't see this check your [connections](https://readthedocs.org/accounts/social/connections/)
    - Rename the project to user-word-count (replacing "user" with your GitLab username: we need a unique project name)
    - Click "Next"
    ````
  `````

  **Verify the result**

  That's it! Your site should now be live on
  http://user-word-count.readthedocs.io (replace project name).

  **Verify refreshing the documentation**

  Finally, make some changes to your documentation
  - Add documentation related to other functions
  - Prerequisites and how to use the program
  - Rules for contribution
  - Some example results (figures, tables, ...)
  - Commit and push them, and verify that the documentation website refreshes after your changes (can take few seconds or a minute)
``````

```{callout} Do not add the generated build directory to your repository

  The `_build` directory is generated locally with the command `sphinx-build doc _build` and allows you to check the content locally but it should not be part of the Git repository.
  We recommend to add `_build` to `.gitignore` to prevent you from accidentally adding files below `_build` to the Git repository.
```

```{callout} Running your own sphinx server

  We recommend to use Read the Docs to host your documentation but if you prefer, you can host your own Sphinx server.
  If you want to know more about it, look at:
  - [https://docs.readthedocs.io/en/latest/install.html](https://docs.readthedocs.io/en/latest/install.html)
  - [https://pypi.org/project/sphinx-autobuild/](https://pypi.org/project/sphinx-autobuild/)
  - [https://pypi.org/project/sphinx-server/](https://pypi.org/project/sphinx-server/)

```

```{callout} Migrating your own documentation to Sphinx/ Read the Docs

  - First convert your documentation to RST using [Pandoc](https://pandoc.org)
  - Create a file `index.rst` which lists all other RST files and provides the
    table of contents.
  - Add a `conf.py` file. You can generate a starting point for `conf.py` and
    `index.rst` with `sphinx-quickstart`, or you can take the examples in this
    lesson as inspiration.
  - Test building the documentation locally with `sphinx-build`.
  - Once this works, enable the project on Read the Docs and try to push a change to your documentation.

```
