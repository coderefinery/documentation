---
layout: episode
title: "Popular tools and solutions"
teaching: 10
exercises: 0
questions:
  - "What tools are out there?"
  - "What are their pros and cons?"
objectives:
  - "Choose the right tool for the right reason."
keypoints:
  - "Some popular solutions make reproducibility and maintenance of multiple code versions difficult."
  - "Do not reinvent the wheel: learn from large and busy open source projects."
---

## Comments in the source code

- Good for developers
- Requires terminal or repository browser
- Can be used to generate API documentation (examples later)
- Typically not sufficient for users
- Typically not enough on its own

---

## README files in the source tree

- Advantage
  - Versioned (goes with the code development)
- Disadvantage
  - You need a terminal or GitGub/GitLab browser to read them
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
  - Difficult to have versions
  - Typically needs to be hosted and maintained

---

## LaTeX/PDF

- Advantage
  - Popular and familiar in the physics and mathematics community
- Disadvantages
  - Not a lightweight markup
  - Barrier to write documentation is relatively high
  - Often requires sophisticated setup or a human running some compilation scripts
  - PDF format is not ideal for copy-paste ability of examples
  - PDF manual is not ideal on small screens (phone)
  - Typically not trivial to serve and update the generated PDF

---

## Doxygen

- Typically used to auto-generate API documentation
- Documented directly in the source code
- Popular in the C++ community (Doxygen is to C++ what Sphinx is to Python)
- Has support for Fortran and Python
- Many keywords are understood by Doxygen: http://www.stack.nl/~dimitri/doxygen/manual/commands.html
- Can be used to also generate higher-level ("human") documentation
- Can be deployed to GiHub/GitLab/Bitbucket pages

---

## RST and Markdown

- Both very lightweight
- Looks good in the browser
- Looks good in the terminal
- [Sphinx](http://sphinx-doc.org) can generate HTML/PDF/LaTeX from RST
- Basically all Python projects use Sphinx
- Good code highlighting: [Pygments](http://pygments.org), [Rouge](http://rouge.jneen.net)
- [Jekyll](https://jekyllrb.com) and other static site generators could be used, too
- Advantage of Sphinx
  - [Read the docs](http://readthedocs.org)

---

## HTML

- Avoid inventing your own solution
- Avoid maintaining own servers
- Use [Jekyll](https://jekyllrb.com) or other static site generators since they can be hosted on GitHub pages or GitLab pages for free
- Good code highlighting: [Pygments](http://pygments.org), [Rouge](http://rouge.jneen.net)
