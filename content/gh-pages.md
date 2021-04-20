# Hosting websites/homepages on GitHub Pages

```{questions}
- How to serve a website/homepage using GitHub
```

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

```{figure} img/gh-pages.svg
:alt: Scheme that describes how branch names end up websites

Scheme that describes how branch names end up websites.
```

---

> ## Exercise
>
> - Deploy own website reusing a template:
>   - Follow the steps from GitHub Pages <https://pages.github.com/>. The documentation there is very good so there is no need for us to duplicate the screenshots
>   - Select "Project site"
>   - Select "Choose a theme" (for instance "Minimal")
>   - Click "Select theme"
>   - Adjust the README.md and commit
>   - Browse your page on `http://username.github.io/repository` (adjust "username" and "repository")
> - Make a change to the repository after the webpage has been deployed for the first time
> - Please wait few minutes and then verify that the change shows up on the website

{: .challenge}

> ## Real-life examples
>
> - Research Software Hour
>   - Source: <https://raw.githubusercontent.com/ResearchSoftwareHour/researchsoftwarehour.github.io/main/content/about.md>
>   - Result: <https://researchsoftwarehour.github.io/about/>
> - This lesson
>   - Source: <https://raw.githubusercontent.com/coderefinery/documentation/gh-pages/_episodes/06-gh-pages.md>
>   - Result: this page
{: .prereq}

> ## Discussion
>
> - You can use HTML directly or another static site generator if you prefer
>   to not use the default [Jekyll](https://jekyllrb.com/).
> - It is no problem to use a custom domain instead of `*.github.io`.
{: .discussion}
