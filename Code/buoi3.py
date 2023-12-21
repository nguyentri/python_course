'''Bài Tập 1:
Tạo 2 biến tên là so1 và so2 và nhập từ bàn phím
a. Tính tổng số, so1 và so2; lưu kết quả vào biến ketqua; và dùng hàm print in biến ketqua ra màn hình.
b. Tính nhân 2 số, so1 và so2; lưu kết quả vào biến ketqua; và dùng hàm print in biến ketqua ra màn hình.
c. Làm tương tự cho phép hiệu và phép chia
'''

#Khai báo 2 số
print ("Phần mềm tính +, -, *, : 2 số nguyên!")
#hàm input để nhận dữ liệu từ bàn phím
so1 = input("Mời nhập số thứ nhất: ")
so2 = input("Mời nhập số thứ hai: ")
#hàm int để đổi từ chuỗi nhập từ bàn phím thành số nguyên
so1 = int(so1)
so2 = int(so2)
#Tính tổng 2 số34
ketqua =  so1 + so2
#In tổng 2 số ra màn hình
print ("Kết quả tổng của 2 số", so1, "và", so2, "là: ", ketqua)
#Nhân 2 số
ketqua = so1 * so2
#In tích 2 số ra màn hình
print ("Kết quả tích của 2 số", so1, "và", so2, "là: ", ketqua)
#Hiệu 2 số
ketqua = so1 - so2
#In hiệu 2 số ra màn hình
print ("Kết quả hiệu của 2 số", so1, "và", so2, "là: ", ketqua)
#Chia 2 số
ketqua = so1 / so2
print ("Kết quả chia của 2 số", so1, "và", so2, "là: ", ketqua)

'''
Bài Tập 2:  Dùng 1b để làm bài sau
Tính diện tích của bàn học với chiều rộng là 0.5 m và chiều dài là 1.2 m và in kết quả ra màn hình có giải thích với chuỗi.
“Chiều dài của bàn là: “, …
“Chiều dài của bàn là : “,  …
“Diện tích của bàn là :  “, ….
'''
#chieudaiban = 1.2
#chieurongban = 0.5
##Dien tich ban la
#dientichban = chieudaiban * chieurongban
#print("Chiều dài của bàn là:", chieudaiban)
#print("Chiều rộng của bàn là:", chieurongban)
#print("Diện tích của bàn là  :", dientichban)