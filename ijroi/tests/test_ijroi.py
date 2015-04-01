import os

import numpy as np
import py
import pytest

import ijroi

def get_fixture(name):
    dirpath = py.path.local(__file__).dirpath()
    return dirpath.join("fixtures", name)

def test_ijroi_import():
    assert ijroi.__version__

@pytest.mark.xfail(raises=ValueError)
def test_unit_rectangle():
    fixture = get_fixture("unit_rectangle.roi")
    with fixture.open() as f:
        rect = ijroi.read_roi(f)
    print(rect)

def test_freehand_circle():
    fixture = get_fixture("freehand_circle.roi")
    with fixture.open() as f:
        circle = ijroi.read_roi(f)
    assert abs(circle[:,1].mean()-10) < 0.01
