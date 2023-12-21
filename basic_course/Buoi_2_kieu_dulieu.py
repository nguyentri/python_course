#Kiểu int: kiểu số nguyên như trong toán học.
#Có lưu số nguyên âm và nguyên dương
so_nguyen = 10
print(type(so_nguyen))
#Đổi 1 chuỗi sang 1 số nguyên dùng hàm int
so_nguyen = input("Nhập số nguyên:")
so_nguyen = int(so_nguyen)
print(so_nguyen)

#Kiểu float: Kiểu số thực (có chứa phần thập phân)
#Phân biệt phần nguyên và phần thập phân bởi dấu .
so_thuc = input("Nhập số thực: ")
#Đổi 1 chuỗi sang 1 số thực dùng hàm float
so_thuc = float(so_thuc)
print(so_thuc)

#Kiểu chuỗi (str/string), để trong dấu nháy đơn hoặc dấu đôi
#Hàm input luôn trả về 1 chuỗi sau khi ấn Enter
so_nguyen = 1
chuoi = str(so_nguyen)
print(chuoi)

#Kiểu bool/boolean, chỉ có 2 giá trị là True hoặc False
#Mọi giá trị của kiểu bool đều True ngoài trừ giá trị của nó là 0 hoặc
#chuỗi rỗng.
var_is_false = bool("")
print(var_is_false)
var_is_false = bool(0)
print(var_is_false)
var_is_false = bool("")
print(var_is_false)
var_is_false = bool(0)
print(var_is_false)
var_is_false = bool(0.0)
print(var_is_false)
var_is_true = bool("0")
print(var_is_true)
#Biểu thị sự đúng () sai trong so sánh
print(12>2)
print("a"=="b")
