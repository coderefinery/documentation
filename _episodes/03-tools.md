---
layout: episode
title: "Popular tools and solutions"
teaching: 10
exercises: 0
questions:
  - What tools are out there?
  - What are their pros and cons?
objectives:
  - Choose the right tool for the right reason.
keypoints:
  - Some popular solutions make reproducibility and maintenance of multiple code versions difficult.
  - Do not reinvent the wheel - learn from large and busy open source projects.
---

## Comments in the source code

- Good for programmers
- Typically not sufficient for users
- Can be used to auto-generate documentation for functions/classes
- Version controlled alongside code

---

## README files in the source tree

- Advantage
  - Versioned (goes with the code development)
- Disadvantage
  - You need a terminal or GitHub/GitLab browser to read them
- If you use README files, use either
  [RST](http://docutils.sourceforge.net/rst.html) or
  [Markdown](http://daringfireball.net/projects/markdown/) markup

---

## Wikis

- Popular solutions (but many others exist):
  - [MediaWiki](https://www.mediawiki.org)
  - [Dokuwiki](https://www.dokuwiki.org)
- Advantage
  - Barrier to write and edit is low
- Disadvantages
  - Difficult to serve multiple versions
  - Difficult to check out a specific old version
  - Typically needs to be hosted and maintained
  - Typically disconnected from source code repository

---

## LaTeX/PDF

- Advantage
  - Popular and familiar in the physics and mathematics community
- Disadvantages
  - PDF format is not ideal for copy-paste ability of examples
  - PDF manual is not ideal on small screens (phone)
  - Typically not trivial to serve and update the generated PDF

---

## Doxygen

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

## RST and Markdown

- Lightweight and readable
- [Sphinx](http://sphinx-doc.org) can generate HTML/PDF/LaTeX from RST and Markdown
- Basically all Python projects use Sphinx but Sphinx is not limited to Python
- Good code highlighting: [Pygments](http://pygments.org), [Rouge](http://rouge.jneen.net)
- [Jekyll](https://jekyllrb.com) and other static site generators could be used, too
- Advantage of Sphinx: [Read the docs](http://readthedocs.org)
  hosts public [Sphinx](http://sphinx-doc.org) documentation for free!

```
# This is a section in Markdown   This is a section in RST
                                  ========================

## This is a subsection           This is a subsection
                                  --------------------

No markup is needed for           No markup is needed for
a normal paragraph.               a normal paragraph.

                                  ::

    This is a code block            This is a code block


**Bold** and *emphasized*.        **Bold** and *emphasized*.

A list:                           A list:
- this is an item                 - this is an item
- another item                    - another item

There is more: images,            There is more: images,
tables, links, ...                tables, links, ...
```

Experiment with Markdown:
- [Learn Markdown in 60 seconds](http://commonmark.org/help/)
- [https://dillinger.io](http://dillinger.io)
- [https://stackedit.io](https://stackedit.io)

Experiment with reStructuredText:
- [http://rst.ninjs.org/](http://rst.ninjs.org/)

---

## HTML

- Projects can easily autogenerate HTML from RST or Markdown
- Make it possible to avoid maintaining own web servers to host
  documentation and use resources like:
    - [GitHub Pages](https://pages.github.com)
    - [Bitbucket Pages](https://pages.bitbucket.io/)
    - [GitLab Pages](https://pages.gitlab.io)
