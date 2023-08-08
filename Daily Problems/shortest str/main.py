# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(s):
    x = s.split(' ')
    return len(min(x, key=len))




x = 'Aerish Apex Alok Kelly Sa Wukong Roronoa Zoro'

print(find_short(x))