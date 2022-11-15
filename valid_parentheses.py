
def valid_para(s):
    #creation of the list, aka our stack
    stack = []
    #creation of dictionary or hashmap
    lookup = {
        ")":"(","}":"{","]":"["
    }
    #Some base cases, to not do stack.
    if len(s) == 0 or len(s) % 2 != 0:
        return False

    for element in s:
        #if the element is valid in in the lookup table
        if element in lookup:
            # in python stack of -1 is the last item we just added to the stack
            # if element is in stack and is previous element equal lookup element
            # remove them
            if stack and stack[-1] == lookup[element]:
                stack.pop()
            else:
                return False
        else:
            # if opening tag append that element
            stack.append(element)
    return stack == []


print(valid_para('{}'))
