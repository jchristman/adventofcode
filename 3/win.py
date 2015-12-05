# ----------------------------------------------------------------------------------------------------------------------
# Advent of Code - Day 3
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

_input = open('input', 'r').read().strip()

# ----------------------------------------------------------------------------------------------------------------------
# Part 1 (find the number of houses santa visited)
# 
# Find all of the coordinates visited by digesting each substring of the overall input, then find all of the unique
# points.
# ----------------------------------------------------------------------------------------------------------------------

print len(set([(_input[:i].count('>') - _input[:i].count('<'), _input[:i].count('^') - _input[:i].count('v')) for i in xrange(len(_input))] + [(0,0)]))



# ----------------------------------------------------------------------------------------------------------------------
# Part 2 (find the number of houses visited by santa and robosanta
#
# Same as the last one, but take slices of the input.
# ----------------------------------------------------------------------------------------------------------------------

print len(set([(_input[::2][:i].count('>') - _input[::2][:i].count('<'), _input[::2][:i].count('^') - _input[::2][:i].count('v')) for i in xrange(len(_input[::2]) + 1)] + [(_input[1::2][:i].count('>') - _input[1::2][:i].count('<'), _input[1::2][:i].count('^') - _input[1::2][:i].count('v')) for i in xrange(len(_input[1::2]) + 1)] + [(0,0)]))
