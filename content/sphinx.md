(sphinx)=

# Sphinx and Markdown

```{objectives}
- Understand how static site generators build websites out of plain
  text files.
- Create example Sphinx documentation and learn some Markdown along the way.
```

We will take the first steps in creating documentation using Sphinx, and learn some
MyST flavored Markdown syntax along the way.

```{discussion} This lesson is built with Sphinx
Try to compare the [source
code](https://raw.githubusercontent.com/coderefinery/documentation/main/content/sphinx.md)
and the result side by side.
```

- Our goal in this episode is to build HTML pages locally on our computers.
- In the next episode we will learn how to deploy the documentation to a cloud service
  upon every `git push`.

````{prereq} Before we start, let us verify whether we have the software we need
  Check whether Python is available
  (you should see a version; precise version is not so important):
  ```console
  $ python --version

  Python 3.11.5
  ```

  Check whether Sphinx is available
  (you should see a version; precise version is not so important):
  ```console
  $ sphinx-build --version

  sphinx-build 5.3.0
  ```

  Check whether the quickstart tool is available
  (you should see a version; precise version is not so important):
  ```console
  $ sphinx-quickstart --version

  sphinx-quickstart 5.3.0
  ```

  Check whether MyST parser is available
  (you should see no output):
  ```console
  $ python -c "import myst_parser"
  ```

If the above commands produce an error
(**command not found** or **module not found** or **ModuleNotFoundError**),
please follow our
[installation instructions](https://coderefinery.github.io/installation/conda-environment/).
But please don't give up if you don't have these - the episodes after this one will work even without these
tools.
````


## Exercise: Sphinx quickstart

````{exercise} Sphinx-1: Generate the basic documentation template

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
> Separate source and build directories (y/n) [n]: <hit enter>
> Project name: <your project name>
> Author name(s): <your name>
> Project release []: 0.1
> Project language [en]: <hit enter>
```

A couple of files and directories are created:

| File/directory | Contents |
| -------------- | -------- |
| conf.py        | Documentation configuration file |
| index.rst      | Main file in Sphinx |
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
   sphinx-quickstart on Sat Sep 23 17:35:26 2023.
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

   some-feature.md
```
Note that `some-feature.md` needs to be indented to align with `:caption:`.

We now need to tell Sphinx to use markdown files. To do this, we open
`conf.py` and replace the line:
```python
extensions = []
```

with this line so that Sphinx can parse Markdown files:
```python
extensions = ['myst_parser']
```

Let's create the file `some-feature.md` (in Markdown format) which we have just listed in
`index.rst` (which uses reStructured Text format).

```md
# Some feature

## Subsection

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
$ ls -1

_static
_templates
conf.py
index.rst
make.bat
Makefile
some-feature.md

$ sphinx-build . _build

... lots of output ...
build succeeded.

The HTML pages are in _build.

$ ls -1 _build

_sources
_static
genindex.html
index.html
objects.inv
search.html
searchindex.js
some-feature.html
```

Now open the file `_build/index.html` in your browser.
- Linux users, type:
  ```console
  r xdg-open _build/index.html
  ```
- macOS users, type:
  ```console
  $ open _build/index.html
  ```
- Windows users, type:
  ```console
  $ start _build/index.html
  ```
- If the above does not work:
  Enter `file:///home/user/doc-example/_build/index.html` in your browser (adapting the path to your case).

Hopefully you can now see a website. If so, then you are able to build Sphinx pages locally.
This is useful to check how things look before pushing changes to GitHub or elsewhere.

Note that you can change the styling by editing `conf.py` and changing the value `html_theme`
(for instance you can set it to `sphinx_rtd_theme` (if you have that Python package installed)
to have the Read the Docs look).
````


## Exercise: Sphinx content

````{exercise} Sphinx-2: Add content to your example documentation

1. Add a entry below feature-a.md labeled *feature-b.md* to the `index.rst` file.
2. Create a file `feature-b.md` in the same directory as your `feature-a.md` file.
3. Add some content to feature-b, rebuild with `sphinx-build`, and refresh the browser to look at the results
  ([Help](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html)).

Experiment with the following Markdown syntax:

- \*Emphasized text\* and \*\*bold text\*\*
- Headings

```md
# Level 1

## Level 2

### Level 3

#### Level 4
```

- An image: `![](image.png)`
- `[A link](http://www.google.com)`
- Numbered lists (numbers adjusted automatically)

```md
1. item 1
2. item 2
3. item 3
1. item 4
1. item 5
```

- Simple tables

```md

| No.  |  Prime |
| ---- | ------ |
| 1    |  No    |
| 2    |  Yes   |
| 3    |  Yes   |
| 4    |  No    |

```

- Code block

~~~md
The following is a code block:
```
  def hello():
      print("Hello world")
```
~~~

- Code block specifying syntax highlighting for other language than Python

~~~md
 ```c

  #include <stdio.h>
  int main()
  {
      printf("Hello, World!");
      return 0;
  }
 ```
~~~
- You could include the contents of an external file using `{include}` directive, as follows:

~~~md
 ```{include} ../README.md
 ```
~~~

<!--
Note, that this will not resolve e.g. image paths within README.md, use experimental feature `{literalinclude}` instead:

~~~md
 ```
 {literalinclude} ../README.md
 :language: md
 ```
~~~
-->

- It is possible to combine `{include}` with code highlighting, line numbering, and even line highlighting.
- We can also use Jupyter notebooks (*.ipynb) with Sphinx. It requires the
  [myst-nb](https://myst-nb.readthedocs.io/) extension to be installed.
````


## Exercise: Sphinx and LaTeX

````{exercise} (optional) Sphinx-3: Rendering (LaTeX) math equations

There are two different ways to display mathematical equations within Sphinx:
`pngmath` and `MathJax`.  While `pngmath` displays an equation as an image,
`MathJax` is using scalable vector graphics (quality remains the same after
zooming). For this reason, we strongly encourage you to use `MathJax` for
your mathematical equations.

To enable `MathJax` in Sphinx, you need first to add `sphinx.ext.mathjax` to
the list of extensions in `conf.py`:

```python
extensions = ['myst_parser', 'sphinx.ext.mathjax']
```

The following shows how to inline mathematics within a text:

```md
This is an inline equation embedded {math}`a^2 + b^2 = c^2` in text.
```

This is an inline equation embedded {math}`a^2 + b^2 = c^2` in text.

This creates an equation or it's own line:
~~~
```{math}
a^2 + b^2 = c^2
```
~~~

```{math}
a^2 + b^2 = c^2
```

For more math syntax (separate to what is above, not needed for this exercise), check [the MyST documentation](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#syntax-amsmath).

````


## Exercise: Sphinx autodoc

````{exercise} (optional) Sphinx-4: Auto-generating documentation from docstrings.

1. Write some docstrings in functions and/or class definitions of `my-module` python module. You can use sphinx syntax as follows:

```python
def mean_temperature(data):
    """
    Get the mean temperature

    :param data (pandas.DataFrame): A pandas dataframe with air temperature measurements.

    :returns: The mean air temperature (float)
    """
    temperatures = data['Air temperature (degC)']
    return float(sum(temperatures)/len(temperatures))
```

2. In the the folder `doc-example` add a file `API.rst` with the following contents:

```rst
Python API
==========

my-module
+++++++++

.. automodule:: my-module
   :members:
```

3. In the file `conf.py` add:

```python
import os
import sys

sys.path.insert(0, os.path.abspath("../"))

# in extensions add "sphinx.ext.autodoc"
extensions = ['myst_parser', "sphinx.ext.autodoc"]
```

~~~{callout}
If your working tree is different you might have to adapt the path passed in `sys.path.insert(0, os.path.abspath("../"))` such that it points to the python module.
~~~

4. In `index.rst` add `API` below `feature-a.md`. This will add a section with the contents of `API.rst`.
5. Re-build the documentation and check the `API` section and how the docstrings get rendered.

```bash
cd doc-example
sphinx-build . _build
```

````

[sphinx-autobuild](https://pypi.org/project/sphinx-autobuild/)
provides a local web server that will automatically refresh your view
every time you save a file - which makes writing and testing much easier.

---

## Where to find more

- [Sphinx documentation](https://www.sphinx-doc.org/)
- [Sphinx + ReadTheDocs guide](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/index.html)
- For more Markdown functionality, see the [Mardown guide](https://www.markdownguide.org/basic-syntax/).
- For Sphinx additions, see [Sphinx Markup Constructs](http://www.sphinx-doc.org/en/master/markup/index.html).
- [https://docs.python-guide.org/writing/documentation/](https://docs.python-guide.org/writing/documentation/)

---

```{keypoints}
- Sphinx and Markdown are relatively lightweight options for writing documentation.
- Another option is to use reStructuredText, see the [Sphinx documentation](http://www.sphinx-doc.org/en/stable/rest.html)
  and the [quick-reference](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
```
