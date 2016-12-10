---
layout: episode
title: "Deploying a project website to GitHub Pages"
teaching: 0
exercises: 15
questions:
  - "How can we have a good-looking project website without hosting it ourselves?"
objectives:
  - "Create a working example which you can take home and adapt for your project."
keypoints:
  - "Do not maintain own web servers for project websites."
---

## Create an example project website and host it on GitHub Pages

In this demo we will create a very simple project website and host it on GitHub
Pages. This exercise is transferable to GitLab or Bitbucket pages which offer a
very similar solution. The key is that you can give the hosting to
professionals so that you can focus on your project.

Every project `<projectname>` on GitHub under the user/namespace `<user>` which
contains a branch `gh-pages` is served on
`https://<user>.github.io/<projectname>`.

First fork and clone the [example
repository](https://github.com/coderefinery/gh-pages-example).  Check that you
are indeed on the `gh-pages` branch.  Make some changes to `index.html`,
commit, and push and verify that your changes land on
`https://<user>.github.io/gh-pages-example/`.

Now you have successfully deployed a website!

It is a good idea to keep source code, web sources, and possibly also Sphinx
source all in the same repository, tracking a common history.

GitHub pages can be configured to also serve directly from the master branch
under `docs/`.

Many people put their personal home page on `<user>.github.io`, which is served
on `https://<user>.github.io'.

---

## Where you might want to go from here

- Plain HTML often leads to code repetition and does not allow modular development of website with control flows.
- There are many web frameworks available.
- Static site generators allow modular websites and play well with GitHub/GitLab/Bitbucket Pages:
  - [Jekyll](https://jekyllrb.com)
  - [Hugo](https://gohugo.io)
  - [Hexo](https://hexo.io)
  - Many others
- See https://pages.github.com for step-by-step guides.
- It is no problem to serve GitHub/GitLab/Bitbucket Pages using your own domain name.
- Use CSS frameworks:
    - [Bootstrap](http://getbootstrap.com)
    - [Foundation](http://foundation.zurb.com)
