def pos_string_suppercharcs(ls):
    vi_tri_max = -1
    so_ky_tu_in_hoa_max = 0

    for i, chuoi in enumerate(ls):
        so_ky_tu_in_hoa = sum(1 for char in chuoi if char.isupper())
        if so_ky_tu_in_hoa > so_ky_tu_in_hoa_max:
            so_ky_tu_in_hoa_max = so_ky_tu_in_hoa
            vi_tri_max = i

    return vi_tri_max  # Trả về vị trí của chuỗi có ký tự in hoa lớn nhất


n = int(input("Nhập số phần tử danh sách: "))
L = []
for k in range(n):
    gt = input(f"Nhập giá trị phần tử thứ {k + 1}: ")
    L.append(gt)

vt = pos_string_suppercharcs(L)
if vt != -1:
    print(f"Vị trí của chuỗi có ký tự in hoa lớn nhất: {vt + 1}")
else:
    print("Không có chuỗi nào có ký tự in hoa trong danh sách L.")