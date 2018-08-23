---
layout: episode
title: "Sphinx and Read the Docs exercise"
teaching: 5
exercises: 30
objectives:
  - Contribute documentation to a project powered by Sphinx and Read the Docs.
---

## How it works

- Documentation written in RST (or Markdown)
- [Sphinx](http://sphinx-doc.org) renders this to HTML/PDF/LaTeX
- Result deployed to and served by [Read the Docs](https://readthedocs.org)


### Sphinx is not only for Python

Sphinx comes from the Python community but you can use
it to document any project in **any language**.


### How documentation is updated

- By a `git push`
- GitHub informs Read the Docs after every push
- Read the Docs clones the project and runs Sphinx
- Read the Docs then updates the HTML


### Sphinx documentation

- [Sphinx documentation](http://www.sphinx-doc.org/en/stable/rest.html)
- [Quick reference](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
- [Sphinx Markup Constructs](http://www.sphinx-doc.org/en/stable/markup/index.html)

---

## Exercise

We will return to the word-count example from the
[https://coderefinery.github.io/reproducible-research/](reproducible research lesson)
which we have partially documented using Sphinx/RTD.

- [https://github.com/coderefinery/word-count](Repository)
- [https://word-count.readthedocs.io](Documentation on RTD)

Your goal:

- Fork the repository
- Clone the fork
- [https://word-count.readthedocs.io/en/latest/exercises.html](Contribute some documentation) using pull requests which we review and integrate together


### Which files to edit

Below is the directory listing for the word-count example project.
To add/edit documentation, we only need to edit files under `doc`:

```
.
├── data
│   ├── abyss.txt
│   ├── isles.txt
│   ├── last.txt
│   ├── LICENSE_TEXTS.md
│   └── sierra.txt
├── doc
│   ├── conf.py
│   ├── credit.rst
│   ├── dependencies.rst
│   ├── exercises.rst
│   ├── index.rst
│   ├── purpose.rst
│   └── usage.rst
├── Dockerfile
├── license.md
├── Makefile
├── Makefile_all
├── manuscript
├── matplotlibrc
├── processed_data
├── README.md
├── requirements.txt
├── results
├── Snakefile_all
└── source
    ├── plotcount.py
    ├── wordcount.py
    └── zipf_test.py
```


### How to preview changes locally

We will require the Python packages `sphinx` and `sphinx_rtd_theme`.
If you are missing `sphinx_rtd_theme`, you can replace `sphinx_rtd_theme` by `alabaster`
in `doc/conf.py`.

We can build the documentation locally using:

```shell
$ sphinx-build doc _build
```

Now open the file `_build/index.html` in your browser by:

Linux users type:

```shell
$ xdg-open _build/index.html
```

OS X users type:

```shell
$ open _build/index.html
```

Windows users type:

```shell
$ start _build/index.html
```

Others: enter `file:///home/user/word-count/_build/index.html`
in your browser (adapting the path to your case).

Hopefully you can now see the documentation pages. If so, then you are able to
build Sphinx pages locally.  This is useful to check how things look before
pushing changes to GitHub or elsewhere.
