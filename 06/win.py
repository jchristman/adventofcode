# ----------------------------------------------------------------------------------------------------------------------
# Advent of Code - Day 6
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

_input = [(re.findall('(toggle|off|on)', line)[0], tuple(map(tuple, map(lambda x: map(int, x.split(',')), re.findall('([0-9]+,[0-9]+)', line))))) for line in open('input', 'r').readlines()]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1 (find how many lights are lit)
# 
# This problem was a bit trickier than those previous. The strategy used here was run through all possible coordinates,
# generate a list of commands for each coordinate, then reduce the commands to a value based on a lambda function. If
# toggle, XOR the value at the coordinate with 1 to toggle state; if on, or the value with one to turn it on; if off,
# and the value with 0 to turn it off.
#
# The reduce function applies the lambda to a list in sequential pairs to reduce an iterator to a single value. For
# example, reduce(lambda x, y: x+y, [1,2,3,4]) becomes (((1 + 2) + 3) + 4). We can apply a similar strategy to a list
# like reduce(lambda_func, [0, 'on', 'toggle', 'off']) becomes (((0 | 1) ^ 1) & 0).
# ----------------------------------------------------------------------------------------------------------------------

print sum(reduce(lambda value, cmd: value ^ 1 if cmd == 'toggle' else value | 1 if cmd == 'on' else value & 0, [0] + [cmd for cmd,coords in _input if coords[0][0] <= i <= coords[1][0] and coords[0][1] <= j <= coords[1][1]]) for i in xrange(1000) for j in xrange(1000))


# ----------------------------------------------------------------------------------------------------------------------
# Part 2 (find the total brightness of the lights)
#
# The strategy here is the exact same as part 1, with different rules for each light.
# ----------------------------------------------------------------------------------------------------------------------

print sum(reduce(lambda value, cmd: max(value + 2 if cmd == 'toggle' else value + 1 if cmd == 'on' else value - 1, 0), [0] + [cmd for cmd,coords in _input if coords[0][0] <= i <= coords[1][0] and coords[0][1] <= j <= coords[1][1]]) for i in xrange(1000) for j in xrange(1000))
