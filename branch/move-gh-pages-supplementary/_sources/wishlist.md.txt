# Motivation and wishlist

## Motivation

```{discussion} Motivation-1: Why documenting code?

**Use the collaborative document**:
- Is project documentation important? Why?
- How would you describe a useful documentation?
- How can you motivate your colleagues to contribute to the documentation?
```

```{solution} Our motivation (but let us brainstorm first)

- You will probably use your code in the future and may forget details.
- You may want others to use your code (almost impossible without documentation).
- You may want others to contribute to the code.
- Shield your limited time and let the documentation answer FAQs.
```


## What do we expect from a suitably good documentation?

```{note} Documentation comes in different forms - what *is* documentation?

  - **Tutorials**: learning-oriented, allows the newcomer to get started
  - **How-to guides**: goal-oriented, shows how to solve a specific problem
  - **Explanation**: understanding-oriented, explains a concept
  - **Reference**: information-oriented, describes the machinery

  Read more:
  - <https://www.divio.com/blog/documentation/>
  - <https://diataxis.fr/>
  - <https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/>
```

**There is no one size fits all**: often for small projects a `README.md` or
`README.rst` can be enough (more about these formats later).


(checklist)=

## Creating a checklist

```{discussion} Motivation-2: Create a wishlist

**Use the collaborative document**:
  - Let us create a wishlist for how we would like documentation to be.
  - Below are some of our ideas but please do not look at them yet.
  - We are sure you will come up with ideas we did not think about.
```

````{solution} Our wishlist (but let us brainstorm first)

  **Versions**

  - Your code project should be versioned (version control).
  - Enable reproducibility and avoid confusion: **documentation should be versioned** as well.
  - Have you ever seen: *"We will soon release a new version and are updating the documentation.
    Some features may not be available in the version you have downloaded."*?


  **Documentation should be placed and tracked close to the source code**

  - Documenting **close to the source code** (e.g. subdirectory ``doc/``) minimizes barrier to contribute.
  - I should not need to log in to another machine or service and jump through hoops to contribute.
  - It is often good enough to have a `README.md` or `README.rst` along with your code/script.


  **Use a standard markup language**

  ```{instructor-note} Markup
    Markup is a set of human readable instructions that is used to tell the computer how a document shall be styled and structured. By using a markup language we can for example write a `*` or `-` where we want a bullet point to appear in the rendered document.
  ```
  - offers formatting flexibility, enforces a basic document structure and the rendered documents can be exported to other formats (e.g. for printing). Also, the source can be read by humans without knowledge of the language in case the rendered document is unavailable.
  - We suggest to use either
    [reStructuredText (RST)](https://docutils.sourceforge.net/rst.html) or
    [Markdown](https://daringfireball.net/projects/markdown/) markup.
  - GitHub and GitLab automatically render `README.md` or `README.rst` files.


  **Copy-paste-able**

  - PDF alone is not enough since **copy-pasting out of a PDF document can be difficult**.
  - It is OK to provide a generated PDF in addition to a copy-paste-able format.


  **Written by humans**

  - Automatically generated documentation (e.g. API documentation) is useful as
    complementary documentation but it does not replace tutorials written by
    humans.


  **Installation instructions**

  - Give **step by step instructions for the basic case**.
    Additional information and caveats can be linked from there.
  - List requirements and dependencies (libraries, compilers, environment).
  - Include instructions for how to test for correctness after installation.


  **Make the license explicit**

  - **Include a LICENSE file** with your source code.
  - Without a license, your work is under exclusive copyright by default:
    others are not allowed to re-use or modify anything.
  - GitHub and GitLab allows to choose a license from common license templates.


  **Information for contributors**

  - Make it easy for others to contribute: **document how you prefer others to contribute**.
  - Users of your code may be shy to contribute code.
    Your **documentation provides a platform for your first contributions**.
````


```{admonition} Documentation checklist

  Which items to include depends on the number of users apart from yourself.

  - Purpose
  - Authors
  - License
  - Recommended citation
  - Copy-paste-able example to get started
  - Dependencies and their versions or version ranges
  - Installation instructions
  - Tutorials covering key functionality
  - Reference documentation (e.g. API) covering all functionality
  - How do you want to be asked questions (mailing list or forum or chat or issue tracker)
  - Possibly a FAQ section
  - Contribution guide
```


```{keypoints}
- Documentation is part of the code and should be versionable.
- Documentation (sources) should be tracked with the corresponding code in the same repository.
- Use standard markup languages such as reStructuredText or Markdown.
```
