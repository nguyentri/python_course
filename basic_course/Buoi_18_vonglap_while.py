#Cấu trúc:
# Nếu điều kiện đúng thực hiện các biểu thức thụt vào
# và lặp lại kiểm tra điều kiện
# Nếu sai thoát khỏi vòng lặp
# while <điều kiện>:
#   <Biểu thức 1>
#...<Biểu thức n>

#Ví dụ 1: In "Hello!" 10 lần
count = 0
# Kiểm tra count nhỏ hơn 10 hay không, nếu nhỏ hơn 10 thì tiếp tục in Hello
# Nếu khác thoát vòng lặp while, kết thúc chương trình
while count < 10:
    count = count + 1
    print(count, "Hello!")

#Ví dụ 2: Tính tổng từ 1 tới n, với n là số nguyên dương nhập vào
n = int(input("Nhập 1 số nguyên dương: "))
count = 0
sum = 0
while count < n :
    count = count + 1
    sum = sum + count

print ("Tổng từ 1 tới n là:", sum)
