---
layout: episode
title: "Recommendations"
teaching: 10
exercises: 0
questions:
  - What tools can we recommend?
objectives:
  - Automatize and give the boring work to machines.
  - Make contributing documentation easy, simple, and direct.
  - Sometimes take a step back and consider different perspectives to your documentation.
  - Do not maintain own servers, use good available services.
---

## Setup

- Whatever solution you choose, make it automatically rebuild pages upon `git push`.
- Documentation needs to be close to the source code and evolve with the source code.
- When using code review make sure that new functionality always comes with documentation.

---

## Example

- Great example: [https://snakemake.readthedocs.io](https://snakemake.readthedocs.io)
- Written in reStructuredText (RST)
- Rendered to HTML/PDF/LaTeX by [Sphinx](http://sphinx-doc.org)
- Served by [Read the Docs](https://readthedocs.org)

---

## Markdown and RST

- Two of the most popular lightweight markup languages.

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

- Widely used by static site generators such as [Sphinx](http://sphinx-doc.org),
  [Jekyll](https://jekyllrb.com), and others.
- Markdown considered simpler to use, but RST more extensible.
- Markdown convenient for smaller documents,
  but for larger and more complicated documents RST may be a better option.
- Sphinx was built around RST, but recently
  [support for Markdown was added](http://blog.readthedocs.com/adding-markdown-support/).
- There are (unfortunately) [many flavors of Markdown](https://github.com/jgm/CommonMark/wiki/Markdown-Flavors).

Learn Markdown:
- [Learn Markdown in 60 seconds](http://commonmark.org/help/)
- [https://dillinger.io](http://dillinger.io)
- [https://stackedit.io](https://stackedit.io)

Learn RST:
- [http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html](reStructuredText Primer)

---

## Avoid Wikis as code documentation

- Popular solutions (but many others exist):
  - [MediaWiki](https://www.mediawiki.org)
  - [Dokuwiki](https://www.dokuwiki.org)
  - GitHub wiki
  - GitLab wiki
- Advantage
  - Barrier to write and edit is low
- Disadvantages
  - **Wiki history is disconnected from source history**
  - Difficult to serve multiple versions
  - Difficult to check out a specific version
