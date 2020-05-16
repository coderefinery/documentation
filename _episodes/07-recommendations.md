---
layout: episode
title: "Recommendations"
teaching: 5
exercises: 0
questions:
  - What recommendations can we take home?
objectives:
  - Automatize and give the boring work to machines.
  - Make contributing documentation easy, simple, and direct.
  - Sometimes take a step back and consider different perspectives to your documentation.
  - Do not maintain own servers, use good available services.
---

## Setup

- Rather use Read the Docs if your documentation is associated to a source code and vary from one version to another. If you develop general documentation that is version independent then deploying a project website or homepage to GitHub Pages can be preferred.
- Whatever solution you choose, make it automatically rebuild pages upon `git push`.
- Documentation needs to be close to the source code and evolve with the source code.
- When using code review make sure that new functionality always comes with documentation.


### Sphinx or GitHub pages or both?

- GitHub pages typically serves one version (one branch). It is often used as the project/group/personal page.
- Sphinx can serve several versions (several branches/tags) at the same time.
- Some projects use both.
- It is a good idea to keep source code, web sources, and possibly also Sphinx source all in the same repository, tracking a common history.

---

## Human aspects

- Write documentation that you would like to read.
- Answer questions about your code with an updated documentation.
- Do not force persons who install and test your software to read
  tens of pages of documentation and understand the domain theory behind the code
  in order to install and test the code:
    - User support at computing centers
    - Vendors who run benchmarks
