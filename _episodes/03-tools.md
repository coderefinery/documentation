---
layout: episode
title: "Tools"
teaching: 10
exercises: 0
questions:
  - "What tools are out there?"
  - "What are their pros and cons?"
objectives:
  - "This is one objective of this episode."
  - "This is another objective of this episode."
  - "Yet another objective."
  - "And not to forget this objective."
keypoints:
  - "This is an important key point."
  - "Another important key point."
  - "One more key point."
---

## README files in the source tree

- advantage: versionnable (goes with the code development)
- disadvantage: you need a terminal to read it
- better than nothing

---

## Wikis

- Dokuwiki https://www.dokuwiki.org
- advantage: barrier to write and edit is low
- disadvantage: difficult to have versions

---

## LaTeX/PDF

- Not a lightweight markup
- Barrier to write documentation is relatively high
- PDF format is not ideal for copy-paste ability of examples
- PDF manual is not ideal on small screens (phone)
- Typically not trivial to serve and update the generated PDF

---

## Doxygen

- Typically used to autogenerate API documentation
- Documented directly in the source code
- Popular in the C++ community (Doxygen is to C++ what Sphinx is to Python)
- Has support for Fortran and Python
- Many keywords are understood by Doxygen: http://www.stack.nl/~dimitri/doxygen/manual/commands.html
- Can be used to also generate higher-level ("human") documentation
- Can be deployed to GiHub/Bitbucket pages

---

## RST and Markdown

- Both very lightweight
- Looks good in the browser
- Looks good in the terminal
- Sphinx http://sphinx-doc.org can generate HTML from RST
- Basically all Python projects use Sphinx
