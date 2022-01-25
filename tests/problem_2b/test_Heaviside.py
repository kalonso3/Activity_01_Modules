# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 01 (Modules)
# PROBLEM NUMBER: 2b

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'problem2.py'
POINTS = 2

def test_Heaviside():
    return _test_variable("y", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )
