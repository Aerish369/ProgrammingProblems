#Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
# No floats or non-positive integers will be passed.

#For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

#[10, 343445353, 3453445, 3453545353453] should return 3453455.

#Func::

def sum_two_smallest_numbers(numbers):
    sort = sorted(numbers)
    return sort[0] + sort[1]

#Example use case:

odds = [3, 1, 9, 5, 7]
x = sum_two_smallest_numbers(odds)
print(x)