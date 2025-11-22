def kt(a, b):
    if a > b:
        for i in range(1, 11):
            print(f"{a} x {i} = {a * i} ")
        return
    else:
        for i in range(1, 11):
            print(f"{b} x {i} = {b * i} ")
        return


kt(8, 7)