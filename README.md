**MLOps Lab 1: Python Testing and GitHub Actions**
Overview

This project implements basic arithmetic functions in Python and automates testing using Pytest and Unittest. GitHub Actions is set up to automatically run tests when changes are pushed to the repository.

Folder Structure
mlops_lab_01/
│
├── .github/
│   └── workflows/
│       ├── pytest.yml    # Pytest workflow
│       └── unittest.yml  # Unittest workflow
│
├── src/
│   ├── calculator.py     # Arithmetic functions
│
├── test/
│   ├── test_pytest.py    # Pytest tests
│   └── test_unittest.py  # Unittest tests
│
├── data/
│   └── __init__.py       # Marks data as a Python package
│
├── requirements.txt      # Dependencies (pytest, unittest)
└── .gitignore            # Exclude unnecessary files

Setup Instructions

Create and activate virtual environment:

python -m venv lab_01
source lab_01/bin/activate


Install dependencies:

pip install -r requirements.txt


Run Tests Locally:

Pytest:

pytest test/test_pytest.py


GitHub Actions

Pytest and Unittest workflows are defined to run on push events to the main branch.

Workflows are located in .github/workflows/pytest.yml and .github/workflows/unittest.yml.

License

MIT License
