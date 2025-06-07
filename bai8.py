 # Bai 8: Dem so luong so chan va so le trong day so
l = input("Nhap vao day so nguyen")
n = [int(num) for num in l.split()]

chan = 0
le = 0

for i in n:
    if i%2 == 0:
        chan += 1
    else:
        le += 1

print("So luong so chan:", chan)
print("So luong so le:", le)    
