---
layout: episode
title: "Motivation and wishlist"
teaching: 15
exercises: 25
questions:
  - Why documenting code?
  - What is our wishlist on a suitably good documentation?
objectives:
  - Arrive at a checklist for designing and deploying code documentation.
keypoints:
  - Documentation is part of the code and should be versionable.
  - For research projects a README file and in-code documentation is often enough.
---

## Why documenting code?

> ## Exercise in the main room
>
> - **Use the collaborative document**.
> - Is project documentation important? Why?
> - How would you describe a useful documentation?
> - How can you motivate your colleagues to contribute to the documentation?
{: .challenge}

> ## Our motivation (but let us brainstorm first)
>
> - You will probably use your code in the future and may forget details.
> - You may want others to use your code (almost impossible without documentation).
> - You may want others to contribute to the code.
> - Shield your limited time and let the documentation answer FAQs.
{: .solution}

---
## What do we expect from a suitably good documentation?
> ## Exercise
> 1. Think of projects of which you like the documentation. What do you like about them?
> 2. Think of projects for which you don't like the documentation. What don't you like about them?
>    Are you missing anything?
>
> **NB: You can choose a mature library with lots of users for this exercise, but try to also
> think of less mature projects you had to collaborate on, or papers you had to reproduce.**  
{: .challenge}

> ## Our wishlist (but let us brainstorm first)
>
> ### Versions
>
> - Your code project should be versioned (version control).
> - Enable reproducibility and avoid confusion: **documentation should be versioned** as well.
> - Have you ever seen: *"We will soon release a new version and are updating the documentation.
>   Some features may not be available in the version you have downloaded."*?
>
>
> ### Documentation should be placed and tracked close to the source code
>
> - Documenting **close to the source code** (e.g. subdirectory ``doc/``) minimizes barrier to contribute.
> - I should not need to log in to another machine or service and jump through hoops to contribute.
> - It is often good enough to have a `README.md` or `README.rst` along with your code/script.
>
>
> ### Use a standard markup language
>
> - Use either
>   [reStructuredText (RST)](http://docutils.sourceforge.net/rst.html) or
>   [Markdown](http://daringfireball.net/projects/markdown/) markup.
> - GitHub and GitLab automatically render `README.md` or `README.rst` files.
>
>
> ### Copy-paste-able
>
> - PDF alone is not enough since **copy-pasting out of a PDF document can be difficult**.
> - It is OK to provide a generated PDF in addition to a copy-paste-able format.
>
>
> ### Written by humans
>
> - Automatically generated documentation (e.g. API documentation) is useful as
>   complementary documentation but it does not replace tutorials written by
>   humans.
>
>
> ### Installation instructions
>
> - Give **step by step instructions for the basic case**.
>   Additional information and caveats can be linked from there.
> - List requirements and dependencies (libraries, compilers, environment).
> - Include instructions for how to test for correctness after installation.
>
>
> ### Make the license explicit
>
> - **Include a LICENSE file** with your source code.
> - Without a license, your work is under exclusive copyright by default:
>   others are not allowed to re-use or modify anything.
> - GitHub and GitLab allows to choose a license from common license templates.
>
>
> ### Information for contributors
>
> - Make it easy for others to contribute: **document how you prefer others to contribute**.
> - Users of your code may be shy to contribute code.
>   Your **documentation provides a platform for your first contributions**.
{: .solution}

---

> ## Documentation checklist
>
> Which items to include depends on the number of users apart from yourself.
>
> - Purpose
> - Authors
> - License
> - Recommended citation
> - Copy-paste-able example to get started
> - Dependencies and their versions or version ranges
> - Installation instructions
> - Tutorials covering key functionality
> - Reference documentation (e.g. API) covering all functionality
> - How do you want to be asked questions (mailing list or forum or chat or issue tracker)
> - Possibly a FAQ section
> - Contribution guide
{: .discussion}


> ## Keep it simple
> For most scientific projects in-code documentation 
> and a well thought out README file is enough. 
> Think about the audience and purpose. 
{: .callout}
---

### Good resources

- [A beginner’s guide to writing documentation](http://www.writethedocs.org/guide/writing/beginners-guide-to-docs/)
- [What nobody tells you about documentation](https://www.divio.com/blog/documentation/)
