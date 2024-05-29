## Shape area and perimeter computing

Creates shapes from data collected from input, computes area and perimeter. For square and circle figure validates side and radius length.

To compute area and perimeter each shape is considered as an array of points (except circles), so algorythm is easy to use to compute values for more complex shapes with edges

## Acceptable input

ONLY Square: TopRight *x_xoord, y_coord* Side *value*  
ONLY Rectangle: TopRight *x_xoord, y_coord* BottomLeft *x_xoord, y_coord*   
ONLY Circle: Center *x_xoord, y_coord* Radius *value*

For all shapes with edges: *Shape_name* Point1 *x_xoord, y_coord* ... PointN *x_xoord, y_coord*

## Run tests

```bash
pytest -q tests/test_main.py
```
