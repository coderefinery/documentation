---
layout: episode
title: "Discussion of various alternatives"
teaching: 10
exercises: 0
questions:
  - "A question that this episode will answer?"
  - "Another question?"
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

## Technology

- Do not write own CSS
    - Bootstrap http://getbootstrap.com
    - Jekyll http://jekyllrb.com

- Do not maintain own web servers
    - GitHub pages https://pages.github.com for project websites
    - Bitbucket pages http://pages.bitbucket.org

---

## Typical GitHub pages workflow

- Create `gh-pages` branch for your project which holds website sources
- Every push automatically rebuilds http://myorg.github.io/myproject/ [site does not exist]
- It is good practice to use Bootstrap for CSS
- GitHub provides an automatic page generator: you can create a shiny project website in 5 minutes
- See also https://pages.github.com for step-by-step guides

---

template: inverse

## Project documentation

---

## Problems with many code projects

- Parts of the documentation are outdated/incomplete
- Documentation workflows undocumented
- We typically program first and document later (or never)
- No manual for developers (first steps, call tree, where to start, what to do and what not to do)
- One documentation for different versions (either just confusing or documentation for
  older versions is just dropped)
- Have to read a lot of text in different places just to get started
- Keyword-driven (what is possible) instead of tutorial-driven (what is recommended)
- With some projects it is impossible to get a result after 5 minutes of reading
- Some scientific projects take pride in being inaccessible, hard to understand, undocumented, opaque

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

---

## Specs of a good documentation

- Close to the code (minimize barrier)
- Versions: If the project has versions, the documentation should too
- Lightweight markup (LaTeX is not lightweight enough)
- Readable on any device
- Division into tutorials and keyword reference
- Tutorials contain good defaults
- Ready examples that one can copy-paste to get quickly started
- Prose
- Written by humans

---

## Read the Docs

- https://readthedocs.org
- Free Sphinx hosting
- RST or Markdown
- PDF can be generated on the fly
- Equations and images no problem
- Layout can be changed
- It is no problem to serve from GitHub pages or Read the Docs using your own URL
- Many projects use https://readthedocs.org as their main site

---

## Typical Read the Docs workflow

- Host source code with documentation sources on GitHub
- `post-receive` sends POST request to Read the Docs to rebuild the documentation

```shell
$ curl -X POST http://readthedocs.org/build/myproject
```

- Read the Docs then fetches changes (typically from GitHub but can be somewhere else provided the repo is public)
  and rebuilds HTML and PDF
- No problem to build several branches (versions) of your documentation

---

## Good practices (1/2)

- Whatever solution you choose, make it automatically rebuild pages upon `git push`
- If you need to ask somebody to run some scripts on the server after you have modified sources,
  that will not work in practice (does not scale)
- Answer questions with an URL to (updated) documentation
    - Email answers get lost/forgotten
    - Answer and improve doc at the same time
    - Long-term lazy
    - Chance is that next time the user/colleague
      will find the answer by him/herself
    - Trains people to read the doc

---

## Good practices (2/2)

- Write documentation that you would like to read
- When using code review make sure that new functionality always comes with documentation
- Some people who install and test the software know nothing about the theory behind the code
    - Busy user support at computing centers
    - Vendors who run benchmarks
- Market success stories (pictures, scaling, molecules, be proud)
