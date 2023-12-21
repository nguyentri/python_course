#Nhập vào số nguyên a, 
#nếu a là số chia hết cho 5 nhưng KHÔNG nằm trong khoảng từ [20 - 70] thì in ra True,
#ngược lại in ra False
#Kiểm tra bằng nhập số 10, 20, 70, 90, 99 -> Kết quả True: 10, 90 ; Số khác là False
#Bước 1 nhập số từ bàn phím
a = input("Điền vào số nguyên: ")
#Bước 2 đổi từ chuỗi nhập vào thành số nguyên
a = int(a)
#Bước 3 kiểm tra điều kiện a chia hết cho 5
#và đồng thời NGOÀI khoảng [20 - 70]
#b = (not (a % 5)) and (a < 20 or a > 70)
c = (a % 5)
d = not c
#Kiểm tra ngoài khoảng
e = (a < 20 or a > 70)
b = d and e 
#In kết quả
print(b)
