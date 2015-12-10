# ----------------------------------------------------------------------------------------------------------------------
# Advent of Code - Day 9
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
_input = { place: { place2: int(re.findall('([\d]+)', line)[0]) for place2 in set([re.findall('([\w]+)(?= to)', line)[0] for line in open('input', 'r').read().splitlines()] + ['Arbre']) for line in open('input', 'r').read().splitlines() if re.findall('([\w]+)(?= =)', line)[0] in [place, place2] and re.findall('([\w]+)(?= to)', line)[0] in [place, place2] } for place in set([re.findall('([\w]+)(?= to)', line)[0] for line in open('input', 'r').read().splitlines()] + ['Arbre']) }

# ----------------------------------------------------------------------------------------------------------------------
# Part 1 (find shortest path from one point to another touching all points)
# 
# This is a hamiltonian path problem, where we are trying to touch all points in fastest manner. This is rather simple.
# Just generate every permuation of the locations, then reduce the lists of places to a (path, length) tuple.
# ----------------------------------------------------------------------------------------------------------------------

print min((reduce(lambda first, second: (first[0] + [second], first[1] + _input[first[0][-1]][second]), [([places[0]],0)] + list(places)[1:]) for places in itertools.permutations(_input.iterkeys())), key=lambda x: x[1])[1]



# ----------------------------------------------------------------------------------------------------------------------
# Part 2 (find longest possible path)
#
# Same as last, but max instead of min
# ----------------------------------------------------------------------------------------------------------------------

print max((reduce(lambda first, second: (first[0] + [second], first[1] + _input[first[0][-1]][second]), [([places[0]],0)] + list(places)[1:]) for places in itertools.permutations(_input.iterkeys())), key=lambda x: x[1])[1]
