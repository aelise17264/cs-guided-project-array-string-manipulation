def validParenthesesSequence(s):
    openP = []
    
    for i in range(0, len(s)):
        char = s[i]
        if char == "(":
            openP.append("(")
        elif char == ")":
            if not openP:
                return False
            else:
                openP.pop()
    if not openP:
        return True
    else:
        return False


print(validParenthesesSequence(")))((()(())))(())((("))
print(validParenthesesSequence("()()())"))
