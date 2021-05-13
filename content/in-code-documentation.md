(in-code-documentation)=

# In-code documentation

```{questions}
- What can I do to make my code more easily understandable?
- What information should go into comments?
- What are docstrings and what information should go into docstrings?
```

```{objectives}
- Write docstrings according to best practices
- Know where and when to put comments
```

In this episode we will learn how to write good documentation inside your code.


## Writing good comments

````{challenge} Exercise: Comments
Let's take a look at two example comments (comments in python start with `#`):

**Comment A**
```python
# Now we check if temperature is larger then -50:
if temperature > -50:
    print('do something')
```

**Comment B**
```python
# We regard temperatures below -50 degrees as measurement errors
if temperature > -50:
    print('do something')
```
Which of these comments is best? Can you explain why?
````
```{solution} Solution
Comment A describes **what** happens in this piece of code,
whereas comment B describes **why** this piece of code is there, i.e. its **purpose**.
Comments in the form of B are much more useful, comments of form A are redundant and we should avoid them.
```

````{callout}
Do not use comments for:

**Keeping zombie code**
```python
# Do not run this code!:
# if temperature > 0:
#     print('It is warm')
```
Instead: just remove the code, you can always find it back in a previous version of your code in git.

**Replacing git**
```python
# removed on August 5
# if() ...
# Now it connects to the API with o-auth2, updated 05/05/2016
```
Instead: use git to keep track of different versions of your code.
````

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
        The mean air temperature (float)
    """
    temperatures = data['Air temperature (degC)']
    return float(sum(temperatures)/len(temperatures))
```
A docstring is a structured comment associated to a segment of code (i.e. function or class)

Good docstrings describe:
* What the function does
* What goes in (including the type of the input variables)
* What goes out (including the return type)

In python there are several styles that describe how docstrings should be formatted.
Here we use [Google style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

Python parses docstrings, for example calling the `help` function will display it:
```python
help(mean_temperature)
```
Python will print this help text:
```
Help on function mean_temperature in module __main__:

mean_temperature(data)
    Get the mean temperature

    Args:
        data (pandas.DataFrame): A pandas dataframe with air temperature measurements.

    Returns:
        The mean air temperature (float)
```

It is common to write docstrings for functions, classes, and modules.


````{callout} Script docstrings
You can also add a **structured** docstring at the top of a script to document what the script does and how to run it.
```python
"""Prints information about the mean air temperature.

Usage:
 ./temperature.py

Author:
 Sven van der Burg - 2021-03-2021
"""
```
````

````{callout} Small effort, large gain.
Writing docstrings makes you generate your documentation as you are generating the code!
````

````{challenge} Exercise: Adding in-code documentation
Update this code snippet so it is well-documented:
```python
import pandas as pd

def x(a, print_columns=False):
   b = pd.read_excel(a)
   column_headers = list(b.columns.values)
   if print_columns:
       print("\n".join(column_headers))
   return column_headers
```
````

````{solution}
```python
import pandas as pd

def get_spreadsheet_columns(file_loc, print_columns=False):
   """Gets and prints the spreadsheet's header columns
   Args:
       file_loc (str): The file location of the spreadsheet
       print_columns (bool, optional) : A flag used to print the columns to the console (default is False)
   Returns:
       a list of strings used that are the header columns
   """
   file_data = pd.read_excel(file_loc)
   column_headers = list(file_data.columns.values)
   if print_columns:
       print("\n".join(column_headers))
   return column_headers
```
````

````{callout} Naming **is** documentation.
Giving explicit, descriptive names to your code segments (functions, classes, variables) already provides very useful
and important documentation. In practice you will find that for simple functions it is unnecessary to add a docstring
when the function name and variable names already give enough information.
````

````{keypoints}
- Comments should describe the why for your code not the what.
- Writing docstrings is an easy way to write documentation while you type code.
````
