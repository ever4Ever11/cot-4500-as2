# Introduction:

This program contains several iterative methods for approximating the value of a function based on a finite set of points. The methods available for finding the values of a function are the neville, newton forward diffenece and hermite methods. This program is also able to compute the A matrix, and b and x vectors for finding a cubic spline interpolant of a function. These methods are run using the appropriate subcommand of the program. For help on the arguments expected for each subcommand, use --help and see the examples below.

The primary external dependency of this program is numpy used for its array data type and to solve the x vector in the spline method.

# Run Instructions:

## Option 1: An easy way to run the program is from an editable install of the source directory.

To do this:
1. Create a virtual environment in the top level project directory \
`python -m venv .venv`
2. Activate the virtual environment \
`source .venv/bin/activate`
3. Editable install in the directory with the pyproject.toml \
`python -m pip install --editable .`
4. Run the program \
`python -m main ... (see below for sample inputs)`

The program can also be tested from the top level project directory: \
`python -m unittest discover -v -s src`

## Option 2: The program can be run installing only the requirements.txt

To do this:
1. Create a virtual environment in the top level project directory \
`python -m venv .venv`
2. Activate the virtual environment \
`source .venv/bin/activate`
3. Install the requirement packages \
`python -m pip install -r requirements.txt`
4. Run the program from the src directory \
`python -m main ... (see below for sample inputs)`

# Examples:

`python -m main answers` \
Result: ...

`python -m main neville --x-values 2.0 2.2 2.3 --f-values 0.6931 0.7885 0.8329 --x-value 2.1` \
Result: 0.74189999

`python -m main newton --x-values 8.1 8.3 8.6 8.7 --f-values 16.94410 17.56492 18.50515 18.82091 --x-value 8.4` \
Result: 17.87714249

`python -m main hermite --x-values 1.3 1.6 1.9 --f-values 0.6200860 0.4554022 0.2818186 --d-values -0.5220232 -0.5698959 -0.5811571 --x-value 1.5` \
Result: 0.51182770

`python -m main spline --x-values 0 1 2 3 --f-values 1 2.718281828 7.389056099 20.08553692` \
Result: \
[[1. 0. 0. 0.] [1. 4. 1. 0.] [0. 1. 4. 1.] [0. 0. 0. 1.]] \
[0. 8.85747733 24.07711965 0.] \
[0. 0.75685264 5.83006675 0.]
