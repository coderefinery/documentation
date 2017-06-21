---
layout: episode
title: "Specs and requirements"
teaching: 15
exercises: 0
questions:
  - What requirements and specifications can we impose on a good documentation?
objectives:
  - Arrive at a set of specifications that we can use as checklist for designing and deploying code documentation.
keypoints:
  - Documentation is part of the code.
  - Documentation should be close to the source code to minimize the barrier to contribute.
  - Documentation needs to be versioned for reproducibility.
  - Use lightweight and standard markup languages such as RST or Markdown.
---

## Let's have a look at some project websites
- [ABINIT](http://www.abinit.org/)
- [Dalton](http://daltonprogram.org/)
- [PSI4](http://www.psicode.org/)
- [Jupyter Notebooks](http://jupyter-notebook.readthedocs.io/en/latest/)
- [Julia](https://docs.julialang.org/en/stable/)
- [Seaborn](https://seaborn.pydata.org)
- [Boost](http://www.boost.org)
- [Octopus](http://octopus-code.org/wiki/Main_Page)

---

## What do we expect from a good documentation?

- Separate tutorials, FAQ and keyword reference
- Versioned
- Close to the source code
- Information for contributors (allow pull request)
- Lightweight markup
- Minimize server maintenance
- Readable on any device
- Installation instructions
- Project's license
- Reader-friendly

---

### Division into tutorials, FAQ and keyword reference

- Show not only what the software can do, but also how the software should be used: tutorials!
- Tutorials should contain good defaults.
- Ready examples that one can copy-paste to get quickly started.
- Up-to-date FAQ section

---

### Versions

- Your code project should be versioned (version control).
- If the project has versions, the documentation should too.
- Important for reproducibility: I should be able to install a code version
  from 3 years ago and for this I will probably also need the possibility to
  see the documentation from 3 years ago.
- If you release your code you probably need at least two documentation
  versions: one for the released code, one for the bleeding edge code - make
  sure your documentation supports that.

---

### Documentation should be placed and tracked close to the source code

- Documenting close to the source code minimizes barrier to contribute.
- I should not need to log in to another machine or service and jump through hoops to contribute.
- Ideally we prefer to write documentation where we also write code.
- Include instructions on how to contribute.

---

### Use a lightweight markup

- LaTeX is not lightweight enough.
- Use a standard markup language.
- Use RST or Markdown.
- GitHub and GitLab automatically render README.md or README.rst files.

---

### Make the documentation readable on any device

- Many people browse the web on their phone or tablet.
- If you use standard solutions and services (to be demonstrated later in this
  lesson), you do not have to worry about this.

---

### Written by humans

- Prose
- Automatically generated documentation (e.g. API documentation) is useful as
  complementary documentation but it does not replace tutorials written by
  humans.

---

## Documentation checklist

- Purpose
- Authors
- License
- Recommended citation
- Usage
- Example
- Installation instructions
- Requirements and dependencies (libraries, compilers, environment)
- Contact points (mailing list or forum or chat or issue tracker)
- Contribution guide
