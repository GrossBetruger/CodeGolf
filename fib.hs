

fib 0 = 1
fib 1 = 1
fib n = fib(n-2) + fib(n-1)

main = print $ map fib [0..30]
