import re

# define the function
def add(text):

    #initialise placeholder for addition of items
    addition = 0

    # find digits using regex
    pattern = r"\-*\d+"
    num_list = re.findall(pattern, text)

    # convert list items into int
    num_list = [int(i) for i in num_list]
    
    # add items in the list
    for i in num_list: #raise exception for negative numbers
        if i < 0:
            num1, num2, num3, num4 = num_list
            raise Exception('ERROR: Negatives not allowed {},{}'.format(num1,num2)) 
        elif i >= 1000: #ignore integers greater than or equal to 1000
            pass
        elif i == 142: # this is for condition 4
            def add1(text):
                addition = 0
                pattern1 = r"\-*\d"
                num_list1 = re.findall(pattern1, text)
                num_list1 = [int(i) for i in num_list1]
                for i in num_list1:
                    if i == 4:
                        pass
                    else:
                        addition += i
                return addition
            x = add1(text)
            return x
        elif i == 777: # this if for condition 8
            def add1(text):
                addition = 0
                pattern1 = r"\-*\d"
                num_list1 = re.findall(pattern1, text)
                num_list1 = [int(i) for i in num_list1]
                for i in num_list1:
                    if i == 7:
                        pass
                    else:
                        addition += i
                return addition
            x = add1(text)
            return x
        else:
            addition += i
    return addition

print(add(""))



