def generate(N):
    # code here
    arr = []
    for i in range(1, N+1):
        arr.append(format(i, "b"))

    return arr
