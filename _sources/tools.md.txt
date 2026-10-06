# Popular tools and solutions

```{questions}
- What tools are out there?
- What are their pros and cons?
```

```{objectives}
- Choose the right tool for the right reason.
```

---

## In-code documentation

- Comments, function docstrings, ...
- Advantages
  - Good for programmers
  - Version controlled alongside code
  - Can be used to auto-generate documentation for functions/classes
- Disadvantage
  - Probably not enough for users of the code

For a closer look at this see the {ref}`in-code-documentation` episode.

---

## README files

- Advantages
  - Versioned (goes with the code development)
  - It is often good enough to have a `README.md` or `README.rst` along with your code/script
- If you use README files, use either
  [RST](https://docutils.sourceforge.net/rst.html) or
  [Markdown](https://commonmark.org/help/)
- A great guide to README files: [MakeaREADME](https://www.makeareadme.com/)

For a closer look at this see the {ref}`writing-readme-files` episode.

---

## Plain Text formats: reStructuredText and Markdown

```markdown
# This is a section in Markdown   This is a section in RST
                                  ========================

## This is a subsection           This is a subsection
                                  --------------------

Nothing special needed for        Nothing special needed for
a normal paragraph.               a normal paragraph.

                                  ::

    This is a code block          This is a code block


**Bold** and *emphasized*.        **Bold** and *emphasized*.

A list:                           A list:
- this is an item                 - this is an item
- another item                    - another item

There is more: images,            There is more: images,
tables, links, ...                tables, links, ...
```

- Two of the most popular lightweight markup languages.
- reStructuredText (RST) has more features than Markdown but the choice is a matter of taste.
- There are (unfortunately) [many flavors of Markdown](https://github.com/jgm/CommonMark/wiki/Markdown-Flavors).
- Motivation to stick to a standard text-based format: **They make it easier to move the documentation to other tools
  which also expect a standard format, as the project/organization grows**.
- We use [MyST](https://myst-parser.readthedocs.io/en/latest/)
  flavored Markdown in the {ref}`sphinx` episode and the
  {ref}`gh-pages` example.
- Nice resource to learn Markdown: [Learn Markdown in 60 seconds](https://commonmark.org/help/)
- [Pandoc](https://pandoc.org/) can convert between MD and RST (and many other formats).



---

## HTML static site generators

There are many tools generate documentation 
that can be 
viewed locally,
or hosted on the web.

Here are some HTML static site generators, relevant in our communities.
These tools offer some or all of these features:
- **API Reference generation**: source code is read, scan for docstrings and render them
- **Search**: they offer a "whole site" search feature (non trivial, when viewing only one page).
              (if you can download )
- **Validation**: check that the code snipped in the documentation 
                  match the real behaviour of the code.
- **Continuous checks**: regenerate automatically every time you save, so that you can catch errors early

````{tabs}
  ```{group-tab} Python
     - [Sphinx](https://www.sphinx-doc.org) **← this is how this lesson material is built**  
       - Generate HTML/PDF/LaTeX from RST and Markdown (MyST)
       - Basically all Python projects use Sphinx but **Sphinx is not limited to Python**.
       - [Read the docs](https://about.readthedocs.com)
         hosts public Sphinx documentation for free!
       - **API Reference generation**: via 
         [autodoc](https://sphinx-autodoc2.readthedocs.io/en/latest/)
         or [autoapi](https://sphinx-autoapi.readthedocs.io/en/latest/)
       - **Search:**
         - limited, keyword-based client-side (Javascript that runs in browser)
         - Full-text server-side on [Read the docs](https://about.readthedocs.com)
       - **Validation**: via [doctest](https://docs.python.org/3/library/doctest.html)

     - [MkDocs](https://www.mkdocs.org/): A Markdown-first static site generator.
       - **API Reference generation**: via 
         [mkdocstrings](https://mkdocstrings.github.io/)
       - **Search:** search plugin for client-side (Javascript that runs in the browser - lunr.js)
       
     - [Doxygen](https://www.doxygen.nl/):
       - **API Reference generation**: has also support for Python
     
  ```
  ```{group-tab} R
     - [pkgdown](https://pkgdown.r-lib.org/)  
       - **API Reference generation**: via 
         [roxygen2](https://roxygen2.r-lib.org/) and 
       Rdconv 
       - Uses RMarkdown and a LaTeX-like syntax
       - **Search:** 
         - client-side (Javascript that runs in browser - fuse.js)
         - also typically available in RStudio

       Long-Form Documentation for R is typically contained in [vignettes](https://r-pkgs.org/vignettes.html).
     
  ```
  ```{group-tab} C/C++
     - [Doxygen](https://www.doxygen.nl/) 
       - **API Reference generation** out of the box, generates static call graph
       - Focus on Documentation directly in the source code
       - MarkDown-like syntax, with its own flavour and [special commands](https://www.doxygen.nl/manual/commands.html)
       - **Search**: 
         - limited keyword-based client-side
         - full text search server-side 
     - [Sphinx](https://www.sphinx-doc.org) can be also used to generate documentation for C++ projects, using the XML output from Doxygen via [Breathe](https://breathe.readthedocs.io/en/latest/)  

  ```

  ```{group-tab} Fortran
     - [Doxygen](https://www.doxygen.nl/): 
       - **API Reference generation** out of the box, generates static call graph (but has limited Fortran parsing capabilities)
       - Focus on Documentation directly in the source code
       - MarkDown-like syntax, with its own flavour and [special commands](https://www.doxygen.nl/manual/commands.html)
       - **Search**: 
         - limited keyword-based client-side
         - full text search server-side 

     - [FORD](https://forddocs.readthedocs.io/en/stable/)
       - Python-based
       - **Search:** client-side (Javascript that runs in the browser - lunr.js)
       
  ```
  ```{group-tab} Julia
     - [Documenter.jl](https://documenter.juliadocs.org/stable/)
       - Using MarkDown (JuliaMarkdown flavour)
       - Parses Julia code and in-code documentation/docstrings
       - **Search**: client-side (but typically the whole site is loaded for search on every page)
       - **Validation:** runs the code and checks 

  ```

  ```{group-tab} Rust
     [RustDoc](https://doc.rust-lang.org/rustdoc/what-is-rustdoc.html)
     - Uses MarkDown (CommonMark flavour)
     - **Search**: client-side (Javascript that runs in the browser - elasticlunr.js)
     - **Validation**: validates code examples when run with `--test`
  
  ```

  ```{group-tab} Any 
     These are general-purpose static website generators
     that match the philosophy of the other tools presented so far, 
     but might be better suited for blogging, reports or other kinds of publications:

     - [Hugo](https://gohugo.io)
     - [Hexo](https://hexo.io)
     - [Zola](https://www.getzola.org/) **← this is what we use for our project website and workshop websites**
     - [Jekyll](https://jekyllrb.com/), default for GitHub pages

     - [Franklin.jl](https://github.com/JuliaDocs/Franklin.jl): focuses on technical blogging for the Julia community
     - [Quarto](https://quarto.org/) converts markdown to websites, pdfs, ebooks and many other things (dynamic notebook-based documents) 
  ```
````

```{discussion}

Do you know an awesome tool or feature that should be in this list? 
Let us know! (Open a PR)

```

## Hosting Documentation on the Web 

GitHub, GitLab, and Bitbucket make it possible to serve HTML pages:
- [GitHub Pages](https://pages.github.com)
- [Bitbucket Pages](https://pages.bitbucket.io/)
- [GitLab Pages](https://pages.gitlab.io)

[Read The Docs](https://about.readthedocs.io) is also free to use for open source code,
and can be [connected](https://docs.readthedocs.com/platform/latest/reference/git-integration.htm) 
to common software forges.

---

## Wikis

- Popular solutions (but many others exist):
  - [MediaWiki](https://www.mediawiki.org)
  - [Dokuwiki](https://www.dokuwiki.org)
- Advantage
  - Barrier to write and edit is low
- Disadvantages
  - Typically disconnected from source code repository (**reproducibility**)
  - Difficult to serve multiple versions
  - Difficult to check out a specific old version
  - Typically needs to be hosted and maintained




---

## LaTeX/PDF

- Advantage
  - Popular and familiar in the physics and mathematics community
- Disadvantages
  - PDF format is not ideal for copy-pasting of examples
  - Possible, but not trivial to automate rebuilding documentation after every Git push



---


```{keypoints}
- Some popular solutions make reproducibility and maintenance of multiple code versions difficult.
```
