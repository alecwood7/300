"""
Alec Wood
10/21/21
Discussion 1
"""


#Define y as base starting number.
#Define x as user input, selecting a number to count up to.
#While statement start with y base and adds 1 each loop until it counts to x.
#Once counting is complete, program states bellow message

Y = 0
while True:
    try:
        X = int(input("Let's play hide and seek. Enter a number to count to: "))
        break
    except ValueError:
        print("Please enter a number")

while Y <= X:
    print(Y)
    Y = Y+1

print("Ready or not, here I come!")
