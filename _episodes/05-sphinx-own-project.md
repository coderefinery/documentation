---
layout: episode
title: "Adding Sphinx to your own project"
teaching: 5
exercises: 20
objectives:
  - Hook up your own project with Sphinx.
---

## Optional exercise: add Sphinx to your own project

### Possible route 1: Adapt a working example

For this you can get inspired by our example from the previous exercise:
https://github.com/coderefinery/word-count

You can copy the `doc` directory to your project, adjust `conf.py` (rename project name),
edit `*.rst` files, and iteratively build up your documentation.

You can then build the documentation locally using:

```shell
$ sphinx-build doc _build
```


### Possible route 2: Bootstrap a new Sphinx project

Run `sphinx-quickstart` inside the directory of your project:

```shell
$ cd your-own-project
$ sphinx-quickstart
```

The quickstart utility will ask you some questions. You can give default answers
to all questions. You can always edit the answers later by editing the generated
`conf.py` file.

After running `sphinx-quickstart`, edit the generated `index.rst` to reference additional
files in the table of contents tree. Get inspired by https://github.com/coderefinery/word-count.
