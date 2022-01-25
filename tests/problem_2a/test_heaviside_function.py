# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 01 (Modules)
# PROBLEM NUMBER: 2a

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_function

FILENAME = 'myfuncs.py'
POINTS = 4

@pytest.mark.parametrize(("args", "kwargs", "reference"),
                         list(zip([[0], [-1e+100], [42.1], [1.2e-24], [10], [-10]], [{}, {}, {}, {}, {}, {}], [0.5, 0, 1.0, 1.0, 1.0, 0])))
def test_heaviside_function(args, kwargs, reference):
    return _test_function("heaviside",
                          args,     # tuple or list
                          kwargs,   # dict
                          reference,
                          FILENAME,
                          check_type=False,
                          rtol=None,
                          atol=None,
                          )

