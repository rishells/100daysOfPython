def max_deviation(s, max_dev_init=-1):
    occurence = {}

    max_val = 0
    min_val = len(s)
    min_ch = '\0'
    max_dev = max_dev_init

    for i in range(len(s)):
        ch = s[i]
        if ch not in occurence:
            occurence[ch] = 0

        occurence[ch] += 1
        if ch == min_ch:
            min_ch = min(occurence, key=occurence.get)
            min_val = occurence[min_ch]
        elif occurence[ch] < min_val:
            min_val = occurence[ch]
            min_ch = ch

        if occurence[ch] > max_val:
            max_val = occurence[ch]

        # for i in occurence:
        #     if occurence[i] < min_val:
        #         min_val = occurence[i]

        if (max_val - min_val) > max_dev:
            max_dev = max_val - min_val

    if max_dev_init == -1:
        max_dev_inv = max_deviation(s[::-1], max_dev)
        if max_dev_inv > max_dev:
            max_dev = max_dev_inv



    return max_dev

print(max_deviation('bbacccabab'))