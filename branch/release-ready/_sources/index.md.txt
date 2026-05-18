# How to document your research software

In this lesson we will discuss different solutions for implementing and
deploying code documentation.

This demonstration will be mostly **independent of programming languages**
(you will be able to follow and do all the exercises
using the [CodeRefinery conda environment](https://coderefinery.github.io/installation/conda/)).


We will discuss best practices, and briefly discuss the available tools.

Then we will discuss the form of documentation which is the most immediate to write:
**in-code** comments, and docstrings.

We will step up our game and discuss **what makes a good README**. For many
projects, a curated README is enough.

We will then learn how to build documentation with the
**documentation generator** [Sphinx](https://www.sphinx-doc.org) and how to
deploy it to [GitHub Pages](https://pages.github.com).
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

An optional episode is about 
deploying a **project website or personal homepage** 
to [GitHub Pages](https://pages.github.com).


```{csv-table}
:widths: auto
:delim: ;
5 min ; Intro
5 min ; {doc}`in-code-documentation`
10 min ; {doc}`writing-readme-files`
35 min ; {doc}`sphinx` (with exercise)
10 min ; Break
30 min ; {doc}`gh_workflow` (with exercise)
10 min ; {doc}`tools`
10 min ; {doc}`wishlist`
5 min  ; {doc}`summary`
```

```{toctree}
:maxdepth: 1
:caption: The lesson

in-code-documentation.md
writing-readme-files.md
sphinx.md
gh_workflow.md
tools.md
wishlist.md
summary.md
```

```{toctree}
:maxdepth: 1
:caption: Supplementary material

gh-pages.md
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
