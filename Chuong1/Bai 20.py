h = int(input("Nhập độ cao của tam giác: "))
if h <= 0:
    print("Vui lòng nhập độ cao lớn hơn 0")
else:
    for i in range(1, h + 1):
        for j in range(1, h + 1):
            if j <= i <= h:
                print("*", end="")
        print()