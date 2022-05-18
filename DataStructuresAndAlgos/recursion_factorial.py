def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1) # With recursion N * log(N)
# Iterations (3!)
#          3 * 2!
#          2 * 1!
#          1 * 1! 
#
#          	↑
#
#           3 * 2
#           2 * 1
#           1
#
print(factorial(200))

# Naive method O(N)

def fact_naive(num):
    fact = 1
    while(num > 1):
        fact = fact * num
        num -= 1
    return fact

#print(fact_naive(200))