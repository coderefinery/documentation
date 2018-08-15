---
layout: default
permalink: /guide/
---

# Instructor guide

### How to start

With questions about documentation habits and experience with documentation
of own code and code written by others.


### Questions to involve participants

- How do you document unpublished features?


### Timing

As an instructors you should prepare all bullet points in the requirements and
tools section but do not go through each bullet point in detail. Only highlight
the main points and rather give time for a discussion.


### Core aspects

- Documentation has to be versionnable and branchable
- Documentation should be tracked together with the source code
- Sphinx is not only for Python
- Read the Docs is not only for Github


### Sessions which can be skipped if time is tight

- Do not insist on practicing Markdown or RST syntax


### Typical pitfalls

#### Anaconda shell, Git, and Nano on Windows

Windows users (probably) need to use the Anaconda prompt to run sphinx commands
(sphinx-build, sphinx-quickstart). Git seems to be present in the standard
anaconda installation, but not nano.

A good working solution seems to be that Windows users have two terminals
side-by-side, one with Anaconda prompt and another with git-bash.


#### Character encoding issues

Can arise when using non-utf8 characters in conf.py. Diagonse this with ``file -i conf.py``
and ``locale``.
