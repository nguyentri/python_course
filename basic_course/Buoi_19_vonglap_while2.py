#Tính tổng tất các phần tử trong 1 list tạo từ số
#nguyên dương nhập vào dùng vòng lặp while
# Bước 1: xác định đầu vào, đầu ra và xem xét không hợp lệ của đầu vào
#  Đầu vào: nhập 1 số nguyên
#  Đầu ra: tổng 1 list tạo từ số nguyên nhập vào
#  Xem xét đầu vào hợp lệ: Yêu cầu số nguyên dương, khác thì yêu cầu nhập lại
# Bước 2: Xác định những bước trung gian để chuyển đổi đầu vào thành đầu ra bằng cách xác định, tính toán những cái không rõ trong đầu ra
#  Tạo list từ số nguyên nhập vào
#  Tính tổng các phần tử theo chiều dài của list

def sum_list():
    count = 0
    sum = 0
    # Xác định đâ
    n = input("Nhập số phần tử của list:")
    n = int(n)
    if (n <= 0):
        print ("Nhập số nguyên dương")
    else:
        lst = list(range(1, n+1))
        print (lst)
        # Tương đương hàm sum
        while(count < len(lst)):
            sum = sum + lst[count]
            count = count + 1
        print(sum)

#Gọi hàm để chạy chương trình
sum_list()
