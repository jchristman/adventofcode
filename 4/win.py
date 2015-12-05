# ----------------------------------------------------------------------------------------------------------------------
# Advent of Code - Day 4
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

import hashlib, itertools
_input = 'iwrupvqb'

# ----------------------------------------------------------------------------------------------------------------------
# Part 1 (find an md5 that starts with all 0's as first 5 characters
# 
# Count up until we find the hash
# ----------------------------------------------------------------------------------------------------------------------

print next(i for i in itertools.count() if hashlib.md5(_input + str(i)).hexdigest()[:5] == '00000')



# ----------------------------------------------------------------------------------------------------------------------
# Part 2 (find an md5 that starts with all 0's as first 6 characters)
#
# Count up until we find the hash
# ----------------------------------------------------------------------------------------------------------------------

print next(i for i in itertools.count() if hashlib.md5(_input + str(i)).hexdigest()[:6] == '000000')
