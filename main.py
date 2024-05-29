from src.utils import get_input, dispatcher
from src.scheme import Shape


def main():
    input_data = get_input()

    for data in input_data:
        shape, input_array = dispatcher(data)
        shape.calculate(input_array)
        print(shape)


if __name__ == "__main__":
    main()