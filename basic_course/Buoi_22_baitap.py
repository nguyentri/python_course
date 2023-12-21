#Tìm tất cả vị trí của giá trị nhập vào trong list số thực
#Giá trị tìm cho vị trí bất kì n
#Đầu vào: n nhập vào và danh sách lst
#Đầu ra: danh sách lưu vị trí số cần tìm
n = float(input("Nhập giá trị cần tìm trong list: "))
lst = [4.1, 5.0, 70, 8.1, 1.1, 1.1, 1.1]
#Khai báo biến đầu ra
pos = []
#Đặt biến đếm cho vòng lặp while, là chỉ số của lst
i = 0
#Duyệt tất cả phần tử trong list bằng vòng lặp while
while (i < len(lst)):
  #Lấy từng phần tử của list theo chỉ số i
  m = lst[i]
  #Kiểm tra giá trị của phần tự hiện tại có bằng giá trị cần tìm hay không
  if (m == n):
    pos.append(i)
  #Tăng chỉ số của list
  i = i + 1

if (not pos):
  print ("Không tìm thấy vị trí nào của n =", n)
else:
  print ("Các vị trị của n = ", n, "trong list là:", pos)

