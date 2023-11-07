import numpy as np


def generate_route(stone_locations):
    # go to first location
    route_horizontal = [(i, 0) for i in range(stone_locations[0][0] + 1)]
    route_vertical = [(stone_locations[0][0], i) for i in range(stone_locations[0][1] + 1)]
    route = route_horizontal + route_vertical
    # filter duplicates
    route = list(dict.fromkeys(route))
    print(f"route number 1: {route}")
    complete_route = route
    for i in range(1, len(stone_locations)):
        steps_horizontal = stone_locations[i][0] - stone_locations[i-1][0]
        steps_vertical = stone_locations[i-1][1] - stone_locations[i][1]
        # check in what direction the robot needs to move horizontally
        if steps_horizontal > 0:
            route_horizontal = [(route[-1][0] + j, route[-1][1]) for j in range(1, steps_horizontal + 1)]
        elif steps_horizontal < 0:
            route_horizontal = [(route[-1][0] - j, route[-1][1]) for j in range(1, abs(steps_horizontal) + 1)]
        else:
            route_horizontal = []
        # if there is a horizontal route, start location is the last location in the horizontal route
        if len(route_horizontal) > 0:
            start_location = route_horizontal[-1]
        else:
            start_location = route[-1]

        # check in what direction the robot needs to move vertically
        if steps_vertical > 0:
            # +1 because the range function is exclusive
            route_vertical = [(start_location[0], start_location[1] - j) for j in range(1, steps_vertical + 1)]
        elif steps_vertical < 0:
            route_vertical = [(start_location[0], start_location[1] + j) for j in range(1, abs(steps_vertical) + 1)]
        else:
            route_vertical = []
        # partial_route is the horizontal route + the vertical route for 1 stone
        partial_route = route_horizontal + route_vertical
        print(f"route number {i+1}: {partial_route}")   
        complete_route += partial_route
    print(f"complete route: {complete_route}")
    print(f"amount of steps taken {len(complete_route)}")
    return complete_route

def return_emoji(cell):
    """ function for printing the moon pretty using emoji's for rocks and robot """
    if cell == 1:
        return "🌑"
    elif cell == 2:
        return "🧑"
    else:
        return "🌕"
def pretty_print_moon(moon):
    for row in moon:
        line = [return_emoji(cell) for cell in row]
        print(" ".join(line))
# create menu
# 1. ask for moon size
# 2. ask for amount of stones (should be max 2/3 of moon_size**2)
# 3. ask for for robot type
# 4. ask for printing type (fine or path)

def ask_moon_size():
    print("What size moon do you want to search?")
    print("A number can be between 5 and 10 (inclusive)")
    moon_size = input("Please enter a number for the moon size (between 5 and 10 inclusive): ")
    while not moon_size.isnumeric() or not 5 <= int(moon_size) <= 10:
        moon_size = input("Please enter a valid number between 5 and 10 (inclusive): ")
    return moon_size
def ask_stones(moon_size):
    print("How many stones do you want to place on the moon?")
    print(f"The range of  stones is [1,{int(moon_size**2 * 2/3)}]")
    amount_of_stones = input("Please enter a number for the amount of stones: ")
    while not amount_of_stones.isnumeric() or not 1 <= int(amount_of_stones) <= moon_size**2 * 2/3:
        amount_of_stones = input("Please enter a valid number: ")
    return amount_of_stones

def walk(moon, step):
    # look where the robot (2) stands and put it to 0
    robot_location = np.argwhere(moon == 2)
    if len(robot_location) > 1:
        # switch x and y coordinates
        robot_location = robot_location[:, [1, 0]]
        # set it to 0
        moon[robot_location[0][1]][robot_location[0][0]] = 0 

     # on coordinate (x,y) there is a stone
     # set step coordinate to 0 (remove stone) and return new moon
    moon[step[1]][step[0]] = 2
    return moon
def main():
    print("Welcome to the moon robot program!")
    moon_size = ask_moon_size()
    print(f"You have chosen a moon of size {moon_size}")
    amount_of_stones = ask_stones(int(moon_size))
    moonSize, moon = get_moon(moon_size, amount_of_stones)
    stone_locations = np.argwhere(moon == 1)
    # switch x and y coordinates
    stone_locations = stone_locations[:, [1, 0]]
    complete_route = generate_route(stone_locations)
    fine_print = input("Do you want to see the fine print? (y/n): ")
    if fine_print.lower() == "y":
        for step in complete_route:
            moon_copy = moon.copy()
            # add Person to the current location
            moon_copy = walk(moon_copy, step)
            moon_copy[step[1]][step[0]] = 2
          
            pretty_print_moon(moon_copy)
            # Emoticons are 'longer' than 1 dash so we need +2 at the end
            print("-"*(len(moon_copy)*3+2))


def get_moon(moonSize="8", number_of_stones="2"):
	# Check that moon size is an integer
	if moonSize.isnumeric():

		# Convert to integer
		moonSize = int(moonSize)

		# Check that moon size is between 5 and 10
		if 5 <= moonSize <= 10:
			# check if number_of_stones is an integer
			if not number_of_stones.isnumeric():
				return
			# Convert to integer
			number_of_stones = int(number_of_stones)
			# check if it is between 0 and moonSize^2 * 2/3
			if not 0 <= number_of_stones <= moonSize * moonSize * 2/3:
				return
			# Create a 1D NumPy array with the correct number of stones and empty spots
			moon = np.array([0] * (moonSize * moonSize - number_of_stones) + [1] * number_of_stones)
			# Shuffle the array to randomise the locations of the stones
			np.random.shuffle(moon)
			# Convert to square 2D array to have a square moon surface
			moon = np.reshape(moon, (-1, moonSize))
			# Return the moon size and the generated moon surface
			return moonSize, moon

		else:
			# If moon size is too small or too large, rerun function to get new input
			print("Your input was too large or too small")

	else:
		# If moon size is not an integer, rerun function to get new input
		print("Your input was not an integer.")


if __name__ == "__main__":
	main()