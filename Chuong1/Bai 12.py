a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("phương trình vô nghiệm")
else:
    print("Nghiệm của phương trình là: ", round(-b/a,2))