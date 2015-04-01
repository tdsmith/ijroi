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

def test_rectangle():
    fixture = get_fixture("subpixel_rectangle.roi")
    with fixture.open("rb") as f:
        rect = ijroi.read_roi(f)
    assert (rect == np.array([[4, 5], [8, 5], [8, 10], [4, 10]])).all()
    assert rect.dtype == np.float32

    fixture = get_fixture("integer_rectangle.roi")
    with fixture.open("rb") as f:
        rect = ijroi.read_roi(f)
    assert (rect == np.array([[4, 5], [8, 5], [8, 10], [4, 10]])).all()
    assert rect.dtype == np.int16

def test_freehand_circle():
    fixture = get_fixture("freehand_circle.roi")
    with fixture.open("rb") as f:
        circle = ijroi.read_roi(f)
    assert abs(circle[:,1].mean()-10) < 0.01
