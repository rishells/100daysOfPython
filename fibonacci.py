import time
from tracemalloc import start
start_time = time.time()

# A naive recursive solution
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result



# A memoized solution

def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)


# A bottom-up solution
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]


# 1 1 2 3 5 8 13 21 34



def main():
    memo = []
    #print(fib(40)) # 42 sec --- naive recursive solution  --- Exponential time  ---
    #print(fib_bottom_up(100)) # --- 0 sec bottom-up solution 
    print(fib_2(100,memo))

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()