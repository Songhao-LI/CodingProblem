def problem3(n, arr):
    def get_weight(sub):
        if not sub:
            return 0
        sub_n = len(sub)
        mean = sum(sub) / sub_n
        if sub_n % 2 == 1:
            median = sub[sub_n // 2]
        else:
            median = (sub[(sub_n // 2) - 1] + sub[sub_n // 2]) / 2
        return mean - median

    def handle_subsequences(index, current_subsequence):
        if index == n:
            if current_subsequence:
                val = get_weight(current_subsequence)
                nonlocal max_val
                if val > max_val:
                    max_val = val
            return
        handle_subsequences(index + 1, current_subsequence + [arr[index]])
        handle_subsequences(index + 1, current_subsequence)

    max_val = float('-inf')
    arr.sort()
    handle_subsequences(0, [])
    return max_val


print(problem3(4, [1,3,5,9]))
