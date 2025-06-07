n = float(input("Nhap vao so Km: "))
tong = 0
if n <= 1:
    tong = 10000
elif n <=10:
    tong = 10000 + (n-1)*8500
else:
    tong = 10000 + (9*8500) + (n-10)*7500

print("Tong tien la: ",tong," VND")