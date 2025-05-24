"""
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
"""
def isValid(s: str) -> bool:
    stack = []
    hashmap = {
        ")":"(",
        "]":"[",
        "}":"{",
    }

    for char in s:
        if char in hashmap:
            if stack and stack[-1] == hashmap[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return True if not stack else False

a = "()[]}{"
isValid(a)
