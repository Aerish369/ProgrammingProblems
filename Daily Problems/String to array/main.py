# Write a function to split a string and convert it into an array of words.

# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]

# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

def string_to_array(s):
    a = []
    for i in s.split(' '): a.append(i) 
    return a


# Example usecase
print(string_to_array('Robin Chan is cutie'))

#useless