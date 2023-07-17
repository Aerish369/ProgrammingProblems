# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# Array can contain numbers or strings. X can be either.

#* Return true if the array contains the value, false if not.


def check(seq, elem):
    return True if elem in seq else False


#Example usecase:

print(check([1, 2, 3, 4], 5)) # Output False as 5 is not in the user given array.

print(check([1, 2, 3, 4], 3)) # Output True as 3 is in the user given array.


#! Pythonic way to execute the function

#! def check(seq, elem):
#!  return elem in seq