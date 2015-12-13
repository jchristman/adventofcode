# ----------------------------------------------------------------------------------------------------------------------
# Advent of Code - Day 12
# 
# The Python One-Liner challenge:
# 
# Rules:
#
#   - Reading input into a variable from another file or with an assignment is acceptable and does not count against
#     your total for lines.
#   - Your solution must take the form of 'print INSERT_CODE_HERE'
#   - Formatting your print with a format string is acceptable so long as you are only substituting ONE value (multiple
#     calculations are not allowed)
#   - No global variables (outside of the input variable)
#
# ----------------------------------------------------------------------------------------------------------------------
import re, json, sys
_input = open('input', 'r').read()

# ----------------------------------------------------------------------------------------------------------------------
# Part 1 (sum all numbers in a json file)
# 
# Super easy cakes
# ----------------------------------------------------------------------------------------------------------------------

print sum(int(num) for num in re.findall(r'-?[0-9]+', _input))



# ----------------------------------------------------------------------------------------------------------------------
# Part 2 (sum all numbers not in an object where there is a property with value red)
#
# Recursively iterate through the json object, adding numbers where there is no red key
# ----------------------------------------------------------------------------------------------------------------------

print (lambda books: (lambda func, arg1: func(func, arg1))(lambda self, books: sum(int(int(num) if isinstance(num, int) else 0 if isinstance(num, unicode) else self(self, num)) for key, num in books.items()) if isinstance(books, dict) and not 'red' in books.itervalues() else sum(int(int(num) if isinstance(num, int) else 0 if isinstance(num, unicode) else self(self, num)) for num in books) , books))(json.loads(_input))
