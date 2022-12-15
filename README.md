# prime-factors
A repository demonstrating prime factorization.

![Test](https://github.com/ocrosby/prime-factors/actions/workflows/python-app.yml/badge.svg)

## Problem Description
The following task has two parts.  First you must figure out the principle behind the following encoding of natural
numbers.  The table blow displays the encoding of the numbers from 0 to 11.



## Setup
Create a virtual environment and install the requirements:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


## Usage

This repository uses a tool called invoke to execute build and test tasks.  To see a list of available tasks, run:

```bash
invoke --list
```

To run the tests, run:

```bash
invoke test
```

To run the tests with coverage, run:

```bash
invoke cover
```

To update the current version of pip, run:

```bash
invoke update-pip
```

To clean up the repository, run:

```bash
invoke clean
```

## Running the tests
Run the tests with pytest:

```bash
pytest
```
