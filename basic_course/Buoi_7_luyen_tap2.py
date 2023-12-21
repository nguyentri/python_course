#Kiểm tra số lớn nhất trong 3 số thực nhập vào
#

#Bước 1 nhập số
num1 = float(input("Nhập số thứ nhất: ")) #1
num2 = float(input("Nhập số thứ hai: "))  #2
num3 = float(input("Nhập số thứ ba: "))   #3

#Bước 2 Gán số thứ nhất là số lớn nhất
max_num = num1 # 1

# So sánh và cập nhật số lớn nhất nếu cần
if num2 > max_num: # so sánh với số thứ 2
    max_num = num2 #2

if num3 > max_num: # so sánh với số thứ 3
    max_num = num3

# In ra số lớn nhất
print("Số lớn nhất là:", max_num)
