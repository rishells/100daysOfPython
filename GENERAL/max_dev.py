def solution(s):
    try:
        left = s.index('a')
        s.index('b')
    except Exception:
        # One of the index operations didnt work
        return 0

    # We get one point for free :)
    result, current = 1, 1
    result_contains_b, current_contains_b = False, False

    for i in range(left+1, len(s)):
        c = s[i]

        if c == 'a':
            current += 1
            if current > result:
                result = current
                result_contains_b = current_contains_b
        elif c == 'b':
            current -= 1
            current_contains_b = True
            if current < 0:
                current = 0
                current_contains_b = False
        else:
            # These characters mean nothing to us,
            # despise them!11
            continue

    if current_contains_b == True:
        return result
    else:
        return result-1

print(solution('bbacccabab'))