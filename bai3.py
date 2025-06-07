a = int(input("nhap so nguyen a: "))
b = int(input("nhap so nguyen b: "))
c = int(input("nhap so nguyen c: "))

if(a>b) & (a>c):
    print("So lon nhat la: ",a)
elif (b>a) & (b>c):
    print("So lon nhat la: ",b)
else:
    print("So lon nhat la: ",c) 