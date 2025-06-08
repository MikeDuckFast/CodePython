def InsertionSort(A):
    n = len(A)
    print("Bước 0 tang:", A)  # In danh sách ban đầu
    for i in range(1, n):
        value = A[i]
        j = i - 1
        while j >= 0 and A[j] > value:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = value
        print(f"Bước {i}: {A}")  # In danh sách sau mỗi bước
# Nhập danh sách từ bàn phím
arr = list(map(int, input("Nhập dãy số, cách nhau bởi dấu cách: ").split()))
InsertionSort(arr)
