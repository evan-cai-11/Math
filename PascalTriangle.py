def f(x, y):
    counter=0
    ret = 0
    if (x == 1 or y == 1):
        ret = 1
        counter = 1 
    else:
        ret = f(x, y-1)[0] + f(x-1, y)[0]
        counter += 1

    print(f"f({x}, {y}) = {ret}")
    print(counter)
    return ret, counter
    

print(f(4,4))