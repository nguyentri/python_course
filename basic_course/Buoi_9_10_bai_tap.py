#Bài 1: Tìm số có giá trị ở giữa trong 3 số thực nhập vào
#Ví dụ: Nếu nhập vào 1, 2, 3 thì in ra "Số giá trị ở giữa là 2"
#Bước 1 nhập số
num1 = float(input("Nhập số thứ nhất: ")) #1
num2 = float(input("Nhập số thứ hai: "))  #2
num3 = float(input("Nhập số thứ ba: "))   #3

#Bước 2 Gán số thứ nhất là số ở giữa
mid_num = num1 # 1

if (num1 == num2 or num2 == num3 or num3 == num1):
    print("Không tồn tại giá trị ở giữa!")
else:
    # So sánh và cập nhật số giá trị ở giữa
    # so sánh với số thứ 2 với số thứ nhất và số thứ 3
    if (num2 >= mid_num and num2 <= num3) or (num2 <= mid_num and num2 >= num3):
        mid_num = num2 #2
     # so sánh với số thứ 3 với số thứ nhất và số thứ 2
    if (num3 >= mid_num and num3 <= num2) or (num3 <= mid_num and num3 >= num2):
        mid_num = num3
    # In ra số ở giữa
    print("Số có giá trị ở giữa là:", mid_num)

#Bài 2: Kiểm tra số nhập vào là 1 số chia hết cho 2, 3
#Ví dụ: 
# - Nếu nhập vào 2 thì in ra "Số nhập vào không chia hết cho cả 2 và 3!"
# - Nếu nhập vào 6 thì in ra "Số nhập vào chia hết cho cả 2 và 3!"
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
if (b): # Tương đương với if ((a % 2 == 0) and (a % 3 == 0))
    print("số nhập vào chia hết cho cả 2 và 3!")
else:
    print("Số nhập vào không chia hết cho cả 2 và 3!")

#Bài 3: Kiểm tra số nhập vào là 1 số chia hết cho 2, 3 nhưng không chia hết cho 4
a = input("Nhập vào số nguyên: ")
#Bước 2 đổi từ chuỗi nhập vào thành số nguyên
a = int(a)
#Bước 3 kiểm tra điều kiện a chia hết cho 2 và 3 đồng thời không chia hết cho 4
if (a % 2 == 0) and (a % 3 == 0) and (a % 4 != 0):
    print("số nhập vào chia hết cho cả 2 và 3 và không chia hết cho 4!")
else:
    print("Những số còn lại")
    
#Bài 4: Nhập vào 3 góc của 1 tam giác, xác định loại tam giác đó
#Ví dụ: Nhập vào goc1 = 60, goc2 = 60, goc3 = 60, in ra "Tam giác đều!"
g1 = float(input("Góc thứ nhất:"))
g2 = float(input("Góc thứ 2:"))
g3 = float(input("Góc thứ 3:"))

#Kiểm tra 3 góc nhập vào có phải của 1 tam giác hay không
if (g1 + g2 + g3 == 180):
    if(g1 == g2 == g3):
        print("Tam giác đều!")
    elif(g1 == g2 or g2 == g3 or g3 == g1 ):
        print("Tam giác cân!")
    elif(g1 == 90 or g2 == 90 or g3 == 90):
        print("Tam giác vuông!")
    else:
        print("Tam giác thường!")
else:
    print ("3 góc nhập vào không phải của 1 tam giác!")
