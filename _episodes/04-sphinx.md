---
layout: episode
title: "Sphinx and ReadtheDocs demo"
teaching: 10
exercises: 0
questions:
  - How do I easily create user documentation?
objectives:
  - Know what Sphinx and ReadtheDocs can offer.
keypoints:
  - Sphinx + ReadtheDocs provide a powerful way to create extensive (user) documentation.
---

## Motivation
What if a README file and in-code documentation is not enough? 
What if you want a more extensive documentation because you expect more users or collaborators?

A very popular and nice solution is to use `Sphinx` together with `ReadtheDocs`:
- `Sphinx` let's you create nicely-formatted HTML pages out of simple markdown files. It is programming language-independent.
- `ReadtheDocs` easily connects to your github page and automatically deploys your Sphinx documentation for free!

The aim of this episode is to give you a glimpse of what you can accomplish with `Sphinx` + `ReadtheDocs`.

---

## Sphinx + ReadtheDocs demo
We have setup ReadtheDocs documentation for the 
[example project](https://github.com/escience-academy/coderefinery-documentation-example-project).
Check it out [here](https://temperature-analysis-of-excel-files.readthedocs.io/en/latest/)!
How did we set this up?

Let's look at the [example project](https://github.com/escience-academy/coderefinery-documentation-example-project) again.
It contains a [docs](https://github.com/escience-academy/coderefinery-documentation-example-project/tree/main/docs) folder.
The `docs` folder contains files that Sphinx needs to build your HTML documentation.
Let's look at some files and see how they correspond to the HTML documentation.

### index.rst
The `index.rst` file is the guts of your instructions for `Sphinx` to buid your documentation.
It is written in reStructuredText, which is a markup language.
It is similar to MarkDown, but more powerful (the downside is that it is more difficult to write).
You don't need to understand the detais, but I hope you see that it corresponds to what is rendered in 
[the landing page](https://temperature-analysis-of-excel-files.readthedocs.io/en/latest/):
~~~rest
.. Temperature analysis using excel files documentation master file, created by
   sphinx-quickstart on Mon Mar 15 13:42:37 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Temperature analysis using excel files
==================================================================
A python script for the analysis of temperatures in excel files.

Why should I use this project ?
-------------------------------
It makes it easy to analyse excel files with temperatures in them.

How to cite this project?
-------------------------
Please email `training@esciencecenter.nl` to get instructions on how to properly cite this project.

Contributing
------------
You are welcome to contribute to the code via pull requests.
Please have a look at the NLeSC guide for guidelines about software development.

.. toctree::
   :maxdepth: 1
   :caption: Where to start?

   setup
   quick-start

.. toctree::
   :maxdepth: 1
   :caption: API Reference

   analyse_spreadsheet

~~~
{: .source}

### analyse_spreadsheet.rst
A very powerful feature of Sphinx is that it can autogenerate an API reference based on your docstrings.
You need to configure Sphinx a little bit, and then all you need is these few lines:...
~~~Rest
analyse_spreadsheet
===================

.. automodule:: analyse_spreadsheet
    :members:
~~~
{: .source}

...to render [a beautiful API reference](https://temperature-analysis-of-excel-files.readthedocs.io/en/latest/analyse_spreadsheet.html).
The content of this page corresponds 1-to-1 with the docstrings in 
[analyse_spreadsheet.py](https://github.com/escience-academy/coderefinery-documentation-example-project/blob/main/analyse_spreadsheet.py).
So if you maintain good docstrings you automatically get a nice API reference as a bonus!

---

> ## ReadtheDocs - github integration
> ReadtheDocs adds a webhook to your Github repository. 
> Whenever you make a change in your repository code, a new build of your documentation is automatically triggered!
> This way, your documentation is always up to date with your code.
> You can also setup ReadtheDocs to show different documentations matching different versions of your code.
{: .callout} 
