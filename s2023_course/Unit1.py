#Nhập 1 số thực từ bàn phím và in ra phần nguyên in phần thập phân 3 chữ sô
# Ví dụ nhập 10.001, kết quả:
# "Phần nguyên: 10"
# "Phần thập phân: 001"
import math 
#Nhập số thực a bất kì 
a = float(input())
(phan_thap_phan, phan_nguyen) = math.modf(a)
phan_thap_phan = int(phan_thap_phan*1000)
phan_nguyen = int(phan_nguyen)
print (phan_thap_phan, phan_nguyen)
