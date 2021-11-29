import numpy as np
import re

print("*******************************Welcome to the Python Matrix Application*******************")
while True:
    print("Do you want to play the Matrix Game?")
    # Reading the choice
    choice = input("Enter Y for yes or N for No:")
    if choice == "N":
        print("****************Thanks for playing Python Numpy************************")
        break
    else:
        while True:
            phone = input("Enter your phone number(XXX-XXX-XXXX):")
            # Regular expression for checking the phone number format
            if not re.match("\d{3}-\d{3}-\d{4}", phone):
                print("Your phone number is not in correct format. Please reenter:")
            else:
                break
        while True:
            zip = input("Enter your zipcode+4(XXXXX-XXXX):")
            # Regular expression for checking the zipcode format
            if not re.match("\d{5}-\d{4}", zip):
                print("Your zipcode is not in correct format. Please reenter:")
            else:
                break
        # Reading the first matrix
        print("Enter your first 3x3 matrix:")
        a = []
        for i in range(3):
            # Reading row by row
            row = input().split()
            # Converting each element to integer
            row = list(map(int, row))
            # Adding row to the matrix
            a.append(row)
        # Printing first matrix
        print("Your first 3x3 matrix is:")
        for i in range(3):
            for j in range(3):
                print(a[i][j], end=" ")
            print()
        # Reading second matrix
        print("Enter your second 3x3 matrix:")
        b = []
        for i in range(3):
            # Reading row by row
            row = input().split()
            # Converting each element to integer
            row = list(map(int, row))
            # Adding row to the matrix
            b.append(row)
        # Printing second matrix
        print("Your second 3x3 matrix is:")
        for i in range(3):
            for j in range(3):
                print(a[i][j], end=" ")
            print()
        # Menu for matrix operations
        print("Select a Matrix Operation from the list below:")
        print("a. Addition")
        print("b. Subtraction")
        print("c. Matrix Multiplication")
        print("d. Element by element multiplication")
        ch = input()
        if ch == "a":
            print("You selected Addition. The results are:")
            # converting list to numpy arrays
            a = np.array(a)
            b = np.array(b)
            # addition of matrices
            c = a + b
            for i in range(3):
                for j in range(3):
                    print(c[i][j], end=" ")
                print()
            print("The Transpose is:")
            # function for finding the transpose
            t = np.transpose(c)
            for i in range(3):
                for j in range(3):
                    print(t[i][j], end=" ")
                print()
            print("The row and column mean values of the results are:")
            # Function mean with axis =1 finds row means
            print("Row:", np.mean(c, axis=1))
            # Function mean with axis =0 finds column means
            print("Column:", np.mean(c, axis=0))

        if ch == "b":
            print("You selected Subtraction. The results are:")
            a = np.array(a)
            b = np.array(b)
            # subtraction of matrices
            c = a - b
            for i in range(3):
                for j in range(3):
                    print(c[i][j], end=" ")
                print()
            print("The Transpose is:")
            # function for finding the transpose
            t = np.transpose(c)
            for i in range(3):
                for j in range(3):
                    print(t[i][j], end=" ")
                print()
            print("The row and column mean values of the results are:")
            # Function mean with axis =1 finds row means
            print("Row:", np.mean(c, axis=1))
            # Function mean with axis =0 finds column means
            print("Column:", np.mean(c, axis=0))

        if ch == "c":
            print("You selected Matrix Multiplication. The results are:")
            # For getting matrix multiplication use the function matrix instead of array in numpy
            a = np.matrix(a)
            b = np.matrix(b)
            c = a * b
            c = np.array(c)
            for i in range(3):
                for j in range(3):
                    print(c[i][j], end=" ")
                print()
            print("The Transpose is:")
            # function for finding the transpose
            np.transpose(c)
            for i in range(3):
                for j in range(3):
                    print(t[i][j], end=" ")
                print()
            print("The row and column mean values of the results are:")
            # Function mean with axis =1 finds row means
            print("Row:", np.mean(c, axis=1))
            # Function mean with axis =0 finds column means
            print("Column:", np.mean(c, axis=0))

        if ch == "d":
            print("You selected Element by Element Multiplication. The results are:")
            a = np.array(a)
            b = np.array(b)
            # Elementary wise multiplication
            c = a * b
            for i in range(3):
                for j in range(3):
                    print(c[i][j], end=" ")
                print()
            print("The Transpose is:")
            # function for finding the transpose
            t = np.transpose(c)
            for i in range(3):
                for j in range(3):
                    print(t[i][j], end=" ")
                print()
            print("The row and column mean values of the results are:")
            # Function mean with axis =1 finds row means
            print("Row:", np.mean(c, axis=1))
            # Function mean with axis =0 finds column means
            print("Column:", np.mean(c, axis=0))
