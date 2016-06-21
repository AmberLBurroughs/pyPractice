# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# starts with either 'D' or 'N', but no one
# else.

def is_friend(name):
    return name[0] == "D" or name[0] == "N"