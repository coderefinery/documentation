---
layout: episode
title: Hosting websites/homepages on GitHub Pages
teaching: 0
exercises: 20
questions:
  - How to serve a website/homepage using GitHub
---

## Hosting websites/homepages on GitHub Pages

You can host your personal homepage or group webpage
or project website on GitHub using
[GitHub Pages](https://pages.github.com/).

[GitLab](https://about.gitlab.com/features/pages/) and
[Bitbucket](https://confluence.atlassian.com/bitbucket/publishing-a-website-on-bitbucket-cloud-221449776.html)
also offer a very similar solution.

Unless you need user authentication or a sophisticated database behind your website,
[GitHub Pages](https://pages.github.com/) can be a very nice alternative
to running your own web servers.

This is how all
[https://coderefinery.org](https://coderefinery.org)
material is hosted.

---

<img src="{{ site.baseurl }}/img/gh-pages.jpg" width="50%">

---

> ## Exercise
>
> - Deploy own website reusing a template
> - Make a change to the website after it has been deployed for the first time
> - Verify that the change shows up on the website a minute or two later
>
> The documentation for GitHub Pages is very good so no need for us to duplicate
> screenshots: [https://pages.github.com/](https://pages.github.com/)
{: .challenge}

> ## Discussion
>
> - You can use HTML directly or another static site generator if you prefer
>   to not use the default [Jekyll](https://jekyllrb.com/).
> - It is no problem to use a custom domain instead of `*.github.io`.
{: .discussion}
