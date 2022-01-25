<!-- -*- coding: utf-8 -*- -->
# Activity 01: Modules and Classes
[![GitHub Classroom Workflow](../../workflows/GitHub%20Classroom%20Workflow/badge.svg?branch=main)](../../actions/workflows/classroom.yml) ![Points badge](../../blob/badges/.github/badges/points.svg)


Solve the following problems.

See https://py4phy.github.io/PHY432/modules/python/modules_packages/ for help.

## constants module

1. Create a module `constants.py` with values for the mathematical
   constant [π](https://mathworld.wolfram.com/Pi.html) (named `pi`,
   see also OEIS [A000796](http://oeis.org/A000796)) and the physical
   constants `c` for the [speed of light in
   vaccuum](https://physics.nist.gov/cgi-bin/cuu/Value?c) (in ms/s)
   and [Planck's
   constant](https://physics.nist.gov/cgi-bin/cuu/Value?h) `h` (in J
   s).

2. In a file `problem1.py`, import your *constants* module and compute
   the reduced Planck's constant ħ = h/2π and store it in variable
   `hbar`. Print it to all 9 significant figures in scientific notation with
   ```python
   print(f"hbar = {hbar:.9e}")
   ```
   (See both the [Format Specification
   Mini-Language](https://docs.python.org/3/library/string.html#formatspec)
   and
   [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals)
   if you need a reminder about formatting strings.)


## myfuncs module

You will create your own *myfuncs* module that contains an
implementation of the [Heaviside step
function](http://mathworld.wolfram.com/HeavisideStepFunction.html). You
will use your module for a function evaluation.

1. [Define the Heaviside
   function](https://py4phy.github.io/PHY432/modules/python/functions/#functions)
   in file `myfuncs.py` with the name `heaviside()`.
2. In file `problem2.py`, compute *Heaviside(n)* for the integers -10 ≤ n ≤ 10, assign the
   list to a variable `y`, and print it with
   ```python
   print(f"Heaviside: {y}")
   ```


## Standard library

Import the *[math](https://docs.python.org/3/library/math.html)*
module and the *[os](https://docs.python.org/3/library/os.html)*
module from the [Python Standard
Library](https://docs.python.org/3/library/index.html) in a file
`problem3.py`. Look in these modules for functions and attributes to
solve the following problems:

1. Compute `y_full_circle =
   sin(`[`tau`](https://docs.python.org/3/library/math.html#math.tau)`)`. (Optionally,
   you can also print the value.)

2. Get the current working directory as a string and assign to the
   variable `cwd` and print it with
   ```python
   print(f"cwd = '{cwd}'")
   ```
