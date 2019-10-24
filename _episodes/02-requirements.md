---
layout: episode
title: "Specs and requirements"
teaching: 10
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

## Own examples

We would like to show you some examples which are not ideal but we do not want
to point at others.

Instead we list some of the projects we have contributed to (possibly long time
ago), with varying quality of documentation:

- [pcd](https://github.com/rkdarst/pcd)
- [Dalton](https://daltonprogram.org/documentation/)
- [Autocmake](https://github.com/dev-cafe/autocmake)
- [Cubicle](https://github.com/bast/cubicle)
- [XCFun code](https://github.com/dftlibs/xcfun/) with [documentation 1](https://xcfun.readthedocs.io) and [documentation 2](http://dftlibs.org/xcfun/)

Discuss in groups what you like / or don't like about each before discussing it
as a class.

If you have examples of your own which you would like to share (on this website
or verbally), please do!

---

## What do we expect from a good documentation?

### Documentation comes in different forms - what *is* documentation?

(This is adapted from: [What nobody tells you about documentation](https://www.divio.com/blog/documentation/))

- **Tutorials**: learning-oriented, allows the newcomer to get started
- **How-to guides**: goal-oriented, shows how to solve a specific problem
- **Explanation**: understanding-oriented, explains a concept
- **Reference**: information-oriented, describes the machinery

These are distinct. For an excellent discussion, please see [What nobody tells you about documentation](https://www.divio.com/blog/documentation/).

---

### Versions

- Your code project should be versioned (version control).
- Enable reproducibility and avoid confusion: **documentation should be versioned** as well.
- Have you ever seen: *"We will soon release a new version and are updating the documentation.
  Some features may not be available in the version you have downloaded."*?

---

### Documentation should be placed and tracked close to the source code

- Documenting **close to the source code** (e.g. subdirectory ``doc/``) minimizes barrier to contribute.
- I should not need to log in to another machine or service and jump through hoops to contribute.

---

### Use a standard markup language

- Use either
  [RST](http://docutils.sourceforge.net/rst.html) or
  [Markdown](http://daringfireball.net/projects/markdown/) markup.
- GitHub and GitLab automatically render README.md or README.rst files.

---

### Readable on any device

- Many people browse the web on their phone or tablet.
- If you use standard solutions and services (to be demonstrated later in this
  lesson), you do not have to worry about this.

---

### Copy-paste-able

- PDF alone is not enough since **copy-pasting out of a PDF document can be difficult**.
- It is OK to provide a generated PDF in addition to a copy-paste-able format.

---

### Written by humans

- Automatically generated documentation (e.g. API documentation) is useful as
  complementary documentation but it does not replace tutorials written by
  humans.

---

### Information for contributors

- Make it easy for others to contribute: **document how you prefer others to contribute**.
- Users of your code may be shy to contribute code.
  Your **documentation provides a platform for your first contributions**.

---

### Installation instructions

- Give **step by step instructions for the basic case**.
  Additional information and caveats can be linked from there.
- List requirements and dependencies (libraries, compilers, environment).
- Include instructions for how to test for correctness after installation.

---

### Make the license explicit

- **Include a LICENSE file** with your source code.
- Without a license, your work is under exclusive copyright by default:
  others are not allowed to re-use or modify anything.
- GitHub and GitLab allows to choose a license from common license templates.

---

## Documentation checklist

Which items to include depends on the number of users apart from yourself.

- Purpose
- Authors
- License
- Recommended citation
- Usage
- Example
- FAQ
- Installation instructions
- Contact points (mailing list or forum or chat or issue tracker)
- Contribution guide
