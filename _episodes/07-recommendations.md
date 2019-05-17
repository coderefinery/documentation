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

- Rather use Read the Docs if your documentation is associated to a source code and vary from one version to another. If you develop general documentation that is version independent then deploying a project website or homepage to GitHub Pages can be prefered.
- Whatever solution you choose, make it automatically rebuild pages upon `git push`.
- Documentation needs to be close to the source code and evolve with the source code.
- When using code review make sure that new functionality always comes with documentation.

---

## Human aspects

- Write documentation that you would like to read.
- Answer questions about your code with an updated documentation.
- Do not force persons who install and test your software to read
  tens of pages of documentation and understand the domain theory behind the code
  in order to install and test the code:
    - User support at computing centers
    - Vendors who run benchmarks
