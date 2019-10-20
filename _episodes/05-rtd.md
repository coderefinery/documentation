---
layout: episode
title: "Deploying Sphinx documentation to Read the Docs"
teaching: 5
exercises: 15
questions:
  - How do Python projects deploy their documentation?
  - Can we use their solutions for projects which do not use Python?
objectives:
  - Create a basic workflow which you can take home and adapt for your project.
---

## [Read the Docs](https://readthedocs.org)

- Free Sphinx hosting
- RST or Markdown
- PDF can be generated on the fly
- Equations and images no problem
- Layout can be styled
- Many projects use [Read the Docs](https://readthedocs.org) as their main site
- It is no problem to serve using your own URL `http://myproject.org` instead of `http://myproject.readthedocs.io`

---

## Typical Read the Docs workflow

- Host source code with documentation sources on a public Git repository.
- Each time you `git push` to the repository, a `post-receive` hook triggers
  Read the Docs to rebuild the documentation.
- Read the Docs then clones the repository
  and rebuilds HTML and PDF.
- No problem to build several branches (versions) of your documentation.

---

> ## Exercise: Deploy Sphinx documentation to Read the Docs
> 
> In this exercise we will make a copy of an example repository on GitHub and deploy it to Read the Docs.
> 
> We will use GitHub for this exercise but it will also work with any Git
> repository with public read access.
> 
> 1. In the first step, generate a new repository based on
>  [this word-count example project template](https://github.com/coderefinery/word-count/generate) and
>  then clone the newly created repository to your laptop.
>     - The project contains a script for counting the frequency distribution of words in a given file and some documentation generated using sphinx. For bigger projects, we will have much more source files.
> 2. In the second step, enable the project on Read the Docs.
> 
> ### Step 1: Go to the [word-count project template](https://github.com/coderefinery/word-count/generate), copy it to your namespace, and clone the repository
> 
> - The repository contains following two folders, among few other files and folder. 
>     - **source** folder contains the source code
>     - **doc** folder contains the sphinx documentation
> 
> The doc folder contains the sphinx configuration file (`conf.py`) and the
> core file (`index.rst`) and some contents (`usage.rst` and `contributions.rst`).
> The `conf.py` file has been adjusted to be able to autogenerate documentation from sources.
> 
> #### Build HTML pages locally
> 
> Inside the cloned repository, run 
>```shell
>$ sphinx-build doc _build
>```
> and verify the result in your browser.
> 
> #### Test HTML pages links
>
> Inside the cloned repository, check the integrity of all external links:
>```
>$ sphinx-build doc -W -blinkcheck -d _build/doctrees _build/html
>```
>
> ### Step 2: Enable the project on [Read the Docs](https://readthedocs.org)
> 
> Now you will import a project to Read the Docs by connecting to GitHub.  This
> will automatically set up a webhook on GitHub and webhook integration on Read
> the Docs so that `git push` will automatically rebuild the Read the Docs site.
> One can also manually import the project to Read the Docs and set up the
> webhook on GitHub, along with webhook integration on Read the Docs, but this
> will not be needed here.
> 
> - Log into [Read the Docs](https://readthedocs.org) and visit your [dashboard](https://readthedocs.org/dashboard/)
> - Click "Import a Project"
> - Select "Connect to GitHub", and choose the word-count repository
> - Rename the project to user-word-count (replacing "user" with your GitHub username: we need a unique project name)
> - Click "Next"
> 
> That's it! Your site should now be live on
> http://user-word-count.readthedocs.io (replace project name).
> 
> Finally, make some changes to your documentation
>   - Add documentation related to other functions
>   - Prerequisites and how to use the program
>   - Rules for contribution
>   - Some example results (figures, tables, ...)
>   - Commit and push them, and verify that the documentation website refreshes after your changes
>     (can take few seconds or a minute)
{: .task}
 
> ## Do not add `_build` directory to your repository
>
> The `_build` directory is generated locally with the command `sphinx-build doc _build`
> and allows you to check the content locally but it should not be part of the Git repository.
> We recommend to add `_build` to `.gitignore` to prevent you from accidentally
> adding files below `_build` to the Git repository.
>
{: .callout}

> ## Running your own sphinx server
>
> We recommend to use Read the Docs to host your documentation but this may
> not be suitable for you. For instance, many industries prefer to host their 
> own sphinx server.
> If you want to know more about it, look at:
> - [https://docs.readthedocs.io/en/latest/install.html](https://docs.readthedocs.io/en/latest/install.html)
> - [https://pypi.org/project/sphinx-autobuild/](https://pypi.org/project/sphinx-autobuild/)
> - [https://pypi.org/project/sphinx-server/](https://pypi.org/project/sphinx-server/)
>
{: .callout}

