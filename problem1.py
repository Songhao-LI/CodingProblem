def problem1(source, target):
    res = 0
    
    source_arr = deque(source)
    target_arr = deque(target)
    n = len(source_arr)
    m = len(target_arr)
    
    while target_arr:
        for i in range(n):
            if source_arr[i] == target_arr[0]:
                target_arr.popleft()
        if len(target_arr) == m:
            return -1
        else:
            m = len(target_arr)
            res += 1

    return res


print(problem1("abc", "abcbc"))
print(problem1("abc", "acdbc"))
print(problem1("xyz", "xzyxz"))
