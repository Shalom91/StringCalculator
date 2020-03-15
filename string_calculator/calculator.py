
import re

def add(text): 
    pattern = re.split("4|\n|a-z|777", text)
    x = r"\-*\d+"
    num_list = re.findall(x, str(pattern))
    num_list = [int(i) for i in num_list]
    addition = 0
    for i in num_list:
        if i < 0: 
            raise Exception("ERROR: Negatives not allowed " + ",".join(map(str, [i for i in num_list if i < 0])))
        elif i >= 1000: 
            pass
        else:
            addition += i
    return addition




