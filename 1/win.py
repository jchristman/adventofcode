# ----------------------------------------------------------------------------------------------------------------------
# Advent of Code - Day 1
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
# Part 1 (find the total floor)
# 
# This is fairly self explanatory: sum all of the characters in the input, using a 1 for ( and a -1 otherwise
# ----------------------------------------------------------------------------------------------------------------------

print sum(1 if x == '(' else -1 for x in _input)



# ----------------------------------------------------------------------------------------------------------------------
# Part 2 (find the first character that hits the basement)
#
# To get this in one line required some thinking about the problem. Python does not allow you to do assignments
# inside of a loop, so you can't just keep a counter, incrementing and decrementing while testing every iteration
# of the loop to see if it is -1. So instead, I represent the problem in a different way.
#
# If you create a list (using a list comprehension) of all of the indices of '(' and a second one of all of the
# indices of ')', I can iterate through the two lists in parallel and know the first time that I have ')' with a
# smaller index than its paired '(', I have subtracted 1 more than I have gained and I am negative. Think of this
# with the following toy problem:
#          
#          v--------------------- here is the answer (7)
#   '(())())(()'
#   left  = [0, 1, 4, 7, 8]
#   right = [2, 3, 5, 6, 9]
#                     ^---------- here is where we go negative, at index 3
#
# We are essentially consuming one '(' and one ')' at a time, walking down these two lists. As soon as I consume a
# ')' before a '(' because its index is less, then this is the spot where we have gone negative and into the basement.
# In the above example, the right index is less than the left index at spot 3 in the arrays. Since we are consuming 
# two tokens at a time and the answer must always be odd (think about this on your own), we multiply by two and add one.
#
# Therefore the code can be represented by a one-liner, which I will let you dissect on your own!
# ----------------------------------------------------------------------------------------------------------------------

print [k for k,z in enumerate(zip([i for i,x in enumerate(list(_input)) if x == '('] + [-1]*(len(_input) - _input.count('(')), [j for j,y in enumerate(list(_input)) if y == ')'] + [-1]*(len(_input) - _input.count(')')))) if z[1] < z[0]][0] * 2 + 1
