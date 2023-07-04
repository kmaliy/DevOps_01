"""python01-hw % basic calculator."""

import logging

# variables
operations = {
    "1": "Addition",
    "2": "Subtraction",
    "3": "Multiplication",
    "4": "Division",
}


def calculator(first_user_input: int, second_user_input: int, operation: str) -> int:
    """
     Performs a basic arithmetic operation on two numbers.

    Args:
        first_user_input (int): The first number in the operation.
        second_user_input (int): The second number in the operation.
        operation (str): A string representing the operation to be performed.
                         '1' for addition, '2' for subtraction,
                         '3' for multiplication, and '4' for division.

    Returns:
        int: The result of the operation. If the operation is division, the result may be a float.

    Raises:
        ValueError: If operation is not one of '1', '2', '3', or '4'.
    """
    if operation == "1":
        calculation_output = first_user_input + second_user_input
    elif operation == "2":
        calculation_output = first_user_input - second_user_input
    elif operation == "3":
        calculation_output = first_user_input * second_user_input
    elif operation == "4":
        calculation_output = first_user_input / second_user_input

    return print(calculation_output)


if __name__ == "__main__":
    print("Welcome to the Calculator Program!\n")
    while True:
        try:
            first_user_input = int(input("Please enter the first number: "))
            break
        except ValueError:
            print("That's not a valid number, please try again.")

    while True:
        try:
            second_user_input = int(input("Please enter the second number: "))
            break
        except ValueError:
            print("That's not a valid number, please try again.")
    print("\nPlease select an operation:")

    for number, operation in operations.items():
        print(f"{number}. {operation}")
    operation_choice = input("\nEnter your choice (1-4): ")

    if operations.get(operation_choice) is None:
        logging.error("The operation you chose is out of the given range")

    calculator(first_user_input, second_user_input, operation_choice)
