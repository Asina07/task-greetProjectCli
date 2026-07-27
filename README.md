# Greeter

A simple Python project that provides a greeting module.

## Features

- A `greet(name)` function in the `greet` module that returns `"Hello, {name}!"`.

## Installation

To install the project dependencies (including development tools like `pylint`), run:

```bash
python -m pip install -r requirements.txt
```

## Running Linting

To run static code analysis with `pylint`, use the following command:

```bash
python -m pylint greet.py test_greet.py
```

## Running Tests

To run the unit tests, use the following command:

```bash
python -m unittest test_greet.py
```

