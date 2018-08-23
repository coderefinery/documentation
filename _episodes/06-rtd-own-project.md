---
layout: episode
title: "How to hook up your own project with Read the Docs"
teaching: 5
exercises: 20
objectives:
  - Hook up your own project with Read the Docs.
---

## [Read the Docs](https://readthedocs.org)

- Free Sphinx hosting
- RST or Markdown
- PDF can be generated on the fly
- Equations and images no problem
- Layout can be styled
- Many projects use [Read the Docs](https://readthedocs.org) as their main site
- It is no problem to serve using your own URL `http://myproject.org` instead of `http://myproject.readthedocs.io`

---

## Optional exercise: deploy your own project to [Read the Docs](https://readthedocs.org)


### Step 1: make sure you can build the documentation locally with Sphinx

For this see the previous optional exercise.


### Step 2: Enable the project on [Read the Docs](https://readthedocs.org)

Now you will import a project to Read the Docs by connecting to GitHub (or some
other repository hosting).

This will automatically set up a webhook on GitHub and webhook integration on
Read the Docs so that `git push` will automatically rebuild the Read the Docs
site.

One can also manually import the project to Read the Docs and set up the
webhook on GitHub, along with webhook integration on Read the Docs, but this
will not be needed here.

- Log into [Read the Docs](https://readthedocs.org)
  and visit your [dashboard](https://readthedocs.org/dashboard/)
- Click "Import a Project"
- Select "Connect to GitHub", and choose the doc-example repository
- Click "Next"

That's it! Your site should now be live on
[http://your-project-name.readthedocs.io](http://your-project-name.readthedocs.io).

Finally, make some changes to your documentation, commit and push them, and
verify that the documentation website refreshes after your changes (can take a
minute).
