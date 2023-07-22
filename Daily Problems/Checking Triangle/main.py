# Implement a function that accepts 3 integer values a, b, c. 
# The function should return true if a triangle can be built with 
# the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).


def is_triangle(a, b, c):
    if a and b and c > 0:
        if a + b > c and b + c > a and c + a > b:
            return True
    return False


#* Example Usecase::

print(is_triangle(4, 1, 10)) # Output False
print(is_triangle(3, 7, -1)) # Output False
print(is_triangle(4, 7, 8)) # Output True 