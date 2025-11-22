from datetime import datetime, timedelta

with (open("G:\\BT_py\\CHUONG2\\ngay.inp.txt", "r", encoding='utf-8') as f_in,
      open("ngay.out.txt", "w", encoding='utf-8') as f_out):
    date_str, n = f_in.readline().split()
    n = int(n)
    date = datetime.strptime(date_str, "%d/%m/%Y")
    newDate = date + timedelta(days=n)
    newDate_str = newDate.strftime("%d/%m/%Y")
    f_out.write(newDate_str)