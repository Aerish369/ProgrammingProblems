# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the 
# digits of this number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]


def digitize(n):
    x = []
    for i in str(n):
        x.append(int(i))
    x.reverse()
    return x

#* Example Usecase:

print(digitize(2345))