---
layout: episode
title: "Sphinx and ReStructuredText"
teaching: 5
exercises: 15
questions:
  - How do we get started on writing Sphinx documentation in RST?
objectives:
  - Create example Sphinx documentation and learn some RST along the way.
keypoints:
  - Sphinx and RST are relatively lightweight options for writing documentation.
---

## RST and Markdown
- Two of the most popular lightweight markup languages.
- Markdown considered simpler to use, but RST more extensible.
- Markdown convenient for smaller documents,
  but for larger and more complicated documents RST may be a better option.
- Sphinx was built around RST, but recently
[support for Markdown was added](http://blog.readthedocs.com/adding-markdown-support/).
- There are (unfortunately) [many flavors of Markdown](https://github.com/jgm/CommonMark/wiki/Markdown-Flavors).

## Type-along exercise: Build Sphinx documentation in RST

We will take the first steps in creating documentation using Sphinx, and learn some
RST syntax along the way.

Before we start, make sure that Sphinx is part of your Python installation or
environment. If you use Anaconda, you are set. If you use Miniconda or virtual
environments, make sure Sphinx is installed into the Miniconda or virtual
environment.
To test your Sphinx installation

```shell
$ python --version
Python 3.7.0

$ python -c "import sphinx; print(sphinx.__version__)"
1.8.2

```
The above command should return your python version and your Sphinx version,
if you receive an error  instead of the versions (any version would do)
e.g. command not found or ModuleNotFoundError
please follow installation instructions ([Sphinx](http://www.sphinx-doc.org)).

### Create a directory for your documentation, and generate the basic documentation template

```shell
$ mkdir doc-example
$ cd doc-example
$ sphinx-quickstart
```

The quickstart utility will ask you some questions. For this exercise, you can go
with the default answers except to specify a project name, your name and project version:.

```
> Root path for the documentation [.]:
> Separate source and build directories (y/n) [n]:
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
> Create Windows command file? (y/n) [y]:
```

A couple of files and directories are created:

<table style="width:50%;">
  <tr>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:15%"> File/directory </th>
    <th style="text-align: center; border: 1px solid black; padding: 3px; width:35%"> Contents </th>
  </tr>
  <tr>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> conf.py </td>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> Documentation configuration file </td>
  </tr>
  <tr>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> index.rst </td>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> Documentation master file </td>
  </tr>
  <tr>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> _build/ </td>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> Directory where docs are built </td>
  </tr>
  <tr>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> _templates/ </td>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> Your own HTML templates </td>
  </tr>
  <tr>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> _static/ </td>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> Static files (images, styles, etc.) copied to output directory on build </td>
  </tr>
  <tr>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> Makefile & make.bat </td>
    <td style="text-align: left; border: 1px solid black; padding: 3px;"> Makefiles to build documentation using make </td>
  </tr>
</table>

`Makefile` and `make.bat` (for Windows) are build scripts that wrap the sphinx commands, but
we will be doing it explicitly.

Let's have a look at the `index.rst` file, which is the main file of your documentation:

```
.. My Great Project documentation master file, created by
   sphinx-quickstart on Wed Jun 14 17:46:47 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to My Great Project's documentation!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

- We will not use the `Indices and tables` section now, so remove it.
- The top lines, starting with `..`, are a comment.
- The next lines are the table of contents. We can add content below:

```
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   feature-a
```
A common gotcha with directives is that **the first line of the content must be indented to the same level as the options (i.e., :maxdepth)**.

`feature-a` refers to a file `feature-a.rst`. Let's create it:

```
Feature A
=========

Subsection
----------

Exciting documentation in here.
Let's make a list (empty surrounding lines required):

- item 1

  - nested item 1
  - nested item 2

- item 2
- item 3
```

We now build the site:

```shell
$ ls

_build  _static  _templates  conf.py  feature-a.rst  index.rst

$ sphinx-build . _build

Running Sphinx v1.5.1
loading pickled environment... done
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 1 source files that are out of date
updating environment: 1 added, 1 changed, 0 removed
reading sources... [100%] index
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] index
generating indices... genindex
writing additional pages... search
copying static files... done
copying extra files... done
dumping search index in English (code: en) ... done
dumping object inventory... done
build succeeded.

$ ls _build

_sources  _static  feature-a.html  genindex.html  index.html  objects.inv search.html  searchindex.js
```

Now open the file `_build/index.html` in your browser by:

Linux users type:
```bash
xdg-open _build/index.html
```
OS X users type:
```bash
open _build/index.html
```
Windows users type:
```bash
start _build/index.html
```

Others:

enter `file:///home/user/doc-example/_build/index.html` in your browser (adapting the path to your case).

Hopefully you can now see a website. If so, then you are able to build Sphinx pages locally.
This is useful to check how things look before pushing changes to GitHub or elsewhere.


- Let's say we don't like the style of this website at all! We open the file `conf.py`, and change the option `html_theme` from `alabaster` to `default`. We then rebuild the site with `sphinx-build . _build`, and refresh the browser tab.

> ## Exercise: Add content to your example documentation
> 
> 1. Add a entry below feature-a labeled *feature-b* to the `index.rst` file.
> 2. Create a file `feature-b.rst` in the same directory as your `feature-a.rst` file.
> 3. Add some content to feature-b, rebuild with `sphinx-build`, and refresh the browser to look at the results.
> - [Help](http://docutils.sourceforge.net/docs/ref/rst/directives.html)
> 
> Experiment with the following RST syntax:
> 
> - \*Emphasized text\* and \*\*bold text\*\*
> - Headings
> 
> ```
> Level 1
> =======
> 
> Level 2
> -------
> 
> Level 3
> ^^^^^^^
> 
> Level 4
> """""""
> ```
> 
> - An image: `.. image:: image.png`
> - \`A link \<http://www.google.com\>\`_
> - Numbered lists (can be automatic using `#`)
> 
> ```
> 1. item 1
> 2. item 2
> #. item 3
> #. item 4
> ```
> 
> - Simple tables
> 
> ```
> ====== ======
> No.    Prime
> ====== ======
> 1      No
> 2      Yes
> 3      Yes
> 4      No
> ====== ======
> ```
> 
> - Code block using special marker `::`
> 
> ```
> The following is a code block::
> 
>   def hello():
>       print("Hello world")
> 
> ```
> 
> - Code block specifying syntax highlighting for other language than Python
> 
> ```
> .. code-block:: c
> 
>    #include <stdio.h>
>    int main()
>    {
>        printf("Hello, World!");
>        return 0;
>    }
> ```
> - You could include the contents of an external file using `literalinclude` directive, as follows:
> 
> ```
> .. literalinclude:: filename
> ```
> 
> - It is possible to combine `literalinclude` with code highlighting, line numbering, and even line highlighting.
> - We can also use jupyter notebooks (*.ipynb) with sphinx. It requires `nbsphinx` extension to be installed. See [nbsphinx documentation](http://nbsphinx.readthedocs.io/en/latest/) for more information
> ```
> .. toctree::
>    :maxdepth: 2
>    :caption: Contents:
> 
>    feature-a
>    <python_notebook_name>.ipynb
> ```
{: .task}

> ## Exercise: Update existing documentation that is not yours (Optional)
> 
> Very often we are using existing software/packages that have their own documentation in [ReadTheDocs](https://readthedocs.org/).
> It is good practice to participate in improving the documentation, especially when spotting problems or areas 
> that needs to be clarified.
> The goal of this exercise is to update/improve an [existing documentation](https://word-count.readthedocs.io/en/latest/) 
> available on [ReadTheDocs](https://readthedocs.org/).
> ### Take a few minutes to read it and before you start
>
> - Discuss the exercise idea with the classroom.
> - Distribute exercises among groups of 2-3 persons.
> - Open a GitHub issue and inform the community about the problem and how you
>  plan to solve it. Discuss why we do this.
> - Fork this project.
> - Commit to your fork. In your commit message auto-close the issue you have addressed.
> - Submit a pull request.
> - We then review the pull requests.
> - After the pull requests are merged we verify that documentation updates itself.
>
>
> ### Basic
>
> - Document the purpose of this example code.
> - Document how to clone the code.
> - Describe the project tree structure.
> - Write a sentence or two about Zipf's law and link to Wikipedia
>   (coordinate with the group working on the previous exercise).
> - Document how to check the code style with ``pycodestyle``.
> - Give other developers hints on how they can contribute to the documentation.
> - Document how to build the documentation locally
>   (coordinate with the group working on the previous exercise).
> - Add an example output.
> - Add an example plot
>   (coordinate with the group working on the previous exercise).
> - Document where/how to ask for help.
> - Add a math equation somewhere.
> 
> 
> ### Advanced
> 
> - Add a test and document how to run it.
> - Add the possibility to auto-document Python code.
> 
> 
> ### Meta
> 
> - Add new exercises ideas for future workshops (edit this file).
>
{: .task}

- For more RST functionality, see the [Sphinx documentation](http://www.sphinx-doc.org/en/stable/rest.html)
  and the [quick-reference](http://docutils.sourceforge.net/docs/user/rst/quickref.html).
- For Sphinx additions to standard RST, see [Sphinx Markup Constructs](http://www.sphinx-doc.org/en/1.7/markup/index.html).
