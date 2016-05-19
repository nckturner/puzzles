def fib_at_m(a, b, m):
    fibs = [a, b]
    for i in range(2,m):
        fibs.append(fibs[-1]*fibs[-1] + fibs[-2])
    return fibs[m-1]

if __name__ == "__main__":
    x = input().split()

    print(fib_at_m(int(x[0]),int(x[1]),int(x[2])))
