def proceed():
	user_choice = input("Would you like to continue? ")
	if user_choice == "yes":
		return True
	return False


def get_first_name():
	while True:
		if not proceed():
			return "exit"
		first_name = input("What is your first name? ")
		return first_name


def get_last_name():
	while True:
		if not proceed():
			return "exit"
		last_name = input("What is your last name? ")
		return last_name


def get_age():
	while True:
		if not proceed():
			return "exit"
		age = input("What is your age? ")
		return age


def get_citizenship():
	while True:
		if not proceed():
			return "exit"
		citizenship = input("Are you a U.S. Citizen? ")
		return citizenship


def get_state():
	while True:
		if not proceed():
			return "exit"
		state = input("What state do you live in? ")
		return state


def get_zipcode():
	while True:
		if not proceed():
			return "exit"
		zipcode = input("What is your zipcode? ")
		return zipcode
