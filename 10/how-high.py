# ----------------------------------------------------------------------------------------------------------------------
# Advent of Code - Day 10
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
import re, sys
_input = '1113222113'

# ----------------------------------------------------------------------------------------------------------------------
# Part 1 (create new strings from look and say game 40 times)
# 
# Find each set of duplicated chars using regex and create new string from the length of the sequence and it's character
# ----------------------------------------------------------------------------------------------------------------------

print len((lambda lookandsay: (lambda func1, in1, current_depth1, target_depth1: func1(func1, in1, current_depth1, target_depth1))(lambda self, _in, current_depth, target_depth: _in if current_depth == target_depth else self(self, ''.join('%d%s' % (len(seq), seq[0]) for seq,trash in re.findall(r'((\d)\2*)', _in)), current_depth + 1, target_depth), lookandsay, 0, int(sys.argv[1])))(_input))
