---
layout: default
permalink: /guide/
---

# Instructor guide

## Why we teach this lesson

Everyone should document their code, even if they’re working alone.

These two are the most important points:
- Code documentation has to be versionnable and branchable
- Code documentation should be tracked together with the source code

**Please do not skim over the two above points**. Please take few minutes to
explain why documentation (sources) should be tracked together with the source
code.  Please discuss this aspect with workshop participants and connect it to
**reproducibility**. This is for me (Radovan) the most important take-home
message.

Specific motivations:

- Code documentation becomes quickly unmanageable if not part of the source code.
- It helps people to quickly use your code thus reducing the time spent to explain over and again to new users.
- It helps people to collaborate.
- It improves the design of your code.


### Intended learning outcomes

By the end of this lesson, learners should:
- Understand the importance of writing code documentation together with the source code
- Know what makes a good documentation
- Learn what tools can be used for writing documentation
- Be able to motivate a balanced decision: sometimes READMEs are absolutely enough

---

## How to teach this lesson


### Requirements

These are the software/packages used in the lesson material and exercises:
- python
- Sphinx

Attendees would need a Github account too.


### Typical pitfalls

#### Anaconda shell, Git, and Nano on Windows

Windows users (probably) need to use the Anaconda prompt to run sphinx commands
(sphinx-build, sphinx-quickstart).

Git can be also be installed in the standard anaconda installation:

```bash
conda install git
```

The command above needs to be done into an Anaconda prompt or using Anaconda Navigator.

For editing files, learners should be encouraged to use their favorite editor.

Nano cannot be installed through Anaconda but is available by default in git-bash. So a good working solution seems to be that Windows users have two terminals side-by-side, one with Anaconda prompt and another with git-bash.


#### Character encoding issues

Can arise when using non-utf8 characters in conf.py. Diagnose this with ``file -i conf.py``
and ``locale``.


### How to start

With questions about documentation habits and experience with documentation
of own code and code written by others.


### Questions to involve participants

- How do you document unpublished features?


### Share your experience

The three first episodes do not contain any live coding or exercises.

In these first episodes, instructors share their own experience in writing
documentation. Feel free to add your own experience and ask learners to share
their thoughts too.  Stress the importance of understanding the audience you
are writing the documentation for (developers, users, etc.) and that starting
with a simple tutorial (with a set of tests) is usually a good approach.

In the second episode, we review different tools: the goal here is to highlight
what is important when choosing a tool for writing documentation. We have
chosen to teach how to use Sphinx with Read the Docs but make sure you bring
across that the tools we show are general:
- Sphinx is not only for Python
- Read the Docs is not only for Github

In the fourth exercise, we first test the availability of Sphinx. This test
needs to be done in a terminal where python is available. It can take a bit of
time to get everybody on board with Sphinx.  It can be nice to make a short
break if you need more time to fix problems.


### Things to prepare

We start from scratch for all the exercises in this lesson.


### Optional sections

The lesson does not fit into 1.5 hours if you go through everything. Optimize for
discussions and prepare well to be able to jump over bullet points which
can be left for a later lecture. Some sections can be skipped if needed (see below). However, we recommend to have a
discussion with your learners to make them aware of what the training material contains.

- Do not insist on practicing Markdown or RST syntax
- The section *Rendering (LaTeX) math equations* may be optional if your
  attendees do not have to deal with equations.
- In episode 6 *Deploying a project website or homepage to GitHub Pages*, the
  goal is not anymore to write code documentation but to show how to build
  project website with Github.  If time is tight, the GitHub pages episode can be
  skipped or can be done as demonstration instead of exercise.  However, make
  sure you mention that it exists and explain that it is not generally used to
  write code documentation but to complement it with information on overall
  project.


### Live better than reading the website material

It is better to  demonstrate the commands live and type-along. Ideally connecting
to examples discussed earlier.


### Place this lesson on last day of the workshop

Reason is that with collaborative Git we can create more interesting
documentation exercises. Currently there are some elements of forking and
pushing and this is only really introduced on day two.

We have tried this lesson on day one and it felt too early and disconnected/abrupt.

It works best after the reproducibility lesson since we then reuse the example
and it feels familiar.


### What worked well in past workshops

It is good if participants see how they can `sphinx-quickstart` a project from
zero.

Then they learn how to deploy an existing project to RTD.


### Timing

As an instructor you should prepare all bullet points in the requirements and
tools section but do not go through each bullet point in detail. Only highlight
the main points and rather give time for a discussion. Leave details for a later
lecture for those who want to find out more. If you go through each bullet point
in detail, the motivation can easily take up 30 minutes and you will run out
of time.
