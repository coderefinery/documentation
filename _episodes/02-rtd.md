---
layout: episode
title: "Deploying Sphinx documentation to Read the Docs"
teaching: 0
exercises: 15
questions:
  - "A question that this episode will answer?"
  - "Another question?"
objectives:
  - "This is one objective of this episode."
  - "This is another objective of this episode."
  - "Yet another objective."
  - "And not to forget this objective."
keypoints:
  - "This is an important key point."
  - "Another important key point."
  - "One more key point."
---

## Part 1: Sphinx-based documentation on Read the Docs

In this exercise we will implement a Sphinx-based documentation, host it on
GitHub and deploy it to https://readthedocs.org. This is exactly how this
page that you read right now arrives to your browser (the sources are here:
https://github.com/bast/software-development-toolbox).

- Set up a virtual environment according to http://docs.python-guide.org/en/latest/dev/virtualenvs/.
- Install Sphinx to the virtual environment.
- Run ``sphinx-quickstart`` (http://sphinx-doc.org/tutorial.html).
- Build the html and check it locally on your computer and in your browser.
- Make some changes to it and build them locally.
- Create a new GitHub project for it.
- Push the documentation sources to the new GitHub project.
- Create an account at https://readthedocs.org.
- Import the Github project you just created to Read the Docs.
- Create a post commit hook in GitHub so that changes automatically refresh the Read the Docs pages.
- Test the post commit hook by making and pushing changes to the documentation sources and verify
  that the documentation refreshes after your changes.
