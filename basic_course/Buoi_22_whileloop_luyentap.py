#Ví dụ 1: In "Hello!" 10 lần
count = 0
while True:
    count = count + 1
    # Kiểm tra count nhỏ hơn 10 hay không, nếu nhỏ hơn 10 thì tiếp tục in Hello
    if (count <= 10 ):
        print(count, "Hello!")
    # Nếu khác thoát vòng lặp while, kết thúc chương trình
    else:
        break

#Ví dụ 2: Tính tổng từ 1 tới n, với n là số nguyên dương nhập vào
n = int(input("Nhập 1 số nguyên dương: "))
count = 1
sum = 0
while True :
    # Kiểm tra count nhỏ hơn số nhập vào hay không, nếu đúng thì tăng count lên để tính tổng
    # Nếu khác thoát vòng lặp while, kết thúc chương trình
    if (count > n):
      break
    else:
      sum = sum + count
      count = count + 1

print ("Tổng từ 1 tới n là:", sum)
