"""Wood, Alec - Lab 5"""
import pandas
import matplotlib.pyplot as mat

x = int(input("Select the file you want to analyze:\n 1. Population Data\n "
              "2. Housing Data\n 3. Exit Program "))

while True:
    if x == 1:
        population_change = pandas.read_csv("PopChange.csv")
        user_input = int(input("You have entered Population Data.\n "
                               "Select the column you want to analyze"
                               "\n 1. Pop Apr 1\n 2. Pop Jul 1\n 3. Change Pop\n 4. Exit Column"))
        if user_input == 1:
            pop_selected = population_change[["Pop Apr 1"]]
            pop_selected.hist(bins=50, figsize=(20, 15))
            mat.show()
            print(pop_selected.describe())
        elif user_input == 2:
            pop_selected = population_change[["Pop Jul 1"]]
            pop_selected.hist(bins=50, figsize=(20, 15))
            mat.show()
            print(pop_selected.describe())
        elif user_input == 3:
            pop_selected = population_change[["Change Pop"]]
            pop_selected.hist(bins=50, figsize=(20, 15))
            mat.show()
            print(pop_selected.describe())
        elif user_input == 4:
            break
        else:
            print("Invalid selection")
    if x == 2:
        housing = pandas.read_csv("Housing.csv")
        user_input = int(input("You have entered housing.\n "
                               "Select the column you want to analyze.\n"
                               "1. Age\n 2. Bedrooms\n 3. Built\n 4. Rooms\n 5. Utility\n 6. Exit"))
        if user_input == 1:
            housing_selected = housing[["AGE"]]
            housing_selected.hist(bins=50, figsize=(20, 15))
            mat.show()
            print(housing_selected.describe())
        elif user_input == 2:
            housing_selected = housing[["BEDRMS"]]
            housing_selected.hist(bins=50, figsize=(20, 15))
            mat.show()
            print(housing_selected.describe())
        elif user_input == 3:
            housing_selected = housing[["BUILT"]]
            housing_selected.hist(bins=50, figsize=(20, 15))
            mat.show()
            print(housing_selected.describe())
        elif user_input == 4:
            housing_selected = housing[["ROOMS"]]
            housing_selected.hist(bins=50, figsize=(20, 15))
            mat.show()
            print(housing_selected.describe())
        elif user_input == 5:
            housing_selected = housing[["UTILITY"]]
            housing_selected.hist(bins=50, figsize=(20, 15))
            mat.show()
            print(housing_selected.describe())
        elif user_input == 6:
            break
        else:
            print("Invalid selection")
    elif x == 3:
        break
    else:
        print("Invalid selection")
