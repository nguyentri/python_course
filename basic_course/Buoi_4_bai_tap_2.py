#Nhập vào 3 số float a, b, c. Tính và in ra d = (a + b)^c
#Nếu d là số trong khoảng từ 100 - 200 thì in ra True, ngược lại in ra False
a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
c = float(input("Nhập c:"))
d = (a + b)**c
print(d)
ketqua = d > 100 and d < 200
print(ketqua)