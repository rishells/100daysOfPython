# Input is a string aabcc
# output 2a1b2c


#aabcca -> 2a1b2c1a


def string_encode(input):
    # check for null input
    if len(input) == 0:
        return ""
    prevChar = ""
    counter = 0
    result = []
    # Iterate ober input
    for char in input:
        if char == prevChar:
            counter +=1
        else:
            if prevChar != '':
                result.append(str(counter)+prevChar)
            prevChar = char
            counter = 1
        #result.append(prevChar)
    result.append(str(counter)+prevChar)
    return result

    

#print(string_encode('aaaabbccccddddddaa'))
result = string_encode('aaaabbccccddddddaa')
#print(result)
for item in result:
    print(item,end=' ')

# def reverse_string(input):
#     for i in range(len(input),0,-1):
#         print(input[i-1],end='')

# my_string = 'ricardo'
# print(my_string[0])

#reverse_string('ricardo')
#string_encode('ricardo')