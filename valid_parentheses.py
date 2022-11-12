
def valid_para(s):

    stack = []

    lookup = {
        ")":"(","}":"{","]":"["
    }

    if len(s) == 0 or len(s) % 2 != 0:
        return False

    for element in s:
        if element in lookup:
            if stack and stack[-1] == lookup[element]:
                stack.pop()
            else:
                return False
        else:
            stack.append(element)
    return stack == []


print(valid_para('{}'))
