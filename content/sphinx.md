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
[installation instructions](https://coderefinery.github.io/installation/conda/).
But please don't give up if you don't have these - the episodes after this one will work even without these
tools.
````

(quickstart)=
## Exercise: Setting up a Sphinx project

`````{exercise} Sphinx-1: Generate the basic documentation template

Create a directory for the example documentation, step into it, and inside
generate the basic documentation template:

```console
$ mkdir doc-example
$ cd doc-example
```

We create the basic structure of the project manually.

| File/directory | Contents |
| -------------- | -------- |
| conf.py        | Documentation configuration file |
| index.md      | Main file in Sphinx |

Let's create the `index.md` with this content:

````md

# Documentation example with Sphinx

A small example of how to use Sphinx and MyST 
to create easily readable and aesthetically pleasing
documentation.

```{toctree}
:maxdepth: 2
:caption: Contents:
some-feature.md
```

````

Note that indentation and spaces play a role here.


We also create a `conf.py` configuration file, with this content:
```python
project = 'Test sphinx project'
author = 'Alice, Bob'
release = '0.1'            
                                                                                
extensions = ['myst_parser']
                                                                                
exclude_patterns = ['_build']
```

For more information about the configuration,
see the [Sphinx documentation](https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration).

Let's create the file `some-feature.md` (in Markdown format) which we have just listed in
`index.md`:

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

conf.py
index.md
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

Note that you can change the styling by 
adding the line
```py
html_theme = "<my favorite theme>"
```
in `conf.py`. 
For instance you can use`sphinx_rtd_theme` 
to have the Read the Docs look
(make sure the `sphinx_rtd_theme` python package is available first)
`````

```{seealso} 

Sphinx also provides a tool called `sphinx-quickstart`
that guides you in the creation of the project.
The reason why we do not use it here
is that it does not use Markdown by default,
but a more complex format called ReStructured Text (ReST).
```


## Exercise: Adding more Sphinx content

`````{exercise} Sphinx-2: Add more content to your example documentation

1. Add a entry below `some-feature.md` labeled `another-feature.md` (or a better name) to the `index.md` file.
2. Create a file `another-feature.md` in the same directory as the `index.md` file.
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

- Math equations with LaTeX should work out of the box. Try this (result below):
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


````{admonition} Older versions of Sphinx
In some older versions, you might need
to edit `conf.py` and add `sphinx.ext.mathjax`:
```python
extensions = ['myst_parser', 'sphinx.ext.mathjax']
```
````


`````

(api-exercise)=
## Exercise: Sphinx autodoc

`````{exercise} Sphinx-3: Auto-generating documentation from Python docstrings

1. Write some docstrings in functions and/or class definitions to a python module `multiply.py`:
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

2. In the file `conf.py` add `autodoc2` to the "extensions", and add the list `autodoc2_packages` which will mention `"multiply.py"`:
```python
extensions = ['myst_parser', "autodoc2"]

autodoc2_packages = [
    "multiply.py"
]
```
If you already have extensions from another exercise, just add `"autodoc2"` to the existing list.

4. Add `apidocs/index` to the toctree in `index.md`.
````md
```{toctree}
:maxdepth: 2
:caption: Contents:

...
apidocs/index
````

5. Re-build the documentation and check the "API reference" section.
`````

(jupyter-exercise)=
## Exercise: Using Jupyter with Sphinx

`````{exercise} Sphinx-4: Writing Sphinx content with Jupyter

1. For simplicity, create a text-based notebook files `flower.md` in the same directory as the `index.md` file. This file will be converted to a Jupyter notebook by the `myst_nb` Sphinx extension and then executed by Jupyter. Fill the file with the following content:
````md
---
file_format: mystnb
kernelspec:
  name: python3
---
# Flower plot

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(5, 8), subplot_kw={"projection": "polar"})
theta = np.arange(0, 2 * np.pi, 0.01)
r = np.sin(5 * theta)
ax.set_rticks([])
ax.set_thetagrids([])
ax.plot(theta, r);
ax.plot(theta, np.full(len(theta), -1));
```
````
Note that there needs to be a title in the notebook (a heading starting with a single `#`), that will be used as an entry and link in the table of content.
2. In the file `conf.py` modify `extensions` to remove `"myst_parser"` and add `"myst_nb"` ([you will get an error if you include both](https://myst-nb.readthedocs.io/en/latest/quickstart.html)):
```python
extensions = ["myst_nb"]
```
Note that MyST parser functionality is included in MyST NB, so everything else will continue to work as before.

3. List `flower` in the toctree in `index.md`.
````md
```{toctree}
:maxdepth: 2
:caption: Contents:
...
flower.md
```
````

4. Re-build the documentation and check the "Flower" section.

5. Alternatively, you can directly add `.ipynb` files saved from Jupyter notebook or Jupyter lab. Just make sure to list it in the toctree in `index.md` with the correct path.

If you have problems, consider cleaning manually the `jupyter_execute` directory.

`````

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
- In the next episode we will learn how to deploy the documentation to a cloud service and update it
  upon every `git push`.
```
