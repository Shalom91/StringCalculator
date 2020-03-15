# load modules
import re

# define the function
def add(text): 
    # split items and find integers: pattern, num_list
    pattern = re.split("4|\n|a-z|777", text)
    x = r"\-*\d+"
    num_list = re.findall(x, str(pattern))

    # convert list items into int
    num_list = [int(i) for i in num_list]

    # initialise placeholder for adding integers: addition
    addition = 0

    # add items in a list
    for i in num_list:
        if i < 0: # ---- negative numbers
            # use map() to convert each item in the list to a string, and then join them
            raise Exception("ERROR: Negatives not allowed " + ",".join(map(str, [i for i in num_list if i < 0])))
        elif i >= 1000: # ---- numbers equal to or greater than 1000
            pass
        else:
            addition += i
    return addition




