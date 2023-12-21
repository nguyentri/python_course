#Kiểm tra số nhập vào là số nguyên dương hay số nguyên âm hay là Zero
#Bước 1: nhập số
a = input("Nhập số nguyên: ")
#Bước 2: đổi chuỗi nhập vào thành số nguyên
a = int(a)
#Bước 3: Kiểm tra số
if (a > 0) : # kiểm tra số dương
    print("Số nguyên dương")
elif (a < 0) : #kiểm tra số âm
    print("Số nguyên âm")
else: # ngoài trừ số nguyên âm, nguyên dương sẽ là zero
    print("Số nguyên là 0")
















