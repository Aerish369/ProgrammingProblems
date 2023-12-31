# Check to see if a string has the same amount of 'x's and 'o's. 
# The method must return a boolean and be case insensitive. 
# The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false


def xo(s):
    num_x = s.lower().count('x')
    num_o = s.lower().count('o')
    return num_x == num_o #! Alternative way with less code

    #? This is usual method. It is replaced by the code in line 17.
        # if (num_x == num_o):
        #     return True
        # else:
        #     return False
    
#Example usecase:

a = xo('xOoooxXXxO')
print(a)

#I learned how to make any string case insensitive. 
#It is by using .lower() function to make all chars lowers
#and it applies same for every char of str.  