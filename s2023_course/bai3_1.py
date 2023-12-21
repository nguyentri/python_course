#Nhập tên vào chiều cao
name1 = input("Mới nhập tên bạn 1:")
height1 = input("Mới nhập chiều cao bạn 1 m:")
name2 = input("Mới nhập tên bạn 2:")
height2 = input("Mới nhập chiều cao bạn 2 m:")
#Chuyển chuỗi nhập vào thành số nguyên
height1 = float (height1)
height2 = float (height2)
#Dùng lệnh điều kiện 
if height1 > height2:
   #Nếu điều kiện đúng sẽ in ra và không kiểm tra elif tiếp theo nữa
   print(name1 + " cao hơn " + name2)
elif height1 == height2:
   print(name1 + " cao bằng " + name2)
else:
   print(name1 + " thấp hơn " + name2)
