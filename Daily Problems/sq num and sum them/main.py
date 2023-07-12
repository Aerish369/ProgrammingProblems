# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 
# 1^2 + 2^2 + 2^2 = 9

def square_sum(numbers):
    sq = [i*i for i in numbers]
    return sum(sq)
    

#Example Usecase

print(square_sum([1, 2, 3, 4])) #Output 30