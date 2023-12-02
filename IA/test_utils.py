import pytest
from utils import *

def test_set_fps():
    set_fps(30.0)
    assert get_fps() == 30.0

def test_set_fps_multiple_times():
    set_fps(60.0)
    assert get_fps() == 60.0
    set_fps(120.0)
    assert get_fps() == 120.0

def test_set_fps_negative_value():
    with pytest.raises(ValueError):
        set_fps(-10.0)

def test_set_precision():
    set_precision(30.0)
    assert get_precision() == 30.0

def test_set_precision_multiple_times():
    set_precision(60.0)
    assert get_precision() == 60.0
    set_precision(120.0)
    assert get_precision() == 120.0

def test_set_precision_negative_value():
    with pytest.raises(ValueError):
        set_precision(-10.0)