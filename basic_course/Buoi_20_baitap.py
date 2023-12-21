#Dùng vòng lặp while để tìm vị trí số "1" đầu tiên trong lst sau
#Đầu ra: vị trí số "1" là chỉ số của phần tử số 1 trong list
#Có vẽ sơ đồ ý tưởng dùng drawio
lst = [4, 5, 7, 8, 1, 3, 1]
#Đặt biến đếm cho vòng lặp while
i = 0
#Giá trị tìm cho vị trí bất kì n
n = 3
#Vòng lặp sẽ chạy từ 0 đến chiều dài của list và tới khi tìm thấy số 1
#Tại mỗi vòng lặp, chúng ta kiểm tra xem phần tử tại vị trí i có bằng 1 hay không.
#Nếu bằng 1, điều kiện ở while sai, chúng ta thoát khỏi vòng lặp.
print ("vị trí ", i, "Giá trị", lst[i])
while ((i < len(lst)) and (lst[i] != n)):
  #Tăng biến i lên một để lấy giá trị tiếp theo của danh sách nếu chưa tìm thấy số 1
  i = i + 1
  print ("vị trí ", i, "Giá trị", lst[i])

print ("Vị trí số" ,n, "đầu tiên là: ", i)
