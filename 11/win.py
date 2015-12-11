# ----------------------------------------------------------------------------------------------------------------------
# Advent of Code - Day 11
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
import string, itertools, re
_input = sum(26**i * (ord(c)%32 - 1) for i,c in enumerate(list(reversed('vzbxkghb'))))

# ----------------------------------------------------------------------------------------------------------------------
# Part 1 (find the next valid password)
# 
# We first convert the input string to a numeric number (base 26 but with no numbers), and then using itertools.count,
# start incrementing from that number. Each number will be converted to a base26 string using a recursive lambda
# function to do so, with the result being tested against three regular expressions, which test for sequence of chars,
# double chars, and no i's, o's, or l's.
# ----------------------------------------------------------------------------------------------------------------------

print next(password for newPass in itertools.count(_input + 1) for password in [(lambda pad: 'a'*(8-len(pad)) + pad)((lambda toPass: (lambda func, arg1, arg2: func(func, arg1, arg2))(lambda self, number, letters: letters[number] if number < 26 else self(self, number / 26, letters) + letters[number % 26] , toPass, dict(zip([ord(c)%32-1 for c in string.lowercase], string.lowercase))))(newPass))] if len(re.findall(r'[^iol]{8}', password)) > 0 and len(re.findall(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|jik|ikl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password)) > 0 and len(re.findall(r'(\w)\1.*(\w)\2', password)) > 0)



# ----------------------------------------------------------------------------------------------------------------------
# Part 2 (find the next password)
# ----------------------------------------------------------------------------------------------------------------------
_input = sum(26**i * (ord(c)%32 - 1) for i,c in enumerate(list(reversed('vzbxxyzz'))))

print next(password for newPass in itertools.count(_input + 1) for password in [(lambda pad: 'a'*(8-len(pad)) + pad)((lambda toPass: (lambda func, arg1, arg2: func(func, arg1, arg2))(lambda self, number, letters: letters[number] if number < 26 else self(self, number / 26, letters) + letters[number % 26] , toPass, dict(zip([ord(c)%32-1 for c in string.lowercase], string.lowercase))))(newPass))] if len(re.findall(r'[^iol]{8}', password)) > 0 and len(re.findall(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|jik|ikl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password)) > 0 and len(re.findall(r'(\w)\1.*(\w)\2', password)) > 0)
