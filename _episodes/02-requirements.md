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

## What do we expect from a good documentation?

### Division into tutorials, FAQs, and keyword reference

- Show not only what is possible, but also how the software should be used: **tutorials**!
- Tutorials should contain **good defaults**.
- Ready examples that one can **copy-paste** to get quickly started.
- Up-to-date FAQ section.

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
