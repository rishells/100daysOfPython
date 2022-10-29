import big_o
def fib_naive(n):
     if n < 0:
         return -1
     if n < 2:
         return n
     return fib_naive(n-1) + fib_naive(n-2)

#print(big_o.big_o(fib_naive, big_o.datagen.n_, n_repeats=20, min_n=2, max_n=25)[0])

def print_items(n):
    counter = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(counter)
                print(f"i:{i}, j:{j}, k:{k}")
                counter += 1


print_items(10)