it = iter([1,2,3,4,5,6,7])

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break