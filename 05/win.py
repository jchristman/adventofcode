# ----------------------------------------------------------------------------------------------------------------------
# Advent of Code - Day 5
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
import re
_input = [line.strip() for line in open('input', 'r').readlines()]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1 (find the number of nice strings)
# 
# Use regular expressions to find 3 vowels, a repeated character, and none of ab, cd, pq, and xy
# ----------------------------------------------------------------------------------------------------------------------

print len([word for word in _input if len(re.findall('[aeiou]', word)) > 2 and len(re.findall('(.)\\1', word)) > 0 and len(re.findall('(ab|cd|pq|xy)', word)) == 0])



# ----------------------------------------------------------------------------------------------------------------------
# Part 2 (find the number of nice strings
#
# Use regular expressions to find a double string repeated twice in the string and a repeated letter with one char 
# between them
# ----------------------------------------------------------------------------------------------------------------------

print len([word for word in _input if len(re.findall('(..).*\\1', word)) > 0 and len(re.findall('(.).\\1', word)) > 0])
