numbers = list(map(int, input("Nhap day so: ").split()))
count = {}

for number in numbers:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

for number in count:
    print(f"Số {number} lặp lại {count[number]} lần")