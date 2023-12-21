#Kiểm tra số nhỏ nhất trong 3 số nhập vào
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
num3 = float(input("Nhập số thứ ba: "))
#Cách 1:
min_num = num1
if num2 < min_num:
    min_num = num2
if num3 < min_num:
    min_num = num3
print("Số nhỏ nhất cách 1 là", min_num)
#Cách 2:
if num1 <= num2 and num1 <= num3:
    min_num = num1
elif num2 <= num1 and num2 <= num3:
    min_num = num2
else:
    min_num = num3
print("Số nhỏ nhất cách 2 là:", min_num)
#Cách 3: 
print("Số nhỏ nhất cách 3 là:", min(num1, num2, num3))
