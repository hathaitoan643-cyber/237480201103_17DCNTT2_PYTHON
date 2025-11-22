from person import Person

class GiaoVien(Person):
    def __init__(self, ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi, tham_nien, hoc_vi):
        super().__init__(ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi)
        self.tham_nien = tham_nien
        self.hoc_vi = hoc_vi