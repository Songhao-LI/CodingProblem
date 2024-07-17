def problem2(str):
    stk = []
    index = []
    for i in range(len(str)):
        ch = str[i]
        if ch == "(":
            stk.append(ch)
            index.append(i)
        elif ch == ")":
            if stk and stk[-1] == "(":
                stk.pop()
                index.pop()
            else:
                stk.append(ch)
                index.append(i)
    
    res = []
    for i in range(len(str)):
        ch = str[i]
        if ch == "(":
            if i not in index:
                res.append(" ")
            else:
                res.append("x")
        elif ch == ")":
            if i not in index:
                res.append(" ")
            else:
                res.append("?")
        else:
            res.append(" ")
    print(res)
    return "".join(res)
                


print(problem2("bge)))))))))"))
print(problem2("((IIII))))))"))
print(problem2("()()()()(uuu"))
print(problem2("))))UUUU((()"))
