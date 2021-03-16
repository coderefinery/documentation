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
  - Sphinx and ReadtheDocs provide a powerful way to create extensive (user) documentation.
---

## Motivation
What if a README file and in-code documentation is not enough? 
What if you want a more extensive documentation because you expect more users or collaborators?

A popular and nice solution is to use `Sphinx` together with `ReadtheDocs`
- `Sphinx` let's you create nicely-formatted HTML pages out of simple markdown files.
- `ReadtheDocs` easily connects to your github page and automatically deploys your Sphinx documentation for free!

The aim of this episode is to give you a glimpse of what you can accomplish with `Sphinx` + `ReadtheDocs`.

## Sphinx + ReadtheDocs demo
We have setup ReadtheDocs documentation for the 
[example project](https://github.com/escience-academy/coderefinery-documentation-example-project)].
Check it out [here](https://temperature-analysis-of-excel-files.readthedocs.io/en/latest/)!
How did we do this?

Let's look at the [example project](https://github.com/escience-academy/coderefinery-documentation-example-project) again.
It contains a [docs](https://github.com/escience-academy/coderefinery-documentation-example-project/tree/main/docs) folder.
The `docs` folder contains files that Sphinx needs to build your HTML documentation.

### index.rst
The `index.rst` file is the guts of your instructions for `Sphinx` to buid your documentation.
It is written in reStructuredText, which is a markup language, similar to MarkDown, but more powerful (but more difficult to write).
You don't need to understand the detais, but I hope you see that it corresponds to what is rendered in 
[the landing page](https://temperature-analysis-of-excel-files.readthedocs.io/en/latest/).
~~~Rest
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

   reference/analyse_spreadsheet

~~~
{. source}

