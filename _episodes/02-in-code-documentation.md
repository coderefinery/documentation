---
layout: episode
title: "In-code documentation"
teaching: 5
exercises: 15
questions:
    - What can I do to make my code more easily understandable?
    - What information should go into comments?
    - What information should go into docstrings?
objectives:
    - Write docstrings according to best practices
    - Know where and when to put comments
keypoints:
  - In-code documentation should describe the why for code.
---

## Writing docstrings in python
Let's look at the following function:
```python
def mean_temperature(data):
    temperatures = data['Air temperature (degC)']
    return sum(temperatures)/len(temperatures)
```
It computes the mean temperature for a given dataset.
How can we make it clearer what this function does and how to use it?

We can add a **docstring** (the string in between the two `"""`):
```python
def mean_temperature(data):
    """
    Get the mean temperature
    
    Args:
        data (pandas.DataFrame): A pandas dataframe with air temperature measurements.
    
    Returns:
        The mean air temperature
    """
    temperatures = data['Air temperature (degC)']
    return sum(temperatures)/len(temperatures)
```
A docstring is a structured comment associated to a segment of code (i.e. function or class)

The docstring describes:
* What the function does
* What goes in
* What goes out

In python there are several styles that describe how docstrings should be formatted.
Here we use [Google style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

Python parses docstrings, for example calling the `help` function will display it:
>```python
>help(mean_temperature)
>```
>>```
>>Help on function mean_temperature in module __main__:
>>mean_temperature(data)
>>    Get the mean temperature
>>    
>>    Args:
>>        data (pandas.DataFrame): A pandas dataframe with air temperature measurements.
>>    
>>    Returns:
>>        The mean air temperature
>>```

>
> ## Small effort, large gain.
> Writing docstrings makes you generate your documentation as you are generating the code!
{: .callout}

> ## Exercise 1: Adding in-code documentation
>
> Update this code snippet so it is well-documented:
>
> ```python
> import pandas as pd
> 
> def x(a, print_columns=False):
>    b = pd.read_excel(a)
>    column_headers = list(b.columns.values)
>    if print_columns:
>        print("\n".join(column_headers))
>    return column_headers
> ```
> > ## Solution
> > ~~~python
> > import pandas as pd
> > 
> > 
> > def get_spreadsheet_columns(file_loc, print_columns=False):
> >    """Gets and prints the spreadsheet's header columns
> >
> >    Args:
> >        file_loc (str): The file location of the spreadsheet
> >        print_columns (bool, optional) : A flag used to print the columns to the console (default is False)
> >
> >    Returns:
> >        a list of strings used that are the header columns
> >    """
> >
> >    file_data = pd.read_excel(file_loc)
> >    column_headers = list(file_data.columns.values)
> >
> >    if print_columns:
> >        print("\n".join(column_headers))
> >
> >    return column_headers
> > ~~~
> > {: .source}
> >
> {: .solution}
{: .challenge}


