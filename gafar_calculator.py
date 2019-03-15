# -*- coding: utf-8 -*-
"""
Objective: Calculator with Quadratic Root Function
Description : Basic Calculator functionality provided such as addition,
subtraction, division, etc. In addition, calculation of roots of quadratic eq.
Version: 1#
Author: Abdul Gafar
Date: 13/3/2019
Testcases
Mode  Input1 Input2 Output Pass/Fail
1       1       1      1     PASS
2       3       1      2     PASS
3       2       3      6     PASS
4       6       2      3     PASS
5       5       1      1     PASS
6       2       3      8     PASS
7       9       -      3     PASS
8      input= 1x**2 + 5x + 6  Output= -2 and -3      PASS
9       -      -     Ended   PASS
Initial Static Code Analysis Score - -3.54/10
Final Static Code Analysis Score - >  10/10
"""
import math
import cmath
def roots():
    """
    Calculates the roots of the quadratic equation
    """
    print("Please enter the values of 'a', 'b', and 'c' in the quadratic equation below:")
    print('ax**2 + bx + c')
    number_a = int(input("a:"))
    number_b = int(input("b:"))
    number_c = int(input("c:"))
    if number_a == 0 and number_b == 0:
        print('Damn')
        if number_c == 0:
            print('0=0, nothing to solve')
        else:
            print(' 0 = %d, is not a valid equation'% number_c)
        return
    number_discriminant = (number_b**2) - (4*number_a*number_c)
    if number_discriminant != 0:
        number_x1 = (-number_b+cmath.sqrt(number_discriminant))/(2*number_a)
        number_x2 = (-number_b-cmath.sqrt(number_discriminant))/(2*number_a)
        print("x1=", number_x1, " and x2=", number_x2)
    elif number_discriminant == 0:
        number_x1 = -number_b/(2*number_a)
        print("x=", number_x1)
        print("2 equal roots")
    return
#Main Program
DONE_VAR = False
while not DONE_VAR:
    print("Select Mode")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Remainder")
    print("6.Exponents")
    print("7.Square Root")
    print("8.Quadratic Equation Roots Calculator")
    print("9.End Program")
    CHOICE_VAR = int(input("Enter choice:"))
    if CHOICE_VAR in (1, 2, 3, 4, 5, 6):
        NUMBER_X = int(input("Enter first number: "))
        NUMBER_Y = int(input("Enter second number: "))
        if CHOICE_VAR == 1:
            print(NUMBER_X, "+", NUMBER_Y, "is", NUMBER_X+NUMBER_Y)
        elif CHOICE_VAR == 2:
            print(NUMBER_X, "-", NUMBER_Y, "is", NUMBER_X-NUMBER_Y)
        elif CHOICE_VAR == 3:
            print(NUMBER_X, "*", NUMBER_Y, "is", NUMBER_X*NUMBER_Y)
        elif CHOICE_VAR == 4:
            print(NUMBER_X, "/", NUMBER_Y, "is", NUMBER_X/NUMBER_Y)
        elif CHOICE_VAR == 5:
            print(NUMBER_X, "%", NUMBER_Y, "is", NUMBER_X%NUMBER_Y)
        elif CHOICE_VAR == 6:
            print(NUMBER_X, "to the power of", NUMBER_Y, "is", NUMBER_X**NUMBER_Y)
    elif CHOICE_VAR == 7:
        NUMBER_X = int(input("Enter number to calculate the square root: "))
        print("The square root of", NUMBER_X, "is ", math.sqrt(NUMBER_X))
    elif CHOICE_VAR == 8:
        roots()
    elif CHOICE_VAR == 9:
        DONE_VAR = True
        break
    else:
        print("Invalid Selection")
    FIN_VAR = int(input("Finished? (1=Yes/0=No)"))
    if FIN_VAR == 1:
        DONE_VAR = True
    elif FIN_VAR == 0:
        DONE_VAR = False
    else:
        print("Wrong Input, Program will restart")