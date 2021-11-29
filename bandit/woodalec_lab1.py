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
        try:
            age = int(input("How old are you? "))
            if age < 18:
                age_1 = input("Are you 18 years or older? ")
                if age_1 == "no":
                    return -1
            elif 120 >= age >= 18:
                return age
        except ValueError:
            pass


def get_citizenship():
    while True:
        if not proceed():
            return "exit"
        citizenship = input("Are you a U.S. Citizen? ")
        if citizenship == "yes":
            return "yes"


def get_state():
    while True:
        if not proceed():
            return "exit"
        state = input("What state do you live in? Please enter two letter abbreviation ")
        if len(state) == 2:
            return state


def get_zipcode():
    while True:
        if not proceed():
            return -1
        try:
            zipcode = input("What is your zipcode? ")
            if len(zipcode) == 5:
                return zipcode
        except ValueError:
            pass


if __name__ == "__main__":
    print("Welcome to the Python Voter Registration Application.")
    VOTER_INFO = []

    while True:
        FIRST = get_first_name()
        if FIRST == "exit":
            break
        VOTER_INFO.append(FIRST)

        LAST = get_last_name()
        if LAST == "exit":
            break
        VOTER_INFO.append(LAST)

        AGE = get_age()
        if AGE == -1:
            break
        VOTER_INFO.append(AGE)

        CITIZENSHIP = get_citizenship()
        if CITIZENSHIP in ("exit", "no"):
            break
        VOTER_INFO.append("yes")

        STATE = get_state()
        if STATE == "exit":
            break
        VOTER_INFO.append(STATE)

        ZIPCODE = get_zipcode()
        if ZIPCODE == -1:
            break
        VOTER_INFO.append(ZIPCODE)

        if len(VOTER_INFO) == 6:
            print("Voter info:")
            print("Name: ", VOTER_INFO[0] + " " + VOTER_INFO[1])
            print("Age: ", VOTER_INFO[2])
            print("U.S. Citizen: ", VOTER_INFO[3])
            print("State: ", VOTER_INFO[4])
            print("Zipcode: ", VOTER_INFO[5])
