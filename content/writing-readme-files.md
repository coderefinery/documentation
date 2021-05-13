(writing-readme-files)=

# Writing good README files

```{questions}
- What should be included as a bare minimum in README files?
```

```{objectives}
- Write a README file according to good practices.
```

---

The `README` file (often `README.md` or `README.rst`) is usually the first
thing users/collaborators see when visiting your GitHub repository.  Use it to
communicate important information about your project!


## Exercises

```{instructor-note}
- Groups can choose to work on either exercise README-1, or on exercises README-2 + README-3.
- Exercise README-1 creates and discusses a README for an example Python project.
- Exercise README-2 can be interesting if learners already have a project/code of their own.
- Exercise README-3 (constructively) discusses READMEs of projects which you have recently used.
```

````{challenge} Exercise README-1: Write a README file for an example Python project
**The example project**

Here's [the example project](https://github.com/escience-academy/coderefinery-documentation-example-project).
For this project we transformed the code snippets from the previous episode into a single script [analyse_spreadsheet.py](https://github.com/escience-academy/coderefinery-documentation-example-project/blob/main/analyse_spreadsheet.py)

Let's take a look at [the script](https://github.com/escience-academy/coderefinery-documentation-example-project/blob/main/analyse_spreadsheet.py).
You don't need to understand the script completely, all you need to know is:
* The functions `mean_temperature` and `get_spreadsheet_columns` from previous episode are in there.
* We added a `main` function that is called when you run the script
(you could run this python script by calling `python analyse_spreadsheet.py` on the command line).
It will prompt the user for a file name, print the columns in the spreadsheet, and print the mean
temperature.

That's all there is to this project! (You can ignore the other files in the repository, we'll get back to them in episode 4)

**The exercise**

1. Fork the [the example project](https://github.com/escience-academy/coderefinery-documentation-example-project) to your own github namespace
2. Add a file called `README.md` (you can use the github web interface or work locally (i.e. `git clone`, edit the file,  `git add`, `git commit`, `git push`))
3. Add some content to your README file. Think about what you want the audience to know about your project!
   It does not matter whether the information is correct, it is more important that you have all the components that make up a good README file.
4. Note that the README file is nicely rendered on the github repository page.
5. Compare your README file with that of others, is all the essential information in there?
NB: The `README.md` file is written in 'Markdown' a very popular lightweight markup language, all you need to know for now is this syntax:

```
# A section title
## A subsection title
Normal text

A list with items
- item1
- item2
```

(Optional): Use [https://hemingwayapp.com/](https://hemingwayapp.com/) to analyse your README file and make your writing bold and clear!
````

`````{solution}
A README file for this project could look like this:

````
### Temperature analysis in spreadsheets

A python script for the analysis of temperatures in excel files.


### Why should I use this project ?

It makes it easy to analyse excel files with temperatures in them.


### Setup

You need `python>3.5` to run this script.

The project depends on the `pandas` library, install it with pip:
`pip install pandas`


### How to run?

You can run the script from the command-line using
```
python analyse_spreadsheet.py
```

You can use functions directly, for example: calculate the mean temperature of some data:
```python
from analyse_spreadsheet import mean_temperature

print(mean_temperature(data))
```


### How to cite this project?

Please email `training@esciencecenter.nl` to get instructions on how to properly cite this project.


### Contributing

You are welcome to contribute to the code via pull requests.  Please have a
look at the [NLeSC
guide](https://nlesc.gitbooks.io/guide/content/software/software_overview.html)
for guidelines about software development.
````
`````

```{challenge} Exercise README-2: Draft or review a README for one of your recent projects
Try to draft a brief README or review a README which you have written for one
of your projects.

You can do that either by screensharing and discussing or working individually.

Please note observations and recommendations in the collaborative notes.
```

```{challenge} Exercise README-3: Review and discuss a README of a project that you have used
In this exercise we will review and discuss a README of a project which you
have used. You can also review a library which is popular in your domain of
research and discuss their README.

You can do that either by screensharing and discussing or working individually.

When discussing other people's projects please remember to be respectful and
constructive. The goal of this exercise is not to criticize other projects but
to learn from other projects and to collect the aspects that you enjoyed
finding in a README and to also collect aspects which you have searched for but
which are sometimes missing.

Please note observations and recommendations in the collaborative notes.
```

---

## Table of contents in README files

- With RST you can generate a table of contents (TOC) automatically by adding `.. contents:: Table of Contents`.
- On GitLab you can generate a TOC in Markdown with `[[_TOC_]]`.
- GitHub generates a [TOC for README.md](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes#auto-generated-table-of-contents-for-readme-files).

---

## What makes up a good README file?

```{keypoints}
As a bare minimum a README file should include:
- A descriptive project title
- Motivation (why the project exists)
- How to setup
- Copy-pastable quick start code example
- Recommended citation
```

```{callout} User experience
Think about the user (**which can be a future you**) of your project, what does this user need to know to use or
contribute to the project? And how do you make your project attractive to use or contribute to?
```
