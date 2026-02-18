(writing-readme-files)=

# Writing good README files

The README file (often `README.md` or `README.rst`) is usually the first thing
users/collaborators see when visiting your GitHub repository.

Use it to communicate important information about your project!  For many
smaller or mid-size projects, this is enough documentation.  It's not that hard
to make a basic one, and it's easy to expand as needed.


## Exercise: Have fun testing some README features

````{exercise} Exercise README-1: Have fun testing some README features you may not have heard about

- Test the effect of adding the following to your GitHub README ([read
  more](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts)):
  ```markdown
  > [!NOTE]
  > Highlights information that users should take into account, even when skimming.

  > [!IMPORTANT]
  > Crucial information necessary for users to succeed.

  > [!WARNING]
  > Critical content demanding immediate user attention due to potential risks.
  ```

- For more detailed descriptions which you don't want to show by default you
  might find this useful (please try it out):
  ```markdown
  <details>
  <summary>
  Short summary
  </summary>

  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
  quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
  consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
  cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
  proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
  </details>
  ```

- Would you like to add a badge like this one: [![please replace with alt text](https://img.shields.io/badge/anytext-youlike-blue)](https://example.org)?

  Badge that links to a website (see also <https://shields.io/>):
  ```markdown
  [![please replace with alt text](https://img.shields.io/badge/anytext-youlike-blue)](https://example.org)
  ```
  Badge without link:
  ```markdown
  ![please replace with alt text](https://img.shields.io/badge/anytext-youlike-blue)
  ```

- Know about other tips and tricks? Please share them (send a pull request to this lesson).
````


## Exercise: Improve the README for your own project

```{exercise} Exercise README-2: Draft or improve a README for one of your recent projects
Try to draft a brief README or review a README which you have written for one
of your projects.

- You can do that either by screensharing and discussing or working individually.

- Use the {ref}`checklist <checklist>` which we have discussed earlier.

- Think about the user (**which can be a future you**) of your project, what does this user need to know to use or
  contribute to the project? And how do you make your project attractive to use or contribute to?

- (Optional): Try the [https://hemingwayapp.com/](https://hemingwayapp.com/) to analyse your README file and make your writing bold and clear.

- Please note observations and recommendations in the collaborative notes.
```

---

## Exercise: Discuss the README of a project that you use

```{exercise} Exercise README-3: Review and discuss a README of a project that you have used
In this exercise we will review and discuss a README of a project which you
have used. You can also review a library which is popular in your domain of
research and discuss their README.

- You can do that either by screensharing and discussing or working individually.

- When discussing other people's projects please remember to be respectful and
  constructive. The goal of this exercise is not to criticize other projects but
  to learn from other projects and to collect the aspects that you enjoyed
  finding in a README and to also collect aspects which you have searched for but
  which are sometimes missing.

- Please note observations and recommendations in the collaborative notes.
```

---

## Table of contents in README files

- GitHub automatically generates a [table of contents for README.md files](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes#auto-generated-table-of-contents-for-readme-files).
- On GitLab you can generate a TOC in Markdown with:
  ```markdown
  [[_TOC_]]
  ```
- With RST you can generate a table of contents (TOC) automatically by adding:
  ```rst
  .. contents:: Table of Contents
  ```
