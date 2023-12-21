#Kiểu int: Kiểu số nguyên, không chứa
#phần thập phân, có thể lưu số nguyên âm và nguyên dương
#Ví dụ: -10, 1, 0, 1, 10
so_nguyen = 10
#kiểm tra kiểu của biến so_nguyen
print (type(so_nguyen))
#Nhập số nguyên
#so_nguyen = int(input("nhập số nguyên: "))
print (so_nguyen)

#Kiểu float: Kiểu số thực (có chứa phần thập phân)
#Phân biệt phần nguyên và phần thập phân bới dấu .
so_thuc = 10.00000
#Kiểm tra kiểu in ra màn hình
print (type(so_thuc))
#Nhập số thực từ bàn phím
#so_thuc = float(input("Nhập số thực: "))
print(so_thuc)

#Kiếu str: Kiểu chuỗi,
#để trong nháy đôi hoặc nháy đơnd
chuoi1 = "Hello!"
chuoi2 =  'Goodbye!'
print (chuoi1 + chuoi2)
#nhập chuỗi
#chuoi = input("Nhập chuỗi: ")
#print(type(chuoi))
#print(chuoi)
chuoi = str(1)

#Kiểu bool: chỉ để lưu 2 giá trị
#True (đúng) hoặc False (sai)
var1 = True
var2 = False
print (var1, var2)
print(type(var1), type(var2))
var3 = (1==1)
print (var3)
var3 = "hi"
if (var3):
    print (bool(var3))
#Hầu hết các giá trị kiểu bool đều là True
#Hầu hết mọi giá trị đều được đánh giá là True  
#nếu nó có một loại nội dung nào đó.
#Mọi số đều True, ngoại trừ 0 hoặc chuỗi rỗng
var3 = ""
var3 = 0
var3 = 0.0
if (var3):
    print(True)
else:
    print (False)
#Nhập vào một số thập phân in ra phần nguyên 
#và in ra 1 số thập phân sau dấu chấm.