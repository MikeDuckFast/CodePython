n = int(input("Nhap vao nam: "))
if ((n%4==0) & (n%100 != 0) or  (n %400==0)):
    print("Nam nhuan")
else: 
    print("Khong la nam nhuan")