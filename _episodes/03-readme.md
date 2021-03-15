---
layout: episode
title: "Writing good README files"
teaching: 10
exercises: 20
questions:
  - What should be included as a bare minimum in Readme files?
objectives:
  - Write a Readme file according to best practices.
keypoints:
---
> ## Exercise: Write a README file
> ### Analyse spreadsheet example project
> We are going to write a README file for [this example project](https://github.com/escience-academy/coderefinery-documentation-example-project)
> For this project we transformed the code snippets from the previous episode into a single script [analyse_spreadsheet.py](https://github.com/escience-academy/coderefinery-documentation-example-project/blob/main/analyse_spreadsheet.py).
> 
> You don't need to understand the script completely, all you need to know is:
> * The functions `mean_temperature` and `get_spreadsheet_columns` are in there.
> * We added a `main` function that is called when you run the script 
> (you could run this python script by calling `python analyse_spreadsheet.py`). 
> It will prompt the user for a file name, print the columns in the spreadsheet, and print the mean
> temperature.
> 
> That's all there is to this project!
>
> ### The exercise
> 1. Fork the [the example project](https://github.com/escience-academy/coderefinery-documentation-example-project) to your own github namespace
> 2. Add a file called `README.md` (you can use the github web interface or work locally (i.e. `git clone`, edit the file,  `git add`, `git commit`, `git push`))
> 3. Add some content to your README file. Think about what you want the audience to know about your project! 
>    You don't need to write whole stories, it is more important that you have all the components that make up a good README file.
> 4. Compare your README file with that of others, what did you miss?
> NB: The `README.md` file is written in 'Markdown' a very popular lightweight markup language, all you need to know for now is this syntax:
> ```markdown
> # A section title
> ## A subsection title
> Normal text
> 
> A list with items
> - item1
> - item2
> ```
> 
> (Optional): Use https://hemingwayapp.com/ to analyse your README file and make your writing bold and clear!
> > ## Solution
> > 
> > ### Temperature analysis in spreadsheets
> > A python script for the analysis of temperature in excel files.
> > 
> > ### Why should I use this script ?
> > It makes it easy to analyse excel files with temperatures in them.
> > 
> > ### Setup
> > You need `python>3.5` to run this script.
> > 
> > The project depends on the `pandas` library, install it with pip:
> > `pip install pandas`
> > 
> > ### How to run?
> > You can run the script from the command-line using
> > ```
> > python analyse_spreadsheet.py
> > ```
> > 
> > You can calculate the mean temperature of some data:
> > ```python
> > from analyse_spreadsheet import mean_temperature
> > 
> > print(mean_temperature(data))
> > ```
> > 
> > ### How to cite this project?
> > Please email `training@esciencecenter.nl` to get instructions on how to properly cite this project.
> > 
> > ### Contributing
> > You are welcome to contribute to the code via pull requests.
> > Please have a look at the [NLeSC guide](https://nlesc.gitbooks.io/guide/content/software/software_overview.html) for guidelines about software development.
> > 
{: .challenge}
