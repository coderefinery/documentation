# Summary

```{questions}
- What recommendations can we take home?
```

---

## There is not the one right way: it is always a balance


**Jupyter notebooks can be good documentation for scripts**

- For simple scripts and post-processing, Jupyter notebooks can form a nice
  self-documenting pipeline.
- They can be a nice way to accompany a paper that analyzed some data.


**READMEs or Sphinx?**

- For smaller projects READMEs can be absolutely enough.
- If the code is closed-source (and hence nobody can see the README), you
  probably prefer Sphinx (or similar).
- If you need math equations, Sphinx might be a good fit.


**How to make sure that code changes come together with documentation changes?**

- Make documentation part of your code review.


**Read the Docs or GitHub pages or both?**

- GitHub pages typically serves one version (one branch). However, it is possible to build
  several or all branches as part of a workflow.
- Read the Docs can serve several versions (several branches/tags) at the same time.
- Some projects use both.


**Consider making your development tutorial-driven**

- Writing documentation is as important as writing software.
- Focus on how you use the software.
- If there is no tutorial on it, the feature "doesn't exist".
- Don't keep tutorial in sync with code, keep code in sync with tutorial - change the tutorial first.
- Read more in this [fantastic slide-deck](https://virtual.oxfordabstracts.com/#/event/public/3101/submission/11) about tutorial-driven development.
