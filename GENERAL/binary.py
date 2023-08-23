def numswaps(binary):
    n = len(binary)
    count = 0 
    for i in range(n // 2):
        if binary[i] != binary[n - i - 1]:
            count += 1
    if count % 2 == 1 and n % 2 == 0:
        return -1
    return (count + 1) // 2


print(numswaps('1110'))