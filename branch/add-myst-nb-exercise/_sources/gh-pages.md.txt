(gh-pages)=

# Hosting websites/homepages on GitHub Pages


## Often we don't need more than a static website

You can host your personal homepage or group webpage or project website on
GitHub using [GitHub Pages](https://pages.github.com/).
[GitLab](https://about.gitlab.com/features/pages/) and
[Bitbucket](https://confluence.atlassian.com/bitbucket/publishing-a-website-on-bitbucket-cloud-221449776.html)
also offer a very similar solution.

Unless you need user authentication or a sophisticated database behind your
website, [GitHub Pages](https://pages.github.com/) can be a very nice
alternative to running your own web servers.  This is how all
[https://coderefinery.org](https://coderefinery.org) material is hosted.


## How to find the website URL

Here below, NAMESPACE can either be a username or an organizational account.

**Personal homepage or organizational homepage**
- Generated URL: https://**NAMESPACE**.github.io
- Generated from: https://github.com/**NAMESPACE**/**NAMESPACE**.github.io (main branch)

**Project website**
- Generated URL: https://**NAMESPACE**.github.io/**REPOSITORY**
- Generated from: https://github.com/**NAMESPACE**/**REPOSITORY** (gh-pages branch)


## Exercise - Your own website on GitHub Pages

```{exercise} GH-Pages-2: Host your own github page
- Deploy own website reusing a template:
  - Follow the steps from GitHub Pages <https://pages.github.com/>.
    The documentation there is very good so there is no need for us to duplicate the screenshots.
  - Select "Project site".
  - Select "Choose a theme".
  - Follow the instructions on <https://pages.github.com/>.
  - Browse your page on https://**USERNAME**.github.io/**REPOSITORY** (adjust "USERNAME" and "REPOSITORY").
- Make a change to the repository after the webpage has been deployed for the first time.
- Please wait few minutes and then verify that the change shows up on the website.
```

```{callout} Real-life examples
- CodeRefinery website (built using [Zola](https://www.getzola.org/))
  - [Source](https://raw.githubusercontent.com/coderefinery/coderefinery.org/main/content/lessons/core.md)
  - Result: <https://coderefinery.org/lessons/core/>
- This lesson (built using [Sphinx](https://www.sphinx-doc.org/)
    and [MyST](https://myst-parser.readthedocs.io/)
    and [sphinx-lesson](https://coderefinery.github.io/sphinx-lesson/))
  - [Source](https://raw.githubusercontent.com/coderefinery/documentation/main/content/gh-pages.md)
  - Result: this page
```

```{note}
- You can use HTML directly or another static site generator if you prefer
  to not use the default [Jekyll](https://jekyllrb.com/).
- It is no problem to use a custom domain instead of `*.github.io`.
```
