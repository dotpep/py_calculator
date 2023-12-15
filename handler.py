def input_exception_handler(func, *args):
    """Handle exceptions during input and calls the specified function."""
    while True:
        try:
            result = func(*args)
            break
        except Exception as e:
            print(f"Error: {e}")

    return result


def input_value_handler(allowed_values: tuple) -> tuple:
    """Handle input for values a and b."""

    def is_positive_number(value):
        return isinstance(value, allowed_values) and value > 0

    def try_input():
        a = float(input("a: "))
        b = float(input("b: "))

        if not all(is_positive_number(x) for x in (a, b)):
            raise ValueError(f"Invalid Value!\
            \nAllowed value types: {allowed_values}, integer: 1, float: 1.11.\
            \nMust be positive numbers. Negative numbers are not allowed.")

        return a, b

    return input_exception_handler(try_input)


def input_operator_handler(allowed_operators: tuple) -> str:
    """Handle input for the operator."""

    def try_input():
        operator = input(f"operator {allowed_operators}: ")

        if operator in allowed_operators:
            return operator
        else:
            raise ValueError(f"Invalid Operator!\
            \nAllowed operators: {allowed_operators}")

    return input_exception_handler(try_input)
