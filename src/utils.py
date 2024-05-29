import numpy as np

from src.scheme import Shape, ShapesEnum


def get_input():
    print("Please enter data:")
    rows = []
    while True:
        line = input()
        if line:
            rows.append(line)
        else:
            break
    return rows


def dispatcher(input_data):
    input_data_array = input_data.split(" ")
    name = input_data_array[0]
    try:
        return ShapesEnum[name].value(), input_data_array[1:]
    except KeyError:
        return Shape(name), input_data_array[1:]
