# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

#I did this
def square_digits(num):
    num_str = str(num) #converting num(int) into str
    sq_list = [] #empty list to store squared num
    for i in num_str: #iterating i in num_str to get square of each digit
        j = int(i) * int(i) #concatinating str into int and squaring
        sq_list.append(j) #inserting the squares into the sq_list
    str_list = [str(num) for num in sq_list] #changing ints of str_list into string
    concatinatedList = ''.join(str_list) #joining all the strs of str_list
    return int(concatinatedList) # converting them to int
    
#chatgpt did this:
def square_digits(num):
    sq_list = [int(i) * int(i) for i in str(num)]  # Square each digit and store them in a list
    concatinatedList = ''.join(map(str, sq_list))  # Join the squared digits as strings
    return int(concatinatedList)  # Convert the concatenated string back to an integer