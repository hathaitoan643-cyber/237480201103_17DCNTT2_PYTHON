def dem_so_tu(chuoi):
    for ky_tu in chuoi:
        if ky_tu.isalpha() or ky_tu.isspace():
            continue
        else:
            chuoi = chuoi.replace(ky_tu, ' ')
    danh_sach_tu = chuoi.split()
    so_tu = len(danh_sach_tu)
    return so_tu


s = input("Nhập chuỗi: ")
count_w = dem_so_tu(s)
print("Số từ trong chuỗi là:", count_w)
