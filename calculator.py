#Lab 3 Scientific Calculator
import math
def square_root(a):
        if a < 0:
            raise ValueError("square root input must be non-negative")
        return math.sqrt(a)

def hypotenuse(a, b):
    try:
        return math.hypot(a,b)
    except Exception as e:
        print(f"Error: {e}")

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero is not allowed")
    return a / b
def log(a, b):
    if b <= 0:
        raise ValueError("logarithm input must be positive")
    if a <= 0 or a == 1:
        raise ValueError("logarithm base must be positive and not equal to 1")
    math.log(b, a)
def exp(a, b):
    return a ** b










def print_menu(current_result):
    # Prints the "Current Result" header and the full menu, ending with the selection prompt.
    print(f"\nCurrent Result: {current_result}")
    print("\nCalculator Menu")
    print("---------------")
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average")
    print("\nEnter Menu Selection: ", end="")

def get_operand(prompt, current_result):
    while True:
        s = input(prompt).strip()
        if s == "RESULT":
            return float(current_result)
        try:
            return float(s)
        except ValueError:
            # Keep prompting until a valid float or RESULT is given
            continue

def main():
    current_result = 0.0
    sum_of_calculations = 0.0
    num_calculations = 0

    # Initially print the menu once
    print_menu(current_result)

    while True:
        selection_raw = input().strip()

        # Validate selection is an integer
        try:
            selection = int(selection_raw)
        except ValueError:
            print("Error: Invalid selection!")
            print("\nEnter Menu Selection: ", end="")
            continue

        if selection == 0:
            print("Thanks for using this calculator. Goodbye!")
            break

        elif selection in (1, 2, 3, 4, 5, 6):
            # Read operands; accept float or "RESULT"
            op1 = get_operand("Enter first operand: ", current_result)
            op2 = get_operand("Enter second operand: ", current_result)
            # Ensure a newline after the last prompt so the next output starts on a new line
            print()

            error_occurred = False
            result = current_result  # default

            if selection == 1:
                result = op1 + op2
            elif selection == 2:
                result = op1 - op2
            elif selection == 3:
                result = op1 * op2
            elif selection == 4:
                # Division with zero-check
                if op2 == 0:
                    print("Error: Division by zero!")
                    error_occurred = True
                else:
                    result = op1 / op2
            elif selection == 5:
                # Exponentiation: op1 ^ op2
                try:
                    result = op1 ** op2
                except Exception:
                    # For domain errors like negative base to fractional power
                    print("Error: Invalid exponentiation operation!")
                    error_occurred = True
            elif selection == 6:
                # Logarithm: log_base(op2) with base = op1
                base = op1
                value = op2
                if base <= 0 or base == 1 or value <= 0:
                    print("Error: Logarithm undefined for given base/value!")
                    error_occurred = True
                else:
                    try:
                        result = math.log(value, base)
                    except ValueError:
                        print("Error: Logarithm undefined for given base/value!")
                        error_occurred = True

            if not error_occurred:
                current_result = result
                sum_of_calculations += current_result
                num_calculations += 1

                # Print the menu (which includes Current Result) exactly once
                print_menu(current_result)
            else:
                # On error, reprint the menu without updating state
                print_menu(current_result)

        elif selection == 7:
            if num_calculations == 0:
                print("Error: No calculations yet to average!")
            else:
                average = sum_of_calculations / num_calculations
                print(f"Sum of calculations: {sum_of_calculations}")
                print(f"Number of calculations: {num_calculations}")
                print(f"Average of calculations: {average:.2f}")
            # Immediately prompt for the next selection without redisplaying the menu
            print("\nEnter Menu Selection: ", end="")

        else:
            # Invalid selection per spec/grader
            print("Error: Invalid selection!")
            # Prompt again without redisplaying the menu
            print("\nEnter Menu Selection: ", end="")

if __name__ == "__main__":
    main()

