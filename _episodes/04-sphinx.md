---
layout: episode
title: "A primer on Sphinx and ReStructuredText"
teaching: 10
exercises: 0
questions:
  - How do we get started on writing Sphinx documentation in RST?
objectives:
  - Create sample Sphinx documentation and learn some RST along the way.
keypoints:
  - WRITEME
  - WRITEME
---

## RST and Markdown 
- two of the most popular lightweight markup languages
- Markdown considered simpler to use, but RST more extensible
- Markdown convenient for smaller documents, 
  but for larger and more complicated documents RST may be a better option
- Sphinx was built around RST, but recently 
[support for Markdown was added:](http://blog.readthedocs.com/adding-markdown-support/)

## Type-along exercise: Build Sphinx documentation in RST from scratch

We will take the first steps in creating documentation using Sphinx, and experiment 
with RST syntax along the way.

Before we start, make sure that Sphinx is part of your Python installation or
environment. If you use Anaconda, you are set. If you use Miniconda or virtual
environments, make sure Sphinx is installed into the Miniconda or virtual
environment.

### Create a directory for your documentation, and generate the basic documentation template:

```shell
$ mkdir example-doc
$ cd example-doc
$ sphinx-quickstart
```

The quickstart utility will ask you some questions. For this exercise, enter the following answers (in most cases
the default options are used. Note that people using Windows should change the last answer to `y`). 

```
> Root path for the documentation [.]:
> Separate source and build directories (y/n) [n]: y
> Name prefix for templates and static dir [_]:
> Project name: My Great Project
> Author name(s): <your-name>
> Project version []: 0.1
> Project release [0.1]:
> Project language [en]:
> Source file suffix [.rst]:
> Name of your master document (without suffix) [index]:
> Do you want to use the epub builder (y/n) [n]:
> autodoc: automatically insert docstrings from modules (y/n) [n]:
> doctest: automatically test code snippets in doctest blocks (y/n) [n]:
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]:
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:
> coverage: checks for documentation coverage (y/n) [n]:
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]:
> ifconfig: conditional inclusion of content based on config values (y/n) [n]:
> viewcode: include links to the source code of documented Python objects (y/n) [n]:
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:
> Create Makefile? (y/n) [y]:
> Create Windows command file? (y/n) [y]: n
```

A number of files are created in the source directory:

<table style="width:50%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:15%"> Directory </th>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:35%"> Contents </th>
  </tr>
  <tr>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> source/conf.py </td>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> Documentation configuration file. </td>
  </tr>
  <tr>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> source/index.rst </td>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> Documentation master file.. </td>
  </tr>
  <tr>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> Makefile </td>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> Makefile to generate documentation. </td>
  </tr>
  <tr>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> make.bat </td>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> Batch file to build docs on Windows. </td>
  </tr>
</table>

Let's have a look at the `index.rst` file, which is the master document.

- We will not use the *Indices and tables* section now, so remove it.