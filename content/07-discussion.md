# Discussion after the exercises

```{questions}
- What recommendations can we take home?
```

## Back in the main room: Questions and answers, discussion

> ## Discussion
>
> - Please write your questions in the collaborative notes document.
> - Any other ideas?
>     - e.g. Any incremental improvements that can benefit your projects?
>     - e.g. What's nice but overkill for your work?
>     - Some of the recommendations below can be used as food for thought.
{: .discussion}

---

### There is not the one right way: it is always a balance


**Jupyter notebooks can be good documentation for scripts**

- For simple scripts and post-processing, Jupyter notebooks can form a nice
  self-documenting pipeline.


**README.md or README.rst?**

- Functionality-wise both Markdown and RST are very similar.
- With RST it is a one-liner to generate a table of contents automatically.
- If you need math equations, RST/Sphinx might be a good fit.
- Resizing images in README.rst on GitHub is currently not easy.


**READMEs or Read the Docs?**

- For smaller projects READMEs can be absolutely enough.
- If the code is closed-source, you probably prefer Read the Docs (or similar).


**How to make sure that code changes come together with documentation changes?**

- Make documentation part of your code review.


**Sphinx/RTD or GitHub pages or both?**

- GitHub pages typically serves one version (one branch). It is often used as the project/group/personal page.
- RTD can serve several versions (several branches/tags) at the same time.
- Some projects use both.
