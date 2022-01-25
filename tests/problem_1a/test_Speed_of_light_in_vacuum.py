# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 01 (Modules)
# PROBLEM NUMBER: 1a

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'constants.py'
POINTS = 2

def test_Speed_of_light_in_vacuum():
    return _test_variable("c", 299792458,
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )
