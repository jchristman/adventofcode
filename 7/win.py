# ----------------------------------------------------------------------------------------------------------------------
# Advent of Code - Day 7
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
_input = {re.findall('(?<=-> )([a-z]+)', line)[0]: (_type, (re.findall('([0-9]+|[a-z]+)', line)[0],) if _type == 'ASSIGN' else (re.findall('([a-z]+|[0-9]+)(?= AND| OR)', line)[0], re.findall('([a-z]+|[0-9]+) (?=->)', line)[0]) if _type == 'AND' or _type == 'OR' else (re.findall('([a-z]+).*(?=->)', line)[0], re.findall('([0-9]+)', line)[0]) if _type == 'LSHIFT' or _type == 'RSHIFT' else (re.findall('([a-z]+)', line)[0],)) for _type, line in [(re.findall('([A-Z]+)', line)[0] if len(re.findall('([A-Z]+)', line)) > 0 else 'ASSIGN', line) for line in open('input', 'r').read().splitlines()]}

# ----------------------------------------------------------------------------------------------------------------------
# Part 1 (find the value assigned to a)
# 
# This is definitely a weird one. Use mutual recursion to step through the dictionary built by reading input and perform
# a bunch of operations in lambda functions. Use a bit of dynamic programming to update the _input variable with the
# values of each variable as it is found to avoid having to explore a tree that is potentially 2**(12*26) branches nodes
# large.
# ----------------------------------------------------------------------------------------------------------------------

print (lambda ask: (lambda func2, ask2: func2(func2, ask2))(lambda func1, ask1: (_input.update({ ask1: ('ASSIGN', (int(_input[ask1][1][0] if isinstance(_input[ask1][1][0], str) and _input[ask1][1][0].isdigit() or isinstance(_input[ask1][1][0], int) else func1(func1, _input[ask1][1][0])),))}) or _input[ask1][1][0]) if _input[ask1][0] == 'ASSIGN' else (_input.update({ ask1: ('ASSIGN', (int(func1(func1, _input[ask1][1][0]) >> int(_input[ask1][1][1])),))}) or _input[ask1][1][0]) if _input[ask1][0] == 'RSHIFT' else (_input.update({ ask1: ('ASSIGN', (int(func1(func1, _input[ask1][1][0]) << int(_input[ask1][1][1])),))}) or _input[ask1][1][0]) if _input[ask1][0] == 'LSHIFT' else (_input.update({ ask1: ('ASSIGN', (int(int(_input[ask1][1][0] if isinstance(_input[ask1][1][0], str) and _input[ask1][1][0].isdigit() or isinstance(_input[ask1][1][0], int) else func1(func1, _input[ask1][1][0])) | int(_input[ask1][1][1] if isinstance(_input[ask1][1][0], str) and _input[ask1][1][1].isdigit() or isinstance(_input[ask1][1][0], int) else func1(func1, _input[ask1][1][1]))),))}) or _input[ask1][1][0]) if _input[ask1][0] == 'OR' else (_input.update({ ask1: ('ASSIGN', (int(int(_input[ask1][1][0] if isinstance(_input[ask1][1][0], str) and _input[ask1][1][0].isdigit() or isinstance(_input[ask1][1][0], int) else func1(func1, _input[ask1][1][0])) & int(_input[ask1][1][1] if isinstance(_input[ask1][1][0], str) and _input[ask1][1][1].isdigit() or isinstance(_input[ask1][1][0], int) else func1(func1, _input[ask1][1][1]))),))}) or _input[ask1][1][0]) if _input[ask1][0] == 'AND' else (_input.update({ ask1: ('ASSIGN', (~int(func1(func1, _input[ask1][1][0])),))}) or _input[ask1][1][0]) if _input[ask1][0] == 'NOT' else _input[ask1], ask))('a')



# ----------------------------------------------------------------------------------------------------------------------
# Part 2 (find the value assigned to a if b is assigned a from part 1)
#
# Reset the _input variable and assign 3176 to variable b.
# ----------------------------------------------------------------------------------------------------------------------

_input = {re.findall('(?<=-> )([a-z]+)', line)[0]: (_type, (re.findall('([0-9]+|[a-z]+)', line)[0],) if _type == 'ASSIGN' else (re.findall('([a-z]+|[0-9]+)(?= AND| OR)', line)[0], re.findall('([a-z]+|[0-9]+) (?=->)', line)[0]) if _type == 'AND' or _type == 'OR' else (re.findall('([a-z]+).*(?=->)', line)[0], re.findall('([0-9]+)', line)[0]) if _type == 'LSHIFT' or _type == 'RSHIFT' else (re.findall('([a-z]+)', line)[0],)) for _type, line in [(re.findall('([A-Z]+)', line)[0] if len(re.findall('([A-Z]+)', line)) > 0 else 'ASSIGN', line) for line in open('input', 'r').read().splitlines()]}
_input['b'] = ('ASSIGN', (3176,))

print (lambda ask: (lambda func2, ask2: func2(func2, ask2))(lambda func1, ask1: (_input.update({ ask1: ('ASSIGN', (int(_input[ask1][1][0] if isinstance(_input[ask1][1][0], str) and _input[ask1][1][0].isdigit() or isinstance(_input[ask1][1][0], int) else func1(func1, _input[ask1][1][0])),))}) or _input[ask1][1][0]) if _input[ask1][0] == 'ASSIGN' else (_input.update({ ask1: ('ASSIGN', (int(func1(func1, _input[ask1][1][0]) >> int(_input[ask1][1][1])),))}) or _input[ask1][1][0]) if _input[ask1][0] == 'RSHIFT' else (_input.update({ ask1: ('ASSIGN', (int(func1(func1, _input[ask1][1][0]) << int(_input[ask1][1][1])),))}) or _input[ask1][1][0]) if _input[ask1][0] == 'LSHIFT' else (_input.update({ ask1: ('ASSIGN', (int(int(_input[ask1][1][0] if isinstance(_input[ask1][1][0], str) and _input[ask1][1][0].isdigit() or isinstance(_input[ask1][1][0], int) else func1(func1, _input[ask1][1][0])) | int(_input[ask1][1][1] if isinstance(_input[ask1][1][0], str) and _input[ask1][1][1].isdigit() or isinstance(_input[ask1][1][0], int) else func1(func1, _input[ask1][1][1]))),))}) or _input[ask1][1][0]) if _input[ask1][0] == 'OR' else (_input.update({ ask1: ('ASSIGN', (int(int(_input[ask1][1][0] if isinstance(_input[ask1][1][0], str) and _input[ask1][1][0].isdigit() or isinstance(_input[ask1][1][0], int) else func1(func1, _input[ask1][1][0])) & int(_input[ask1][1][1] if isinstance(_input[ask1][1][0], str) and _input[ask1][1][1].isdigit() or isinstance(_input[ask1][1][0], int) else func1(func1, _input[ask1][1][1]))),))}) or _input[ask1][1][0]) if _input[ask1][0] == 'AND' else (_input.update({ ask1: ('ASSIGN', (~int(func1(func1, _input[ask1][1][0])),))}) or _input[ask1][1][0]) if _input[ask1][0] == 'NOT' else _input[ask1], ask))('a')
