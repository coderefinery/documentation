(sphinx)=

# Sphinx and reStructuredText

```{objectives}
- Create example Sphinx documentation and learn some RST along the way.
```

## Group exercise: Build Sphinx documentation using RST

We will take the first steps in creating documentation using Sphinx, and learn some
RST syntax along the way.

- Our goal in this episode is to build HTML pages locally on our computers.
- In the next episode we will learn how to deploy the documentation to a cloud service
  upon every `git push`.
- Please write your questions in the collaborative HackMD document so that we can answer
  them and discuss them together after the group sessions.

```{discussion} This lesson is built with Sphinx
- [Source code](https://raw.githubusercontent.com/coderefinery/documentation/main/content/sphinx.md)
- Try to compare the source code and the result side by side
- However, note that in this example we have used Markdown whereas in the following we will
  demonstrate reStructuredText which is more typical in combination with Sphinx
```

````{callout} Prerequisites: Check whether we have the software we need

Before we start, make sure that Sphinx is part of your Python installation or
Conda environment.

Test Sphinx installation within Python:

```console
$ python --version

Python 3.7.0
```

```console
$ sphinx-build --version

sphinx-build 3.5.4
```

```console
$ python -c "import sphinx_rtd_theme"

(no output)
```

Test Sphinx tool installation:

```console
$ sphinx-quickstart --version

sphinx-quickstart 3.5.4
```

The the above commands produce an error
instead of printing versions (the precise versions are not too important)
e.g. command not found or ModuleNotFoundError
please follow our
[installation instructions](https://coderefinery.github.io/installation/python/#installing-required-packages).
````

````{challenge} Exercise 1: Generate the basic documentation template

Create a directory for the example documentation, step into it, and inside
generate the basic documentation template:

```console
$ mkdir doc-example
$ cd doc-example
$ sphinx-quickstart
```

The quickstart utility will ask you some questions. For this exercise, you can go
with the default answers except to specify a project name, author name, and project release:

```
Separate source and build directories (y/n) [n]: <hit enter>
Project name: <your project name>
Author name(s): <your name>
Project release [0.1]: 0.1
Project language [en]: <hit enter>
```

A couple of files and directories are created:

| File/directory | Contents |
| -------------- | -------- |
| conf.py        | Documentation configuration file |
| index.rst      | Main file list other RST files to parse |
| _build/        | Directory where docs are built (you can decide the name) |
| _templates/    | Your own HTML templates |
| _static/       | Static files (images, styles, etc.) copied to output directory on build |
| Makefile       | Makefile to build documentation using make |
| make.bat       | Makefile to build documentation using make (Windows) |

`Makefile` and `make.bat` (for Windows) are build scripts that wrap the sphinx commands, but
we will be doing it explicitly.

Let's have a look at the `index.rst` file, which is the main file of your documentation:

```rst
.. myproject documentation master file, created by
   sphinx-quickstart on Tue May 11 18:38:22 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to myproject's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

- We will not use the `Indices and tables` section now, so remove it and everything below.
- The top four lines, starting with `..`, are a comment.
- The next lines are the table of contents. We can add content below:

```rst
.. toctree::
  :maxdepth: 2
  :caption: Contents:

  feature-a.rst
```
A common gotcha with directives is that **the first line of the content must be indented to the same level as the options (i.e., :maxdepth)**.

Let's create the file `feature-a.rst` which `index.rst` refers to:

```rst
Some Feature A
==============

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

```console
$ ls

_build  _static  _templates  conf.py  feature-a.rst  index.rst

$ sphinx-build . _build

Running Sphinx v3.5.4
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
```console
$ xdg-open _build/index.html
```
macOS users type:
```console
$ open _build/index.html
```
Windows users type:
```console
$ start _build/index.html
```

Others:

enter `file:///home/user/doc-example/_build/index.html` in your browser (adapting the path to your case).

Hopefully you can now see a website. If so, then you are able to build Sphinx pages locally.
This is useful to check how things look before pushing changes to GitHub or elsewhere.

Note that you can change the styling by editing `conf.py` and changing the value `html_theme`
(for instance you can set it to `sphinx_rtd_theme` to have the Read the Docs look).
````

````{challenge} Exercise 2: Add content to your example documentation

1. Add a entry below feature-a.rst labeled *feature-b.rst* to the `index.rst` file.
2. Create a file `feature-b.rst` in the same directory as your `feature-a.rst` file.
3. Add some content to feature-b, rebuild with `sphinx-build`, and refresh the browser to look at the results
  ([Help](http://docutils.sourceforge.net/docs/ref/rst/directives.html)).

Experiment with the following RST syntax:

- \*Emphasized text\* and \*\*bold text\*\*
- Headings

```rst
Level 1
=======

Level 2
-------

Level 3
^^^^^^^

Level 4
"""""""
```

- An image: `.. image:: image.png`
- \`A link \<http://www.google.com\>\`_
- Numbered lists (can be automatic using `#`)

```rst
1. item 1
2. item 2
#. item 3
#. item 4
```

- Simple tables

```rst
====== ======
No.    Prime
====== ======
1      No
2      Yes
3      Yes
4      No
====== ======
```

- Code block using special marker `::`

```rst
The following is a code block::

  def hello():
      print("Hello world")
```

- Code block specifying syntax highlighting for other language than Python

```rst
.. code-block:: c

  #include <stdio.h>
  int main()
  {
      printf("Hello, World!");
      return 0;
  }
```
- You could include the contents of an external file using `literalinclude` directive, as follows:

```rst
.. literalinclude:: filename
```

- It is possible to combine `literalinclude` with code highlighting, line numbering, and even line highlighting.
- We can also use jupyter notebooks (*.ipynb) with sphinx. It requires `nbsphinx` extension to be installed. See [nbsphinx documentation](http://nbsphinx.readthedocs.io/en/latest/) for more information
```rst
.. toctree::
  :maxdepth: 2
  :caption: Contents:

  feature-a.rst
  <python_notebook_name>.ipynb
```
````

````{challenge} Rendering (LaTeX) math equations

There are two different ways to display mathematical equations within Sphinx:
`pngmath` and `MathJax`.  While `pngmath` displays an equation as an image,
`MathJax` is using scalable vector graphics (quality remains the same after
zooming). For this reason, we strongly encourage you to use `MathJax` for
your mathematical equations.

To enable `MathJax` in Sphinx, you need first to add `sphinx.ext.mathjax` to
the list of extensions in `conf.py`:

```python
extensions = ['sphinx.ext.mathjax']
```

The following shows how to inline mathematics within a text:

```rst
This is an inline equation embedded :math:`a^2 + b^2 = c^2` in text.
```

An equation and equation array:
```rst
.. math::
  :label: myequation

  a^2 + b^2 = c^2

.. math::
  :label: myarray

  \begin{eqnarray}
    x^2 & : x < 0 \\
    x^3 & : x \ge 0 \\
  \end{eqnarray}
```

These equations can then be referenced using ``:eq:`myequation` `` and ``:eq:`myarray` ``.
````

---

### Where to find more

- For more RST functionality, see the [Sphinx documentation](http://www.sphinx-doc.org/en/stable/rest.html)
  and the [quick-reference](http://docutils.sourceforge.net/docs/user/rst/quickref.html).
- For Sphinx additions to standard RST, see [Sphinx Markup Constructs](http://www.sphinx-doc.org/en/1.7/markup/index.html).
- [https://docs.python-guide.org/writing/documentation/](https://docs.python-guide.org/writing/documentation/)

---

```{keypoints}
- Sphinx and RST are relatively lightweight options for writing documentation.
```
