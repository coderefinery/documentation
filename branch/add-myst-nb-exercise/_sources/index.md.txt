# How to document your research software

In this lesson we will discuss different solutions for implementing and
deploying code documentation.

We will start with a discussion about **what makes a good README**. For many
projects, a README is more than enough.

We will then learn how to build documentation with the
**documentation generator** [Sphinx](https://www.sphinx-doc.org) (and compare it
with others) and how to
deploy it to [Read the Docs](https://readthedocs.org), a service which hosts
open documentation for free.

This demonstration will be **independent of programming languages**.

We will also learn how
to deploy a **project website or personal homepage** to [GitHub Pages](https://pages.github.com).
The approach that we will learn will be transferable to
[GitLab Pages](https://about.gitlab.com/features/pages/) and
[Bitbucket Pages](https://pages.bitbucket.io).

```{prereq}
1. Basic understanding of Git.

2. For the Sphinx part, You need to have
   [sphinx](https://www.sphinx-doc.org) and [sphinx_rtd_theme](https://sphinx-rtd-theme.readthedocs.io/) installed
   (they are part of the [coderefinery environment](https://coderefinery.github.io/installation/conda-environment/)).

3. For the [GitHub Pages](https://pages.github.com) part you need a [GitHub](https://github.com) account.

If you wish to follow in the terminal and are new to the command line, we
recorded a [short shell crash course](https://youtu.be/xbTTDLA3txI).
```

```{csv-table}
:widths: auto
:delim: ;

10 min ; {doc}`wishlist`
10 min ; {doc}`tools`
20 min ; {doc}`in-code-documentation`
30 min ; {doc}`writing-readme-files`
30 min ; {doc}`sphinx`
20 min ; {doc}`gh_workflow`
20 min ; {doc}`gh-pages`
5 min  ; {doc}`summary`
```

```{toctree}
:maxdepth: 1
:caption: The lesson

wishlist.md
tools.md
in-code-documentation.md
writing-readme-files.md
sphinx.md
gh_workflow.md
gh-pages.md
summary.md
```

```{toctree}
:maxdepth: 1
:caption: Reference

Shell crash course <https://youtu.be/xbTTDLA3txI>
exercises.md
guide.md
license.md
```

```{toctree}
:maxdepth: 1
:caption: About

All lessons <https://coderefinery.org/lessons/core/>
CodeRefinery <https://coderefinery.org/>
Reusing <https://coderefinery.org/lessons/reusing/>
```
