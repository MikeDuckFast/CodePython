def xeploai(n):
    if n >= 8.5:
        return("Xuat sac")
    elif n>=7.0:
        return("Gioi")
    elif n>= 5.5 :
        return("Kha")
    elif n >= 4.0 :
        return("Trung binh")
    else:
        return("Yeu")


n = int(input("So luong mon hoc: "))
tong = 0
for i in range(n):
    d = float(input( f"Nhap diem mon hoc thu {i+1}:" ))
    if d < 0 or d > 10:
        print("Hay nhap diem hop le!")
        break
    tong += d

dtb = tong / n
print("Xep loai: ",xeploai(dtb))