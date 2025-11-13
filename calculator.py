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


