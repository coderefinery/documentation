# Popular tools and solutions

```{questions}
- What tools are out there?
- What are their pros and cons?
```

```{objectives}
- Choose the right tool for the right reason.
```

## What tools and solutions are out there?

- [Comments in the source code](#comments-in-the-source-code)
- [README files in the source tree](#readme-files-in-the-source-tree)
- [Wikis](#wikis)
- [LaTeX/PDF](#latexpdf)
- [Doxygen](#doxygen)
- [reStructuredText and Markdown](#restructuredtext-and-markdown)
- [HTML static site generators](#html-static-site-generators)

---

### Comments in the source code

- Advantages
  - Good for programmers
  - Version controlled alongside code
  - Can be used to auto-generate documentation for functions/classes
- Disadvantage
  - Probably not enough for users

---

### README files in the source tree

- Advantage
  - Versioned (goes with the code development)
  - It is often good enough to have a `README.md` or `README.rst` along with your code/script
- Disadvantage
  - You need a terminal or GitHub/GitLab browser to read them
  - Sometimes users have no access to the source tree
- If you use README files, use either
  [RST](http://docutils.sourceforge.net/rst.html) or
  [Markdown](https://commonmark.org/help/) markup

---

### Wikis

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

### LaTeX/PDF

- Advantage
  - Popular and familiar in the physics and mathematics community
- Disadvantages
  - PDF format is not ideal for copy-paste ability of examples
  - Possible, but not trivial to automate rebuilding documentation after every Git push

---

### Doxygen

- Auto-generates API documentation
- Documented directly in the source code
- Popular in the C++ community
- Has support for C, Fortran, Python, Java, etc.,
  see [Doxygen Github Repo](https://github.com/doxygen/doxygen)
- Many keywords are understood by Doxygen:
  [Doxygen special commands](http://www.doxygen.nl/manual/commands.html)
- Can be used to also generate higher-level ("human") documentation
- Can be deployed to GiHub/GitLab/Bitbucket Pages

---

### reStructuredText and Markdown

- Two of the most popular lightweight markup languages.
- reStructuredText (RST) has more features than Markdown but the choice is a matter of taste.
- Markdown convenient for smaller documents,
  but for larger and more complicated documents RST may be a better option.
- There are (unfortunately) [many flavors of Markdown](https://github.com/jgm/CommonMark/wiki/Markdown-Flavors).

```
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

- We will use RST in a Sphinx example and Markdown in a GiHub pages example

Experiment with Markdown:
- [Learn Markdown in 60 seconds](http://commonmark.org/help/)
- [https://dillinger.io](http://dillinger.io)
- [https://stackedit.io](https://stackedit.io)

---

### HTML static site generators

There are many tools that can turn RST or Markdown into beautiful HTML pages:

- [Sphinx](http://sphinx-doc.org) **<- we will exercise this**
  - Generate HTML/PDF/LaTeX from RST and Markdown.
  - Basically all Python projects use Sphinx but **Sphinx is not limited to Python**
  - [Read the docs](http://readthedocs.org)
    hosts public Sphinx documentation for free!

- [Jekyll](https://jekyllrb.com) **<- this is how this lesson material is built**
  - Generates HTML from Markdown.
  - GitHub supports this without adding extra build steps.

- [pkgdown](https://pkgdown.r-lib.org/)
  - Popular in the R community

- [MkDocs](https://www.mkdocs.org/)
- [GitBook](https://www.gitbook.com/)
- [Hugo](https://gohugo.io)
- [Hexo](https://hexo.io)

There are many more ...

GitHub, GitLab, and Bitbucket make it possible to serve HTML pages:
- [GitHub Pages](https://pages.github.com)
- [Bitbucket Pages](https://pages.bitbucket.io/)
- [GitLab Pages](https://pages.gitlab.io)

---

```{keypoints}
- Some popular solutions make reproducibility and maintenance of multiple code versions difficult.
```
