# Quadratic Solver

A powerful and easy-to-use Command Line Interface (CLI) application for solving 
and visualizing quadratic equations. This tool computes key properties of 
quadratic functions and provides a graphical representation of the curve.

***Note: It is recommended to use the stable release.***


## Features

* Solve quadratic equations of the form:
  **ax² + bx + c = 0**

* Compute:

  * Real or complex roots
  * Discriminant
  * Vertex (turning point)
  * Axis of symmetry
  * Ordered pairs (for plotting)
  * Nature of roots (distinct, repeated, or complex)

* Graph the quadratic function directly from the CLI


## Installation

Install via pip:

```bash
pip install quadratic-solver
```


## Usage

Start by importing the model in Python:

```python
from quadratic_solver.model import QuadraticFunctions
```

Make an instance of QuadraticFunctions:

```python
qf = QuadraticFunctions(8, 23, 1)
```

Then call the methods:

```python
qf.quadratic_formula()  # solve and display the roots, discriminant, vertex and axis of symmetry
qf.plot_and_display_graph() # plot and display graph of the quadratic function
```

## Methods
* convert_to_float - convert user input (a, b, c) to float and returns it. 
* vertex - return tuple of ordered pair (vertex) of the function.
* discriminant - returns the discriminant of the function.
* quadratic_formula - solve and display the roots, discriminant, vertex and axis of symmetry
* plot_and_display_graph - plot and display graph of the quadratic function

## Example Output

```
Quadratic Equation: x² - 3x + 2 = 0

Discriminant: 1
Roots: x₁ = 2, x₂ = 1

Nature of Roots: Real and Distinct

Vertex: (1.5, -0.25)
Axis of Symmetry: x = 1.5

Sample Points:
(0, 2)
(1, 0)
(2, 0)
(3, 2)
```

A graph window will also appear displaying the parabola.


## Graphing

The application automatically generates a plot of the quadratic function, 
highlighting:

* The roots
* The vertex
* The curve shape (concave up or down)


## How It Works

The app uses standard quadratic formula logic:

```
x = (-b ± √(b² - 4ac)) / (2a)
```

* If the discriminant is:

  * **> 0** → Two real roots
  * **= 0** → One repeated root
  * **< 0** → Two complex roots

Graphing is handled programmatically using Python plotting libraries.


## Requirements

* Python 3.10+
* Required dependencies (installed automatically):

  * matplotlib
  * numpy 



## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request


## License

This project is licensed under the MIT License.


## Future Improvements

* Batch processing of multiple equations
* Interactive mode with command flags


## Author

Built by *Uchenna Adubasim*


## Support

If you find this project useful, consider giving it a star on GitHub!
