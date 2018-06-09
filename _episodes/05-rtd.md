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

- Host source code with documentation sources on GitHub.
- Each time you `git push` to the repository, a `post-receive` hook sends POST
  request to Read the Docs to rebuild the documentation.

```shell
$ curl -X POST http://readthedocs.org/build/myproject
```

- Read the Docs then fetches changes (typically from GitHub but can be
  somewhere else provided the repo is public) and rebuilds HTML and PDF.
- No problem to build several branches (versions) of your documentation.

---

## Exercise: Deploy Sphinx documentation to Read the Docs

In this exercise we will fork an example repository on GitHub and deploy it to Read the Docs.

We will use GitHub for this exercise but it will also work with any Git
repository with public read access.

1. In the first step, fork [this repository](https://github.com/coderefinery/rtdocs-example.git) and
then clone the fork to your laptop
    - The project contains a script for counting the frequency distribution of words in a given file and some documentation generated using sphinx. For bigger projects, we will have much more source files.
2. In the second step, enable the project on Read the Docs

### Step 1: Fork this [example repository](https://github.com/coderefinery/rtdocs-example.git) and clone the repository


```shell
$ git clone git@github.com:user/rtdocs-example.git  # adapt user, also ok to clone via https if you prefer
$ cd rtdocs-example
```
- The repository contains two folders
    - **source** folder contains the source code
    - **docs** folder contains the sphinx documentation

The docs folder contains the sphinx configuration file (conf.py) and the core file (index.rst) and some contents (usage.rst and contributions.rst).
  
- The sphinx files are generated using sphinx-quickstart that we have practiced earlier. The only changes are:
    - *autodoc: automatically insert docstrings from modules (y/n) [n]: y*
    - informing conf.py where to find the source code  - *sys.path.insert(0, os.path.abspath('../source'))*
  

#### Build HTML pages locally

Inside the cloned repository, run `sphinx-build . _build`.
Then point your browser to e.g.
`file:///home/user/rtdocs-example/docs/_build/index.html`. Adapt the path to the actual
path where you have cloned to (the `/home/user` part is almost certainly wrong in your case).


### Step 2: Enable the project on [Read the Docs](https://readthedocs.org)

Now you will import a project to Read the Docs by connecting to GitHub.  This
will automatically set up a webhook on GitHub and webhook integration on Read
the Docs so that `git push` will automatically rebuild the Read the Docs site.
One can also manually import the project to Read the Docs and set up the
webhook on GitHub, along with webhook integration on Read the Docs, but this
will not be needed here.

- Log into [Read the Docs](https://readthedocs.org) and visit your [dashboard](https://readthedocs.org/dashboard/)
- Click "Import a Project"
- Select "Connect to GitHub", and choose the doc-example repository
- Click "Next"

That's it! Your site should now be live on
[http://user-rtdocs-example.readthedocs.io](http://user-rtdocs-example.readthedocs.io)
(replace project name).

Finally, make some changes to your documentation
  - add documentation related to other functions
  - prerequisites and how to use the program
  - rules for contribution
  - commit and push them, and verify that the documentation website refreshes after your changes
(can take few seconds or a minute).

