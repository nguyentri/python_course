
#Bài tập 1 buổi 4 bắt buộc
#Điền vào dấu chấm ? để hoàn thành chương trình theo yêu cầu sau:
# Nhập vào số nguyên a, nếu a là số chia hết cho 3 và nằm trong khoảng từ
# [50 - 100] thì in ra True, ngược lại in ra False
#Bước 1 nhập số từ bàn phím
a = input("Điền vào số nguyên: ")
#Bước 2 đổi từ chuỗi nhập vào thành số nguyên
a = int(a)
#Bước 3 kiểm tra điều kiện a chia hết cho 3 (điền vào dấu so sánh thích hợp)
b = (a%3 == 0) # Trả về kết quả lưu vào biến b là True nếu a chia hết cho 3
#Bước 4 : Kiểu tra a nằm trong khoảng 50 - 100 dùng dấu and
c = (a >= 50 and a <= 100) # Kết quả trả về True lưu vào biến c nếu a nằm trong khoảng 50 - 100
#Bước 4 kết hợp 2 điều kiện của kết quả (a chia hết cho 3, biến b) và (a nằm trong khoảng 50 - 100, biến c)
d = b and c
#In kết quả
print (d)
