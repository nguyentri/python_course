#Nhập vào một số nguyên a, nếu a chia hết cho 2, 
#lưu vào biến tên ret là True, ngược lại False
#Sau đó in ra biết ret
#Bước 1: nhập số
a = input("Nhập số nguyên:")
#Bước 2: đổi số nguyên
a = int(a)
#Bước 3: Xác định chia hết cho 2 = dấu chia lấy dư %, lưu vào biến ret
ret = a%2
ret = bool(ret)
#Not để đổi từ True qua False hoặc False qua True
ret = not ret
#Bước 4: In ra biến ret
print(ret)







