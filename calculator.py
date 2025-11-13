#https://github.com/Andres-Arvelo/lab11-AA-FZ.git
#Partner 1: Andres Arvelo
#Partner 2: Fareed Zaki

#In this project, you will build a scientific calculator on the command line. The program will display a menu of options which includes several arithmetic operations as well as options to display statistics and exit the program. The project is designed to give you an opportunity to practice looping, type conversion, and data persistence.
import math

def add(a, b):
    return a+ b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a==0:
        raise ZeroDivisionError
    b / a # raise ZeroDivisionError if a == 0


def log(a, b):
    loga(b)# use math library + raise ValueError
    if a<=0 or a==1 or b<=0:
        raise ValueError
    return math.log(b,a)


def exp(a, b):
    return a**b


program = 1
result = 0.0

totresult = 0.0
numcalc = 0

print(f"Current Result: 0.0")

print("\nCalculator Menu\n---------------\n0. Exit Program")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average\n")

while program != 0:

    selection = int(input("Enter Menu Selection: "))

    #end program 0
    if selection == 0:
        print("Thanks for using this calculator. Goodbye!")
        break
        program = 0

    #addition 1
    elif selection == 1:
        operand1 = input("Enter first operand: ")
        if operand1 == 'RESULT':
                operand1 = result
        else:
                operand1 = float(operand1)

        operand2 = input("Enter second operand: ")
        if operand2 == 'RESULT':
                operand2 = result
        else:
                operand2 = float(operand2)
        result = operand1 + operand2
        print(f"Current Result: {result}")
        totresult = totresult + result
        numcalc += 1

    #subtraction 2
    elif selection == 2:
        operand1 = input("Enter first operand: ")
        if operand1 == 'RESULT':
            operand1 = result
        else:
            operand1 = float(operand1)

        operand2 = input("Enter second operand: ")
        if operand2 == 'RESULT':
            operand2 = result
        else:
            operand2 = float(operand2)
        result = operand1 - operand2
        print(f"Current Result: {result}")
        totresult = totresult + result
        numcalc += 1

    #Multiplication 3
    elif selection == 3:
        operand1 = input("Enter first operand: ")
        if operand1 == 'RESULT':
            operand1 = result
        else:
            operand1 = float(operand1)

        operand2 = input("Enter second operand: ")
        if operand2 == 'RESULT':
            operand2 = result
        else:
            operand2 = float(operand2)
        result = operand1 * operand2
        print(f"Current Result: {result}")
        totresult = totresult + result
        numcalc += 1

    #division 4
    elif selection == 4:
        operand1 = input("Enter first operand: ")
        if operand1 == 'RESULT':
            operand1 = result
        else:
            operand1 = float(operand1)

        operand2 = input("Enter second operand: ")
        if operand2 == 'RESULT':
            operand2 = result
        else:
            operand2 = float(operand2)
        result = operand1 / operand2
        print(f"Current Result: {result}")
        totresult = totresult + result
        numcalc += 1

    #exponentiation 5
    elif selection == 5:
        operand1 = input("Enter first operand: ")
        if operand1 == 'RESULT':
            operand1 = result
        else:
            operand1 = float(operand1)

        operand2 = input("Enter second operand: ")
        if operand2 == 'RESULT':
            operand2 = result
        else:
            operand2 = float(operand2)
        result = math.pow(operand1, operand2)
        print(f"Current Result: {result}")
        totresult = totresult + result
        numcalc += 1

    #Log 6
    elif selection == 6:
        operand1 = input("Enter first operand: ")
        if operand1 == 'RESULT':
            operand1 = result
        else:
            operand1 = float(operand1)

        operand2 = input("Enter second operand: ")
        if operand2 == 'RESULT':
            operand2 = result
        else:
            operand2 = float(operand2)
        result = math.log(operand2, operand1)
        print(f"Current Result: {result}")
        totresult = totresult + result
        numcalc += 1

    #average 7
    elif selection == 7:

        if numcalc == 0:
            print("Error: No calculations yet to average!")
            continue
        else:
            print(f"Sum of calculations: {totresult:.2f}",)
            print("Number of calculations:", numcalc)
            print(f"Average of calculations: {(totresult / numcalc):.2f}")
            print("")
            continue
    else:
        print("Error: Invalid selection!\n")
        continue
    if selection != 0 or selection != 7:
        print("\nCalculator Menu\n---------------\n0. Exit Program")
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average\n")

#Lab 3 Scientific Calculator
import math
def square_root(a):
    try:
        if a < 0:
            raise ValueError("square root input must be non-negative")
        return math.sqrt(a)
    except ValueError as e:
        print(f"Error: {e}")

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


