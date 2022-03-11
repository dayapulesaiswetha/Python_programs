#Checking opening and closing bracket using stack push and pop

def func_2(str_1):
    stack = []
    for i in str_1:
        if i == '{' or i == '(' or i == '{':
            stack.append(i)
        elif i == '}' or i==')' or i == '}':
            x = stack.pop()            
            if not compare(x,i):
                return False
        return True        


def compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '{' and closing == '}' :
        return True
    if opening == '[' and closing == ']' :
        return True

print(func_2("{(}"))
            