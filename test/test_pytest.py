import sys
import os
import pytest

# Add the 'src' directory to sys.path to ensure it is found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Now import the calculator functions
from calculator import fun1, fun2, fun3, fun4

# Test for fun1 (addition)
def test_fun1():
    assert fun1(2, 3) == 5
    assert fun1(5, 0) == 5
    assert fun1(-1, 1) == 0
    assert fun1(-1, -1) == -2

# Test for fun2 (subtraction)
def test_fun2():
    assert fun2(2, 3) == -1
    assert fun2(5, 0) == 5
    assert fun2(-1, 1) == -2
    assert fun2(-1, -1) == 0

# Test for fun3 (multiplication)
def test_fun3():
    assert fun3(2, 3) == 6
    assert fun3(5, 0) == 0
    assert fun3(-1, 1) == -1
    assert fun3(-1, -1) == 1

# Test for fun4 (sum of three numbers)
def test_fun4():
    assert fun4(2, 3, 5) == 10
    assert fun4(5, 0, -1) == 4
    assert fun4(-1, -1, -1) == -3
    assert fun4(-1, -1, 100) == 98

