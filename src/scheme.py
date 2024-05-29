import numpy as np
from src.utils import (get_line_length, square_test_input, rectangle_test_input,
                       circle_test_input, points_test_input)


class Shape:
    def __init__(self, input_data: str):
        self.points = None
        self.name = None
        self.area = None
        self.perimeter = None
        self.determine_shape(input_data)

    def determine_shape(self, input_data: str):
        input_data_array = input_data.split(" ")
        self.name = input_data_array[0]
        if self.name == "Square":
            square_test_data = square_test_input(input_data_array)
            self.points = square_test_data if square_test_data is not None \
                else points_test_input(input_data_array)
        elif self.name == "Rectangle":
            rectangle_test_data = rectangle_test_input(input_data_array)
            self.points = rectangle_test_data if rectangle_test_data is not None \
                else points_test_input(input_data_array)
        else:
            if self.name != "Circle":
                self.points = points_test_input(input_data_array)
            else:
                self.points = circle_test_input(input_data_array)
        self.get_data()

    def get_data(self):
        if self.name == "Circle" and self.points is not None:
            self.perimeter = 2 * np.pi * self.points[1]
            self.area = np.pi * self.points[1] ** 2
        else:
            self.perimeter = self.calculate_perimeter_pointed()
            self.area = self.calculate_area_pointed()

    def calculate_area_pointed(self):
        if self.points is None: return
        point_mults = [(self.points[i + 1][0] - self.points[i][0]) * (self.points[i + 1][1] + self.points[i][1])
                       for i in range(len(self.points) - 1)]
        point_mults.append((self.points[0][0] - self.points[len(self.points) - 1][0]) *
                           (self.points[0][1] + self.points[len(self.points) - 1][1]))
        return 0.5 * sum(point_mults) if sum(point_mults) >= 0 else -0.5 * sum(point_mults)

    def calculate_perimeter_pointed(self):
        if self.points is None: return
        line_lengths = [get_line_length(self.points[i], self.points[i + 1])
                        for i in range(len(self.points) - 1)]
        line_lengths.append(get_line_length(self.points[0], self.points[len(self.points) - 1]))
        return sum(line_lengths)

    def __repr__(self):
        if self.perimeter is not None and self.area is not None:
            return f'Shape {self.name}: perimeter = {self.perimeter}, area = {self.area}'
        else:
            return f'Shape {self.name}: Invalid input. Cannot compute perimeter and area'
