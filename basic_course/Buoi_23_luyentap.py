#Tìm tất cả vị trí của các số chia hết cho 2 trong list số nguyên
#Đầu vào: danh sách lst
#Đầu ra: danh sách lưu vị trí số cần tìm chia hết cho 2
n = 2
lst = [2, 3, 4, 8, 5, 3, 1] #=>Mong đợi kết quả in ra 0, 2, 3
#Khai báo biến đầu ra
pos = []
#Đặt biến đếm cho vòng lặp while, là chỉ số của lst
i = 0
#Duyệt tất cả phần tử trong list bằng vòng lặp while
while (i < len(lst)):
  #Lấy từng phần tử của list theo chỉ số i
  m = lst[i]
  #Kiểm tra giá trị của phần tự hiện tại có bằng giá trị cần tìm hay không
  if (m % n == 0):
    pos.append(i)
  #Tăng chỉ số của list
  i = i + 1

if (not pos):
  print ("Không tìm thấy vị trí nào chia hết cho", n)
else:
  print ("Các vị trị chia hết ", n, "trong list là:", pos)

