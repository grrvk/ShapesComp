from src.io import get_input
from src.scheme import Shape


def main():
    input_data = get_input()

    for data in input_data:
        shape = Shape(data)
        print(shape)


if __name__ == "__main__":
    main()