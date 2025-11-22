def FirstPosition(list_n, k):
    for i in range(len(list_n)):
        if list_n[i] == k:
            return i
    return -1


list_numbers = [-2, -2, 6, 1, 3, 6]
t = 3
vt = FirstPosition(list_numbers, t)
if vt != -1:
    print(f"Phần tử đầu tiên có giá trị {t} nằm ở vị trí {vt+1}")
else:
    print(-1)