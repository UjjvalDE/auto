def evalRPN(tokens):
    stack = []
    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y) if x % y == 0 else int(y / x)
    }
    
    for token in tokens:
        if token not in ops:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[token](a, b))
            
    return stack[0]