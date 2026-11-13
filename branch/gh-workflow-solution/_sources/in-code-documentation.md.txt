(in-code-documentation)=

# In-code documentation

```{questions}
- What can I do to make my code more easily understandable?
- What information should go into comments?
- What are docstrings and what information should go into docstrings?
```

In this episode we will learn how to write good documentation inside your code.


## Exercise - Writing good comments

````{exercise} In-code-1: Comments
  Let's take a look at two example comments (comments in Python start with `#`):

  **Comment A**
  ```python
  # now we check if temperature is below -50
  if temperature < -50:
      print("ERROR: temperature is too low")
  ```

  **Comment B**
  ```python
  # we regard temperatures below -50 degrees as measurement errors
  if temperature < -50:
      print("ERROR: temperature is too low")
  ```
  Which of these comments is more useful? Can you explain why?

  ```{solution} Solution
  - Comment A describes **what** happens in this piece of code. This can be
    useful for somebody who has never seen Python or a program, but for somebody
    who has, it can feel like a redundant commentary.

  - Comment B is probably more useful as it describes **why** this piece of code
    is there, i.e. its **purpose**.
  ```
````


## Sometimes version control is better than a comment

````{admonition} Examples for code comments where Git is a better solution
  **Keeping zombie code** "just in case" (rather use version control):
  ```python
  # do not run this code!
  # if temperature > 0:
  #     print("It is warm")
  ```
  Instead: Remove the code, you can always find it back in a previous version of your code in Git.

  **Emulating version control**:
  ```python
  # John Doe: threshold changed from 0 to 15 on August 5, 2013
  if temperature > 15:
      print("It is warm")
  ```
  Instead: You can get this information from `git log` or `git show` or `git
  annotate` or similar.
````


## What are "docstrings" and how can they be useful?

Here is function `fahrenheit_to_celsius` which converts temperature in
Fahrenheit to Celsius, implemented in a couple of different languages.
Your language is missing? Please contribute an example.

The first set of examples uses **regular comments**:
````{tabs}
  ```{group-tab} Python
    ```{literalinclude} code/fahrenheit_to_celsius.py
    :language: python
    ```
  ```

  ```{group-tab} R
    ```{literalinclude} code/fahrenheit_to_celsius.R
    :language: R
    ```
  ```

  ```{group-tab} Julia
    ```{literalinclude} code/fahrenheit_to_celsius.jl
    :language: Julia
    ```
  ```

  ```{group-tab} Fortran
    ```{literalinclude} code/fahrenheit_to_celsius.f90
    :language: fortran
    ```
  ```

  ```{group-tab} C++
    ```{literalinclude} code/fahrenheit_to_celsius.cpp
    :language: C++
    ```
  ```

  ```{group-tab} Rust
    ```{literalinclude} code/fahrenheit_to_celsius.rs
    :language: rust
    ```
  ```
````

The second set uses **docstrings or similar concepts**. Please compare the two
(above and below):
````{tabs}
  ```{group-tab} Python
    ```{literalinclude} code/fahrenheit_to_celsius_docstring.py
    :language: python
    ```
    Read more: <https://peps.python.org/pep-0257/>
  ```

  ```{group-tab} R
    ```{literalinclude} code/fahrenheit_to_celsius_docstring.R
    :language: R
    ```
    Read more: <https://cran.r-project.org/web/packages/roxygen2/vignettes/roxygen2.html>
  ```

  ```{group-tab} Julia
    ```{literalinclude} code/fahrenheit_to_celsius_docstring.jl
    :language: Julia
    ```
    Read more: <https://docs.julialang.org/en/v1/manual/documentation/>
  ```

  ```{group-tab} Fortran
    ```{literalinclude} code/fahrenheit_to_celsius_docstring.f90
    :language: fortran
    ```
    Read more: <https://en.wikibooks.org/wiki/Fortran/Documenting_Fortran>
  ```

  ```{group-tab} C++
    ```{literalinclude} code/fahrenheit_to_celsius_docstring.cpp
    :language: C++
    ```
    Read more: <https://www.doxygen.nl>
  ```

  ```{group-tab} Rust
    ```{literalinclude} code/fahrenheit_to_celsius_docstring.rs
    :language: rust
    ```
    Read more: <https://doc.rust-lang.org/rust-by-example/meta/doc.html>
  ```
````

Docstrings can do a bit more than just comments:
- Tools can generate help text automatically from the docstrings.
- Tools can generate documentation pages automatically from code.

It is common to write docstrings for functions, classes, and modules.

Good docstrings describe:
- What the function does
- What goes in (including the type of the input variables)
- What goes out (including the return type)

**Naming is documentation**:
Giving explicit, descriptive names to your code segments (functions, classes,
variables) already provides very useful and important documentation. In
practice you will find that for simple functions it is unnecessary to add a
docstring when the function name and variable names already give enough
information.

---

```{keypoints}
- Comments should describe the why for your code not the what.
- Writing docstrings can be a good way to write documentation while you type
  code since it also makes it possible
  to query that information from outside the code or to auto-generate
  documentation pages.
```
