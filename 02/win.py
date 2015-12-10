# ----------------------------------------------------------------------------------------------------------------------
# Advent of Code - Day 2
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

_input = [tuple(map(int, box.strip().split('x'))) for box in open('input', 'r').readlines()]

# ----------------------------------------------------------------------------------------------------------------------
# Part 1 (find the total square feet of wrapping paper needed)
# 
# Calculate the area of the box plus the smallest side extra. The reduce function here will multiply together all of the
# elements in a list, so we pass in the sorted list of the length width and height, slicing the first two elements out
# to give the dimensions of the smallest side of the box. Then sum up the result for all of the boxes
# ----------------------------------------------------------------------------------------------------------------------

print sum(2*l*w + 2*l*h + 2*w*h + reduce(lambda x, y: x*y, sorted([l,w,h])[:2]) for l,w,h in _input)



# ----------------------------------------------------------------------------------------------------------------------
# Part 2 (find the total length of ribbon required)
#
# This is almost the same problem as part 1. Find cubic volume of all of the boxes and add the smallest perimeter of
# the sides of the box. To do the second one, we just find the smallest side and multiply the sum of the sides by 2.
# ----------------------------------------------------------------------------------------------------------------------

print sum(l*w*h + reduce(lambda x, y: 2*(x+y), sorted([l,w,h])[:2]) for l,w,h in _input)
