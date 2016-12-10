---
layout: episode
title: "Recommendations"
teaching: 5
exercises: 0
questions:
  - "What recommendations can we take home?"
objectives:
  - "Automatize and give the boring work to machines."
  - "Make contribution documentation easy, simple, and direct."
  - "Sometimes take a step back and consider different perspectives to your documentation."
  - "Do not maintain own servers, use good available services."
---

## Technical aspects

- Whatever solution you choose, make it automatically rebuild pages upon `git push`
- If you need to ask somebody to run some scripts on the server after you have modified sources,
  that will not work in practice (does not scale)
- When using code review make sure that new functionality always comes with documentation

---

## Human aspects

- Write documentation that you would like to read
- Answer questions about your code with an URL to (updated) documentation
    - Email answers get lost/forgotten
    - Answer and improve doc at the same time
    - Lazy in the long-term
    - Chance is that next time the user/colleague
      will find the answer by him/herself
    - Trains people to read the documentation before writing emails

---

## Documentation checklist

- Purpose
- Authors
- License
- Recommended citation
- Usage
- Example
- Installation instructions
- Requirements and dependencies (libraries, compilers, environment)
- Contact points (mailing list or forum or chat or issue tracker)
- Contribution guide

---

## Aspects we often forget in our busy lives

- Some people who install and test the software know nothing about the theory behind the code - do not force them to understand the theory in order to install and test the code
    - Busy user support at computing centers
    - Vendors who run benchmarks
- Be proud of your good work and market success stories
    - Important for grant applications
    - Show pictures
    - Demonstrate the efficiency or functionality or good scaling (if relevant)
