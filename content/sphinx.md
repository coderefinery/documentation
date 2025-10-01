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

Our goal in this episode is to build HTML pages locally on our computers.

````{prereq} Before we start, let us verify whether we have the software we need

  You may need to activate your CodeRefinery conda environment we set up
  in the installation instructions.  This was covered as part of the
  installation instructions, but the most usual command to do this is:
  ```console
  $ conda activate coderefinery
  ```

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


```

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
  $ xdg-open _build/index.html
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


## Exercise: Adding more Sphinx content

`````{exercise} Sphinx-2: Add more content to your example documentation

1. Add a entry below `some-feature.md` labeled `another-feature.md` (or a better name) to the `index.rst` file.
2. Create a file `another-feature.md` in the same directory as the `index.rst` file.
3. Add some content to `another-feature.md`, rebuild with `sphinx-build . _build`, and refresh the browser to look at the results.
4. Use the [MyST Typography](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html) page as help.

Experiment with the following Markdown syntax:

- \*Emphasized text\* and \*\*bold text\*\*

- Headings:
```md
# Level 1

## Level 2

### Level 3

#### Level 4
```

- An image: `![alt text](image.png)`

- `[A link](https://www.example.org)`

- Numbered lists (numbers adjusted automatically):
```md
1. item 1
2. item 2
3. item 3
1. item 4
1. item 5
```

- Simple tables:
```md
| No.  |  Prime |
| ---- | ------ |
| 1    |  No    |
| 2    |  Yes   |
| 3    |  Yes   |
| 4    |  No    |
```

- Code blocks:
````markdown
The following is a Python code block:
```python
  def hello():
      print("Hello world")
```

And this is a C code block:
```c
#include <stdio.h>
int main()
{
    printf("Hello, World!");
    return 0;
}
```
````

- You could include an external file (here we assume a file called "example.py"
  exists; at the same time we highlight lines 2 and 3):
````markdown
```{literalinclude} example.py
:language: python
:emphasize-lines: 2-3
```
````

- We can also use Jupyter notebooks (*.ipynb) with Sphinx. It requires the
  [myst-nb](https://myst-nb.readthedocs.io/) extension to be installed.
`````


## Exercise: Sphinx and LaTeX

`````{exercise} Sphinx-3: Rendering (LaTeX) math equations

Math equations should work out of the box. In some older versions, you might need
to edit `conf.py` and add `sphinx.ext.mathjax`:
```python
extensions = ['myst_parser', 'sphinx.ext.mathjax']
```

Try this (result below):
````markdown
This creates an equation:
```{math}
a^2 + b^2 = c^2
```

This is an in-line equation, {math}`a^2 + b^2 = c^2`, embedded in text.
````

This creates an equation:
```{math}
a^2 + b^2 = c^2
```

This is an in-line equation, {math}`a^2 + b^2 = c^2`, embedded in text.
`````


## Exercise: Sphinx autodoc

`````{exercise} (optional) Sphinx-4: Auto-generating documentation from Python docstrings

1. Write some docstrings in functions and/or class definitions of an `example` python module:
```python
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.

    :param a: First number.
    :param b: Second number.
    :return: The product of a and b.
    """
    return a * b
```

2. In the file `conf.py` modify "extensions" and add 3 lines:
```python
extensions = ['myst_parser', "autodoc2"]

autodoc2_packages = [
    "multiply.py"
]
```

4. List `apidocs/index` in the toctree in `index.rst`.
```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   some-feature.md
   apidocs/index
```

5. Re-build the documentation and check the "API reference" section.
`````


## Confused about reStructuredText vs. Markdown vs. MyST?

- At the beginning there was reStructuredText and Sphinx was built for reStructuredText.
- Independently, Markdown was invented and evolved into a couple of flavors.
- Markdown became more and more popular but was limited compared to reStructuredText.
- Later, [MyST](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html)
  was invented to be able to write
  something that looks like Markdown but in addition can do everything that
  reStructuredText can do with extra directives.


## Good to know

- The `_build` directory is a generated directory
  and should not be part of the Git repository.  We recommend to add `_build`
  to `.gitignore` to prevent you from accidentally adding files below
  `_build` to the Git repository.
- [sphinx-autobuild](https://pypi.org/project/sphinx-autobuild/)
  provides a local web server that will automatically refresh your view
  every time you save a file - which makes writing and testing much easier.
- This is useful if you want to check the integrity of all internal and external links:
  ```console
  $ sphinx-build . -W -b linkcheck _build
  ```


## References

- [Sphinx documentation](https://www.sphinx-doc.org/)
- [Sphinx + ReadTheDocs guide](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/index.html)
- For more Markdown functionality, see the [Markdown guide](https://www.markdownguide.org/basic-syntax/).
- For Sphinx additions, see [Sphinx Markup Constructs](https://www.sphinx-doc.org/en/master/markup/index.html).
- [https://docs.python-guide.org/writing/documentation/](https://docs.python-guide.org/writing/documentation/)

```{keypoints}
- Sphinx and Markdown is a powerful duo for writing documentation.
- Another option is to use reStructuredText, see the [Sphinx documentation](https://www.sphinx-doc.org/en/stable/rest.html)
  and the [quick-reference](https://docutils.sourceforge.net/docs/user/rst/quickref.html)
- In the next episode we will learn how to deploy the documentation to a cloud service and update it
  upon every `git push`.
```
