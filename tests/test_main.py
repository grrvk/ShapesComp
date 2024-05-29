import pytest
import sys

sys.path.append(".")
from src.scheme import Shape


@pytest.mark.parametrize("input_data, perimeter, area", [
    ("Square TopRight 4 4 Side 10", 40, 100),
    ("Rectangle TopRight 3 5 BottomLeft 0 0", 16, 15),
    ("Circle Center -1 4 Radius 5", 31.41592653589793, 78.53981633974483),
    ("Circle Center -1 4 Radius 5", 31.41592653589793, 78.53981633974483),
    ("Triangle Point1 5 5 Point2 8 9 Point3 11 5", 16, 12),
    ("Rectangle Point1 1 1 Point2 1 4 Point3 4 4 Point4 4 1", 12, 9),
    ("Polygon Point1 -2 -2 Point2 0 4 Point3 3 -1 Point4 1 -1", 17.317784875350437, 13),
    ("Invalid", None, None),
    ("Circle Center 1 1 Radius -4", None, None),
])
def test_shape_get_data(input_data, perimeter, area):
    shape = Shape(input_data)
    assert shape.perimeter == perimeter
    assert shape.area == area

#pytest -q tests/test_main.py
