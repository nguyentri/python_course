#Nhập vào một số nguyên a, nếu a chia hết cho 2 và 3 thì in ra True, ngược lại in ra False
#Bước 1 nhập số từ bàn phím
#Kiểm tra bằng cách điền thử số 6, 7, 8
a = input("Nhập vào số nguyên: ")
#Bước 2 đổi từ chuỗi nhập vào thành số nguyên
a = int(a)
#Bước 3 kiểm tra điều kiện a chia hết cho 2 và 3
#Nếu đồng thời chia hết cho 2 và 3 thì kết quả là True, ngược lại là False
#Kiểm tra chia hết cho 2, dùng phép lấy dư %
c = (a % 2 == 0) # so sánh a chia dư 2 = 0 thì c là True 
#Kiểm tra chia hết cho 3
d = (a % 3 == 0)   # so sánh a chia dư 3 = 0 thì d là True
b = c and d
#In kết quả
print(b)
