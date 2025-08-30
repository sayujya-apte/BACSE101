fib = [0]
n = int(input())

while fib[-1] < n:
    if len(fib) >= 2:
        if fib[-1]+fib[-2] > n:
            break
        fib.append(fib[-1]+fib[-2])
    elif len(fib) == 1:
        fib.append(1)

print(fib)
