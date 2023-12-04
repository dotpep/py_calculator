from typing import Union, List


class PositiveNumberError(Exception):
   pass


def add(*args: Union[int, float]) -> Union[int, float]:
    """Sum all arguments passed in.
    
    Returns:
        Union[int, float]: _description_
    """
    result: Union[int, float] = 0
    for arg in args:
        result += arg

    return result
    #return sum(args)



def user_input_bar() -> List[Union[int, float]]:
    """Get user input and return a list of numbers.
    
    Returns:
        List[int, float]: _description_
    """
    numbers: List[Union[int, float]] = []

    while True:
        try:
            user_input: Union[str, int, float] = input("\ntype 'q' to quit\
                               \nEnter a number: ")
            
            if user_input == 'q':
                break

            number: Union[int, float] = float(user_input)

            if number < 0:
                raise PositiveNumberError("Negative number entered. Please enter a positive number.")

            numbers.append(number)

        except ValueError:
            print("|ERROR|:", "Invalid input. Please enter a valid number.")
        except PositiveNumberError as e:
            print("|ERROR|:", e)
        
    #if all(isinstance(item, int) for item in numbers):
    #    numbers = [int(x) for x in numbers]

    #print(type(numbers[0]))

    return numbers


def main() -> None:
    print("---My Calculator---")
    calcul1 = add(5, 5, 5.5)
    print(calcul1)
    print(type(calcul1))


    values = user_input_bar()
    
    #if all(isinstance(item, int) for item in values):
    #    values = [int(x) for x in values]

    #if all(isinstance(item, int) for item in values):
    #    calcul2 = int(calcul2)

    #if not any(isinstance(item, float) for item in values):
    #    calcul2 = int(calcul2)
    
    #print(type(values))
    #print(values)

    calcul2 = add(*values)

    print(calcul2)

    #if not values:
    #    print("No values entered. Exiting...")
    #    exit()

if __name__ == "__main__":
    main()
