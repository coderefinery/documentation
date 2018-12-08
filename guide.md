---
layout: default
permalink: /guide/
---

# Instructor guide


### What you need to do before the workshop

We use this repository for a collaborative exercise:
https://github.com/coderefinery/word-count

Before the workshop you should squash all submitted changes
by the participants of the last workshop and place the squashed
commit on a branch, e.g.: https://github.com/coderefinery/word-count/commit/1f772a4f01cfcb9bd8bd1da505e6a7c47bcf091c

For the branch name use the same URL suffix as for the workshop, e.g.
for workshop
https://coderefinery.org/workshops/2018-12-03-uppsala/
create the branch name
`doc-exercise/2018-12-03-uppsala`

Then rewind the master branch to the last commit before participants
sent in changes.

Close all PRs which are open from the last workshop.


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

Finally we all collaborate on a central example via PRs and this can be fun to
receive documentation changes from participants.


### How to start

With questions about documentation habits and experience with documentation
of own code and code written by others.


### Questions to involve participants

- How do you document unpublished features?


### Timing

As an instructors you should prepare all bullet points in the requirements and
tools section but do not go through each bullet point in detail. Only highlight
the main points and rather give time for a discussion. Leave details for a later
lecture for those who want to find out more. If you go through each bullet point
in detail, the motivation can easily take up 30 minutes and you will run out
of time.


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
