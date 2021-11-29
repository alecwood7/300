"""System module."""
import sys
from operator import itemgetter
import matplotlib.pyplot as plt

state = [['Alabama', 'Montgomery', 4887681, 'Camellia'],
         ['Alaska', 'Juneau', 735139, 'Forget-Me-Not'],
         ['Arizona', 'Phoenix', 7158024, 'Suguaro Cactus Blossom'],
         ['Arkansas', 'Little Rock', 3009733, 'Apple Blossom'],
         ['California', 'Sacramento ', 39461588, 'Golden Poppy'],
         ['Colorado', 'Denver', 5691287, 'Mountain Columbine'],
         ['Connecticut', 'Hartford', 3571520, 'Mountain Laurel'],
         ['Delaware', 'Dover', 965479, 'Peach Blossom'],
         ['Florida', 'Tallahassee', 21244317, 'Orange Blossom'],
         ['Georgia', 'Atlanta', 10511131, 'Cherokee Rose'],
         ['Hawaii', 'Honolulu', 1420593, 'Red Hibiscus'],
         ['Idaho', 'Boise', 1750536, 'Syringa'],
         ['Illinois', 'Springfield', 12723071, 'Violet'],
         ['Indiana', 'Indianapolis', 6695497, 'Peony'],
         ['Iowa', 'Des Moines', 3148618, 'Wild Rose'],
         ['Kansas', 'Topeka', 2911359, 'Sunflower'],
         ['Kentucky', 'Frankfort', 4461153, 'Goldenrod'],
         ['Louisiana', 'Baton Rouge', 4659790, 'Magnolia'],
         ['Maine', 'Augusta', 1339057, 'Pine Cone & Tassel'],
         ['Maryland', 'Annapolis', 6035802, 'Black-eyed Susan'],
         ['Massachusetts', 'Boston', 6882635, 'Mayflower'],
         ['Michigan', 'Lansing', 9984072, 'Apple Blossom'],
         ['Minnesota', 'St.Paul', 5606249, 'Lady-Slipper'],
         ['Mississippi', 'Jackson', 2981020, 'Magnolia'],
         ['Missouri', 'Jefferson City', 6121623, 'Hawthorne'],
         ['Montana', 'Helena', 1060665, 'Bitterroot'],
         ['Nebraska', 'Lincoln', 1925614, 'Goldenrod'],
         ['Nevada', 'Carson City', 3027341, 'Sagebrush'],
         ['New Hampshire', 'Concord', 1353465, 'Purple Lilac'],
         ['New Jersey', 'Trenton', 8886025, 'Violet'],
         ['New Mexico', 'Santa Fe', 2092741, 'Yucca'],
         ['New York', 'Albany', 19530351, 'Rose'],
         ['North Carolina', 'Raleigh', 10381615, 'Flowering Dogwood'],
         ['North Dakota', 'Bismark', 758080, 'Prairie Rose'],
         ['Ohio', 'Columbus', 11676341, 'Scarlet Carnation'],
         ['Oklahoma', 'Oklahoma City', 3940235, 'Mistletoe'],
         ['Oregon', 'Salem', 4181886, 'Oregon Grape'],
         ['Pennsylvania', 'Harrisburg', 12800922, 'Mountain Laurel'],
         ['Rhode Island', 'Providence', 1058287, 'Violet'],
         ['South Carolina', 'Columbia', 5084156, 'Yellow Jessamine'],
         ['South Dakota', 'Pierre', 878698, 'Pasque flower'],
         ['Tennessee', 'Nashville', 6771631, 'Iris'],
         ['Texas', 'Austin', 28628666, 'Bluebonnet'],
         ['Utah', 'Salt Lake City', 3153550, 'Sego Lily'],
         ['Vermont', 'Montpelier', 624358, 'Red Clover'],
         ['Virginia', 'Richmond', 8501286, 'Dogwood'],
         ['Washington', 'Olympia', 7523869, 'Coast Rhododendron'],
         ['West Virginia', 'Charleston', 1803291, 'Rhododendron'],
         ['Wisconsin', 'Madison', 5807406, 'Wood Violet'],
         ['Wyoming', 'Cheyenne', 577601, 'Indian Paintbrush']]

state.sort()


def get_sorted_states():
    """Sorts states alphabetically"""
    for i in range(0, 50):
        print("State: ", state[i][0], "//Capital: ", state[i][1],
              "//Population: ", state[i][2], "//Flower: ",
              state[i][3])


def get_search_display():
    """Search particular state"""
    state_name = input('Input your State: ')
    for i in range(0, 50):
        if state_name == (state[i][0]):
            print("State: ", state[i][0], "//Capital: ", state[i][1],
                  "//Population: ", state[i][2], "//Flower: ",
                  state[i][3])

        if i == 51:
            print("Invalid State Name")


def get_bar_graph():
    """Produces bar graph by sorting state list by highest population.
    Next, the program will pull first 5 sub-list's to new list.
    Last, two separate lists, state and population are created"""
    pop_list = sorted(state, key=itemgetter(2), reverse=True)
    top_list = pop_list[:5]
    top_state = [ele[0] for ele in top_list]
    top_pop = [ele[2] for ele in top_list]
    plt.bar(top_state, top_pop)
    plt.title('Highest Population states')
    plt.xlabel('State')
    plt.ylabel('Population')
    plt.show()


def get_update_state():
    """Calls particular sub-list and allows user to update only the population"""
    state_name = input('Input your State you would like to update: ')
    new_pop = int(input('New population value: '))
    for i in range(0, 50):
        if state_name == (state[i][0]):
            state[i][2] = new_pop


if __name__ == "__main__":

    USER_INPUT = 1
    while True:
        print('1. Display all U.S. States in Alphabetical '
              'order along with the Capital, State Population, and Flower '),
        print('2. Search for a specific state and display '
              'the appropriate Capital name, State Population, and an image\
of the associated State Flower. '),
        print('3. Provide a Bar graph of the top 5 '
              'populated States showing their overall population '),
        print('4. Update the overall state population for a specific state. '),
        print('5. Exit the program '),
        USER_INPUT = int(input('Please select one of the above: '))

        if USER_INPUT == 1:
            get_sorted_states()

        elif USER_INPUT == 2:
            get_search_display()

        elif USER_INPUT == 3:
            get_bar_graph()

        elif USER_INPUT == 4:
            get_update_state()

        elif USER_INPUT == 5:
            print("Thank you for coming, goodbye!")
            sys.exit()

        else:
            print('Please only enter a value between 1 and 5')
