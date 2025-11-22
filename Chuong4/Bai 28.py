L = input("Nhập các phần tử danh sách, cách nhau bằng khoảng trắng: ").split()
K = []
for i in range(0, len(L), 2):
    if i + 1 < len(L):
        if isinstance(L[i], str) and L[i + 1].isdigit():
            K.append(L[i] + str(L[i + 1]))

print(K)