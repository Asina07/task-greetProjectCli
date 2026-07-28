[![Python Tests](https://github.com/Asina07/task-greetProjectCli/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/Asina07/task-greetProjectCli/actions/workflows/test.yml)

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



## Pull Requests and CI

When creating a pull request, GitHub Actions automatically runs the test workflow.
The CI badge at the top of this README shows the current status of the latest workflow run.

### How to create a pull request
1. Create a new branch.
2. Make your changes (e.g., add a new test case).
3. Push the branch to GitHub.
4. Open a pull request from your branch into `main`.
5. Wait for the CI checks to complete.
6. Review the results and merge if the tests pass.

The CI badge will update to reflect the latest pipeline status.



## Manually Triggering the CI Workflow

This project supports manual workflow runs using GitHub Actions.

### How to Run the Workflow Manually

1. Open the repository on GitHub.
2. Click the **Actions** tab.
3. Select the workflow named **Python Tests**.
4. Click the **Run workflow** button on the right.
5. Choose the branch (e.g., `main`) and click **Run workflow**.

GitHub will start the workflow immediately. You can open the run to watch logs and verify that all tests pass.
