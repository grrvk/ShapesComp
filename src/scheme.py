import numpy as np
from enum import Enum


def get_line_length(a: tuple, b: tuple):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


class Shape:
    def __init__(self, name=None):
        self.points = None
        self.area = None
        self.perimeter = None
        self.name = name

    def calculate(self, input_data_array):
        self.get_points_input(input_data_array)
        self.calculate_perimeter_pointed()
        self.calculate_area_pointed()

    def get_points_input(self, input_data_array):
        points = []
        try:
            for i, entry in enumerate(input_data_array):
                if "Point" in entry:
                    points.append((float(input_data_array[i + 1]), float(input_data_array[i + 2])))
            self.points = points if points else None
        except Exception:
            self.points = None

    def calculate_area_pointed(self):
        if self.points is None: return
        point_mults = [(self.points[i + 1][0] - self.points[i][0]) * (self.points[i + 1][1] + self.points[i][1])
                       for i in range(len(self.points) - 1)]
        point_mults.append((self.points[0][0] - self.points[len(self.points) - 1][0]) *
                           (self.points[0][1] + self.points[len(self.points) - 1][1]))
        self.area = 0.5 * sum(point_mults) if sum(point_mults) >= 0 else -0.5 * sum(point_mults)

    def calculate_perimeter_pointed(self):
        if self.points is None: return
        line_lengths = [get_line_length(self.points[i], self.points[i + 1])
                        for i in range(len(self.points) - 1)]
        line_lengths.append(get_line_length(self.points[0], self.points[len(self.points) - 1]))
        self.perimeter = sum(line_lengths)

    def __repr__(self):
        if self.perimeter is not None and self.area is not None:
            return f'Shape {self.name}: perimeter = {self.perimeter}, area = {self.area}'
        else:
            return f'Shape {self.name}: Invalid input. Cannot compute perimeter and area'


class Rectangle(Shape):
    def __init__(self, name="Rectangle"):
        super().__init__(name=name)
        self.TopRight = None
        self.BottomLeft = None

    def calculate(self, input_data_array):
        if not self.get_rectangle_input(input_data_array): self.get_points_input(input_data_array)
        if not self.calculate_perimeter_rectangle(): self.calculate_perimeter_pointed()
        if not self.calculate_area_rectangle(): self.calculate_area_pointed()

    def get_rectangle_input(self, input_data_array):
        try:
            if "TopRight" not in input_data_array or "BottomLeft" not in input_data_array: return False
            self.TopRight = (float(input_data_array[input_data_array.index('TopRight') + 1]),
                             float(input_data_array[input_data_array.index('TopRight') + 2]))
            self.BottomLeft = (float(input_data_array[input_data_array.index('BottomLeft') + 1]),
                               float(input_data_array[input_data_array.index('BottomLeft') + 2]))
            return True
        except Exception:
            return False

    def calculate_perimeter_rectangle(self):
        if not self.TopRight or not self.BottomLeft: return None
        self.perimeter = 2 * ((self.TopRight[0] - self.BottomLeft[0]) + (self.TopRight[1] - self.BottomLeft[1]))
        if self.perimeter < 0: self.perimeter *= -1

    def calculate_area_rectangle(self):
        if not self.TopRight or not self.BottomLeft: return None
        self.area = (self.TopRight[0] - self.BottomLeft[0]) * (self.TopRight[1] - self.BottomLeft[1])
        if self.area < 0: self.area *= -1


class Square(Rectangle):
    def __init__(self):
        super().__init__(name="Square")
        self.TopRight = None
        self.Side = None

    def calculate(self, input_data_array):
        if not self.get_square_input(input_data_array): self.get_points_input(input_data_array)
        if not self.calculate_perimeter_rectangle(): self.calculate_perimeter_pointed()
        if not self.calculate_area_rectangle(): self.calculate_area_pointed()

    def get_square_input(self, input_data_array):
        try:
            if "TopRight" not in input_data_array or "Side" not in input_data_array: return False
            self.TopRight = (float(input_data_array[input_data_array.index('TopRight') + 1]),
                             float(input_data_array[input_data_array.index('TopRight') + 2]))
            self.Side = float(input_data_array[input_data_array.index('Side') + 1])
            if self.Side <= 0:
                self.Side = None
                return False
            self.BottomLeft = (self.TopRight[0]-self.Side, self.TopRight[1]-self.Side)
            return True
        except Exception:
            return False


class Circle(Shape):
    def __init__(self):
        super().__init__(name="Circle")
        self.Center = None
        self.Radius = None

    def calculate(self, input_data_array):
        self.get_circle_input(input_data_array)
        self.calculate_perimeter_circle()
        self.calculate_area_circle()


    def get_circle_input(self, input_data_array):
        try:
            if "Center" not in input_data_array or "Radius" not in input_data_array: return False
            self.Center = [float(input_data_array[input_data_array.index('Center') + 1]),
                           float(input_data_array[input_data_array.index('Center') + 2])]
            self.Radius = float(input_data_array[input_data_array.index('Radius') + 1])
            if self.Radius <= 0:
                self.Radius = None
                return
            return
        except Exception:
            return

    def calculate_perimeter_circle(self):
        if not self.Radius: return None
        self.perimeter = 2 * np.pi * self.Radius

    def calculate_area_circle(self):
        if not self.Radius: return None
        self.area = np.pi * self.Radius ** 2


class ShapesEnum(Enum):
    Square = Square
    Rectangle = Rectangle
    Circle = Circle
