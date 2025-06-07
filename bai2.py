#002 Ktra chan hay le
def check(n):
    if (n%2==0):
        print("La so chan")
    else :
        print("La so le")

try:
    n = int(input("Nhap vao so nguyen: "))
    s = check(n)
    print(s)
except ValueError:
    print("Vui long nhap lai so nguyen: ") 
    