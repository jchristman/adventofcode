# ----------------------------------------------------------------------------------------------------------------------
# Advent of Code - Day 8
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

_input = open('input', 'r').read().splitlines()

# ----------------------------------------------------------------------------------------------------------------------
# Part 1 (find length of lines minus escaped length of lines)
# 
# Sum the length of the lines and subtract the evaluated strings (which track the escape characters) lengths.
# ----------------------------------------------------------------------------------------------------------------------

print sum(len(line) for line in _input) - sum(len(eval(line)) for line in _input)



# ----------------------------------------------------------------------------------------------------------------------
# Part 2 (Escape some strings and substract original length)
#
# Same as part 1, but with a string replace.
# ----------------------------------------------------------------------------------------------------------------------

print sum(len('"%s"' % line.replace('\\','\\\\').replace('"', '\\"')) for line in _input) - sum(len(line) for line in _input)
