#Tìm vị trí tên mình trong danh sách lớp
ds_lop = ["Hải", "Tú Anh", "Dori", "Quân", "Vũ", "Minh", "Tú", "Thiên", "Sang", "Hoàn"]

#Đặt biến đếm cho vòng lặp while
i = 0
#Giá trị tìm
n = "Hoàn"
#Vòng lặp sẽ chạy từ 0 đến chiều dài của list và tới khi tìm thấy tên mình
#Tại mỗi vòng lặp, chúng ta kiểm tra xem phần tử tại vị trí i có bằng tên mình hay không.
#Nếu bằng tên mình, điều kiện ở while sai, chúng ta thoát khỏi vòng lặp.
#print ("Vị trí ", i, "Tên ", ds_lop[i])
while ((i < len(ds_lop)) and (ds_lop[i] != n)):
  #Tăng biến i lên một để lấy giá trị tiếp theo của danh sách nếu chưa tìm thấy số 1
  i = i + 1
if (i == len(ds_lop)):
  print("Không tìm thấy tên")
else:
  print ("Vị trí tên của mình là : ", i)

# Cách thoát vòng while = break
i = 0
n = "Sang"
while (i < len(ds_lop)):
  #Tăng biến i lên một để lấy giá trị tiếp theo của danh sách nếu chưa tìm thấy tên
  m = ds_lop[i]
  if (m == n):
    break
  else:
    i = i + 1
if (i == len(ds_lop)):
  print("Không tìm thấy tên")
else:
  print ("Vị trí tên của mình là : ", i)