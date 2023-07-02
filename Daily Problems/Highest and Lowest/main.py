def highest_to_lowest(numbers):
    inting = [int(num) for num in numbers.split(' ')]
    highest = max(inting)
    lowest = min(inting)
    return str(highest) + " " + str(lowest)


#!I previously thought the function has to return all the numbers from highest to lowest.
#!While the question only asked about highest and lowest number
# def highest_to_lowest(numbers):
#     inting = [int(num) for num in numbers.split(' ')]
#     numbers = sorted(inting, reverse= True)
#     return numbers



x = highest_to_lowest('2 3 8 5 9')
print(x)
    
    
    
    
