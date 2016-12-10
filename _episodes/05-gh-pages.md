---
layout: episode
title: "Deploying a project website to GitHub pages"
teaching: 0
exercises: 15
questions:
  - "How can we have a good-looking project website without hosting it ourselves?"
objectives:
  - "Create a working example which you can take home and adapt for your project."
---

## Technology

- Do not write own CSS
    - Bootstrap http://getbootstrap.com
    - Jekyll http://jekyllrb.com

- Do not maintain own web servers
    - GitHub pages https://pages.github.com for project websites
    - Bitbucket pages http://pages.bitbucket.org

---

## Typical GitHub pages workflow

- Create `gh-pages` branch for your project which holds website sources
- Every push automatically rebuilds http://myorg.github.io/myproject/ [site does not exist]
- It is good practice to use Bootstrap for CSS
- GitHub provides an automatic page generator: you can create a shiny project website in 5 minutes
- See also https://pages.github.com for step-by-step guides

---

## Part 2: Create an example project website and host it on GitHub Pages

Create an example project website (from GitHub Pages templates or on your own)
and host it on GitHub Pages (https://pages.github.com). If you use Doxygen, try
to host Doxygen-generated documentation on GitHub Pages.

---

## Where you might want to go from here

- Write me
It is no problem to serve using your own URL
