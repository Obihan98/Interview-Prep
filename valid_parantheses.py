# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        balance = 0
        remove = []
        stack = []
        for i, char in enumerate(s):
            if char == '()':
                continue
            if char == '(':
                stack.append(i)
            elif char == ')':
                if len(stack) == 0:
                    remove.append(i)
                else:
                    stack.pop()
        
        new_string = ''
        for i, char in enumerate(s):
            if i in remove or i in stack:
                continue
            new_string += char
            
        return new_string
                
            