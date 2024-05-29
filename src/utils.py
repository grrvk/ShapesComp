import numpy as np


def square_test_input(input_data_array: list[str]):
    try:
        if "TopRight" not in input_data_array and "Side" not in input_data_array: return None
        top_right_x = float(input_data_array[input_data_array.index('TopRight') + 1])
        top_right_y = float(input_data_array[input_data_array.index('TopRight') + 2])
        side = float(input_data_array[input_data_array.index('Side') + 1])
        if side <= 0: raise ValueError
        return [(top_right_x - side, top_right_y), (top_right_x, top_right_y),
                (top_right_x, top_right_y - side), (top_right_x - side, top_right_y - side)]
    except Exception:
        return None


def rectangle_test_input(input_data_array: list[str]):
    try:
        if "TopRight" not in input_data_array and "BottomLeft" not in input_data_array: return None
        top_right_x = float(input_data_array[input_data_array.index('TopRight') + 1])
        top_right_y = float(input_data_array[input_data_array.index('TopRight') + 2])
        bottom_left_x = float(input_data_array[input_data_array.index('BottomLeft') + 1])
        bottom_left_y = float(input_data_array[input_data_array.index('BottomLeft') + 2])
        return [(bottom_left_x, top_right_y), (top_right_x, top_right_y),
                (top_right_x, bottom_left_y), (bottom_left_x, bottom_left_y)]
    except Exception:
        return None


def circle_test_input(input_data_array: list[str]):
    try:
        center = [float(input_data_array[input_data_array.index('Center') + 1]),
                  float(input_data_array[input_data_array.index('Center') + 2])]
        radius = float(input_data_array[input_data_array.index('Radius') + 1])
        if radius <= 0: raise ValueError
        return [center, radius]
    except Exception:
        return None


def points_test_input(input_data_array: list[str]):
    points = []
    try:
        for i, entry in enumerate(input_data_array):
            if "Point" in entry:
                points.append((float(input_data_array[i + 1]), float(input_data_array[i + 2])))
        return points if points else None
    except Exception:
        return None


def get_line_length(a: tuple, b: tuple):
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
