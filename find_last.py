# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.


def find_last(a, b):
    last_pos = -1
    while True:
        pos = a.find(b, last_pos+1)
        if pos == -1:
            return last_pos
        last_pos = pos