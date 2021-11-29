# Imported modules
import secrets
import string
from datetime import date
import math


def get_password(x, option): #Define password function
	if option == 1: #Creates very strict password
		print(secrets.token_urlsafe(x))
	elif option == 2: #Creates password with less constraints
		alphabet = string.ascii_letters + string.digits
		password = ''.join(secrets.choice(alphabet) for i in range(x))
		print(password.lower())
	elif option == 3: #Creates password with only letters
		letters = string.ascii_letters
		print(''.join(secrets.choice(letters) for i in range(x)))


def get_percentage(num, den, dec): #Define percentage function
	percentage = (num / den)*100
	percentage = round(percentage, dec)
	print(percentage)


def get_date(): #Define function to get number of days
	today = date.today()
	set_date = date(2025, 7, 4)
	delta = set_date - today
	print(delta.days)


def get_cosine(side_a, side_b, angle): #Define the law of cosine function
	a = (side_a**2)+(side_b**2)
	b = 2 * side_a * side_b * math.cos(angle)
	c = a - b
	side_c = math.sqrt(c)
	print("{:.2f}".format(side_c))


def get_cylinder(r, height): #define cylinder volume function
	volume = ((r**2)*math.pi)*height
	print("{:.2f}".format(volume))

	
if __name__ == "__main__":

	while True: #While loop that reruns menu continuously until option 6 is selected.
		print("1: Generate Secure Password")
		print("2: Calculate and Format a Percentage")
		print("3: How many days from today until July 4, 2025?")
		print("4: Use the Law of Cosines to calculate the leg of a triangle")
		print("5: Calculate the volume of a Right Circular Cylinder")
		print("6: Exit")
		menu_choice = int(input("Please select from the menu above: "))
		
		if menu_choice == 1:
			print("1: Very complex(Num/Uppercase/Lowercase)")
			print("2: Medium complexity(Num/Lowercase)")
			print("3: low complexity(Uppercase/Lowercase)")
			option = int(input("Select complexity: "))
			x = int(input("How many characters? "))
			get_password(x, option)
		elif menu_choice == 2:
			print("to calculate percentage, you'll need to enter numerator, denominator and decimal point you want to round to.")
			num = int(input("Numerator: "))
			den = int(input("Denominator: "))
			dec = int(input("Decimal point: "))
			get_percentage(num, den, dec)
		elif menu_choice == 3:
			get_date()
		elif menu_choice == 4:
			side_a = int(input("Side a: "))
			side_b = int(input("Side b: "))
			angle = int(input("Angle: "))
			get_cosine(side_a, side_b, angle)
		elif menu_choice == 5:
			r = int(input("Radius: "))
			height = int(input("Height: "))
			get_cylinder(r, height)
		elif menu_choice == 6:
			print("Thank you for coming, goodbye!")
			break
		else:
			print("Invalid selection made, please choose again.")
