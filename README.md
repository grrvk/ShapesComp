## Shape area and perimeter computing

Creates shapes from data collected from input, computes area and perimeter. For square and circle figure validates side and radius length.  
For common shapes such as Square, Rectangle and Circle creates child class (parent - shape) objects, for others - uses parent class Shape.  
for common pointy shapes accepts two types of input and can compute using two formulas.

## Acceptable input

ONLY Square: TopRight *x_xoord, y_coord* Side *value*  
ONLY Rectangle: TopRight *x_xoord, y_coord* BottomLeft *x_xoord, y_coord*   
ONLY Circle: Center *x_xoord, y_coord* Radius *value*

For all shapes with edges: *Shape_name* Point1 *x_xoord, y_coord* ... PointN *x_xoord, y_coord*

## Run tests

```bash
pytest -q tests/test_main.py
```
