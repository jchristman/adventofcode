# ----------------------------------------------------------------------------------------------------------------------
# Advent of Code - Day 13
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
import re, itertools
_input = { name: { re.findall(r'[A-Z][a-z]+', line)[1]: int(re.findall(r'[0-9]+', line)[0]) if len(re.findall(r'lose', line)) == 0 else -int(re.findall(r'[0-9]+', line)[0]) for line in open('input', 'r').read().splitlines() if re.findall(r'[A-Z][a-z]+', line)[0] == name } for name in set(re.findall(r'[A-Z][a-z]+', open('input', 'r').read())) }

# ----------------------------------------------------------------------------------------------------------------------
# Part 1 (Find maximum happiness at a table)
# 
# Find the best combination of seats by iterating all permutations and calculating the happiness with a reduce func.
# ----------------------------------------------------------------------------------------------------------------------

print max((reduce(lambda first_total, second: (first_total[0] + [second], first_total[1] + _input[first_total[0][-1]][second] + _input[second][first_total[0][-1]]), [([arrangement[-1]], 0)] + list(arrangement)) for arrangement in itertools.permutations(_input.iterkeys())), key=lambda x: x[1])



# ----------------------------------------------------------------------------------------------------------------------
# Part 2 (Find maximum happiness at a table)
#
# Add myself into the table and print the best happiness
# ----------------------------------------------------------------------------------------------------------------------
_input = { name: { re.findall(r'[A-Z][a-z]+', line)[1]: int(re.findall(r'[0-9]+', line)[0]) if len(re.findall(r'lose', line)) == 0 else -int(re.findall(r'[0-9]+', line)[0]) for line in open('input2', 'r').read().splitlines() if re.findall(r'[A-Z][a-z]+', line)[0] == name } for name in set(re.findall(r'[A-Z][a-z]+', open('input2', 'r').read())) }

print max((reduce(lambda first_total, second: (first_total[0] + [second], first_total[1] + _input[first_total[0][-1]][second] + _input[second][first_total[0][-1]]), [([arrangement[-1]], 0)] + list(arrangement)) for arrangement in itertools.permutations(_input.iterkeys())), key=lambda x: x[1])
