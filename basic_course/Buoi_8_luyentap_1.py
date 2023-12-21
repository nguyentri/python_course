#Xác định mùa trong năm với tháng nhập vào
#(nhập số 1 đến 12)
#Ví dụ nhập vào tháng "1", in ra "Mùa Xuân"
month = int(input("Nhập tháng trong năm (1-12): "))
if (1 <= month <=3):
    print("Mùa Xuân")
elif (4 <= month <=6):
    print("Mùa Hạ")
elif (7 <= month <=9):
    print("Mùa Thu")
elif (10 <= month <= 12):
    print("Mùa Đông")
else:
    print("Tháng không hợp lệ")
    