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
- [VASP](https://www.vasp.at/)
- [Dalton](http://daltonprogram.org/)
- [PSI4](http://www.psicode.org/)
- [Jupyter Notebooks](http://jupyter-notebook.readthedocs.io/en/latest/)
- [Julia](https://docs.julialang.org/en/stable/)
- [Seaborn](https://seaborn.pydata.org)
- [Boost](http://www.boost.org)
- [Octopus](http://octopus-code.org/wiki/Main_Page)

---

## What do we expect from a good documentation?

- [Separate tutorials, FAQ and keyword reference](#tutorials)
- [Versioned](#versions)
- [Close to the source code](#close-to-source)
- [Lightweight markup](#markup)
- [Readable on any device](#devices)
- [Reader-friendly](#reader-friendly)
- [Information for contributors (allow pull request)](#contributors)
- [Installation instructions](#installation)
- [Project's license](#license)

---

### Division into tutorials, FAQ and keyword reference {#tutorials}

- Show not only what the software can do, but also how the software should be used: tutorials!
- Tutorials should contain good defaults.
- Ready examples that one can copy-paste to get quickly started.
- Up-to-date FAQ section.

---

### Versions {#versions}

- Your code project should be versioned (version control).
- If the project has versions, the documentation should too.
- Important for reproducibility: I should be able to install a code version
  from 3 years ago and for this I will probably also need the possibility to
  see the documentation from 3 years ago.
- If you release your code you probably need at least two documentation
  versions: one for the released code, one for the bleeding edge code - make
  sure your documentation supports that.

---

### Documentation should be placed and tracked close to the source code {#close-to-source}

- Documenting close to the source code minimizes barrier to contribute.
- I should not need to log in to another machine or service and jump through hoops to contribute.
- Ideally we prefer to write documentation where we also write code.

---

### Use a lightweight markup {#markup}

- LaTeX is not lightweight enough.
- Use a standard markup language.
- Use RST or Markdown.
- GitHub and GitLab automatically render README.md or README.rst files.

---

### Make the documentation readable on any device {#devices}

- Many people browse the web on their phone or tablet.
- If you use standard solutions and services (to be demonstrated later in this
  lesson), you do not have to worry about this.

---

### Written by humans {#reader-friendly}

- Prose
- Automatically generated documentation (e.g. API documentation) is useful as
  complementary documentation but it does not replace tutorials written by
  humans.

---

### Information for contributors {#contributors}

- You probably want people to help out, but it needs to be easy. Document how to contribute by pull requests.
- Users of your code may be shy to contribute code. Your documentation provides a platform for your first contributions.
- If you get contributions to your code or documentation that need further work, provide positive feedback.

---

### Installation instructions {#installation}

- If you haven't documented how to install your code, people might not want to use it.
- Give step by step instructions for the basic case. Additional information and caveats can be linked from there.
- Include instructions for how to test for correctness after installation.

---

### Make the license explicit {#license}

- Include a LICENSE file with your source code.
- Without a license, your work is under exclusive copyright by default (others are not allowed to re-use or modify anything).

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
