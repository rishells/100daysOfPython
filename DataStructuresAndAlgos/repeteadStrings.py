# Example
# Input     s = 'abcac'
#           n = 10



def repeatedString(s, n):
    full_string = ''
    s_length = len(s)
    a_counter = 0
    # if s_length < n:
    #     full_string = s

    length_check = s_length
    while s_length < n:
        
        full_string += s

    return count_a(full_string)
    

def count_a(s):
    a_counter = 0
    for i in range(len(s)):
        if s[i] == 'a':
            a_counter +=1
    return a_counter

#s = 'Ricardo'
#print(s.count('a'))

#print(count_a('Ricardo Emmanuel'))
print(repeatedString('abcac',10))


    
    