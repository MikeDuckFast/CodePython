# ktra so + hay so -

def check(n):
    if n > 0:
        print("La so duong")
    elif n < 0:
        print("La so am")
    else:
        print("La so 0 - khong duong khong am")

try:
    n = int(input("Nhap vao so nguyen: "))
    r = check(n)
    print(r)
except ValueError:
    print("Hay nhap lai so nguyen: ")