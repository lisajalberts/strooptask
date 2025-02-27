import random
import matplotlib as plt


color_dict = {
   '\033[31m': 'r',  # red
   '\033[32m': 'g',  # green
   '\033[33m': 'y',  # yellow
   '\033[34m': 'b'   # blue
}


list_colours = ['blue', 'red', 'green', 'yellow']
random_colourtext = random.choice(list_colours)


# ANSI color codes for red, green, yellow, and blue
#033 is colour of text,, 31m is red etc
colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m']
random_colour = random.choice(colors)


trials = [1, 2, 3,4,5]
# loop for more random trials
for rounds in trials:
 random_colour = random.choice(colors)
 random_colourtext = random.choice(list_colours)
 print(f"{random_colour}{random_colourtext}\033[0m")# Randomly pick a color and print the text
 input_user = input("Which colour was the text? ").lower()# Get user input
 if input_user == color_dict[random_colour]:# Check if input matches the displayed color
     print("Correct!")
 else:
     print(f"Wrong! The correct answer was '{color_dict[random_colour].upper()}'")