#Nhập vào một số thập phân in ra phần nguyên 
#và in ra 1 số thập phân sau dấu chấm.
so_thap_phan = float(input("Nhập số thập phân: "))

# Lấy phần nguyên
phan_nguyen = int(so_thap_phan)

so_thap_phan = so_thap_phan*1000

# Lấy phần thập phân
phan_thap_phan = so_thap_phan - phan_nguyen*1000

# Lấy 3 chữ số của phần thập phân
phan_thap_phan_3_chu_so = int(phan_thap_phan)

# In ra kết quả
print(f"Phần nguyên: {phan_nguyen}")
print(f"3 chữ số của phần thập phân: {phan_thap_phan_3_chu_so:03d}")

