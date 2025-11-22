from person import Person

class HocSinh(Person):
    def __init__(self, ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi, diem_toan, diem_ly, diem_hoa):
        super().__init__(ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi)
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    @property
    def diem_trung_binh(self):
        return (self.diem_toan + self.diem_ly + self.diem_hoa) / 3

    @property
    def xep_loai(self):
        if self.diem_trung_binh > 8 and min(self.diem_toan, self.diem_ly, self.diem_hoa) >= 6.5:
            return "Giỏi"
        elif self.diem_trung_binh > 6.5 and min(self.diem_toan, self.diem_ly, self.diem_hoa) >= 5:
            return "Khá"
        elif self.diem_trung_binh > 5 and min(self.diem_toan, self.diem_ly, self.diem_hoa) >= 3:
            return "Trung bình"
        else:
            return "Yếu"