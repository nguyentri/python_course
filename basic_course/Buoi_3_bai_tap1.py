#Nhập một số thực từ bàn phím// và in ra phần nguyên in phần thập phân 3 chữ số.
#Ví dụ nhập 10.001, kết quả: 
# "Phần nguyên: 10"
# "Phần thập phân: 001"

#Bước 1: Nhập số thực từ bàn phím
so_thuc = input("Nhập số thực")
so_thuc = float(so_thuc)
#Bước 2: Tìm phần nguyên, in phần nguyên
phan_nguyen = int(so_thuc)
print("Phần nguyên:", phan_nguyen)
#Bước 3: Tìm phần thập phân
phan_thap_phan = so_thuc*1000 - phan_nguyen*1000
#Lấy phần nguyên của biến phan_thap_phan
phan_thap_phan = int(phan_thap_phan)
print("Phần thập phân:", phan_thap_phan)
#Cách dùng hàm print theo kiểu định dạng
#03 là số cần in ra ít nhất 3 chữ số, d là số nguyên
print(f"Phần thập phân 3 chữ số {phan_thap_phan:03d}")






