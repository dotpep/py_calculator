from math_standard import add, subtract, divide, multiply
from handler import input_value_handler, input_operator_handler

_ = ('+', '-', '*', '/')


def main() -> None:
    AVAILABLE_OPERATORS: tuple = ('+', '-', '*', '/')
    AVAILABLE_VALUES_TYPE: tuple = (int, float)

    a, b = input_value_handler(AVAILABLE_VALUES_TYPE)

    user_operator = input_operator_handler(AVAILABLE_OPERATORS)

    match user_operator:
        case '+':
            print(f"Result of adding {a=} to {b=} is: ", add(a, b))
        case '-':
            print(f"Result of subtracting {a=} to {b=} is: ", subtract(a, b))
        case '*':
            print(f"Result of multiplying {a=} to {b=} is: ", multiply(a, b))
        case '/':
            print(f"Result of dividing {a=} to {b=} is: ", divide(a, b))
        case _:
            print("Something went wrong!")


if __name__ == "__main__":
    main()
