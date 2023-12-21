#Định nghĩa: "list" là kiểu dữ liệu để lưu trữ một danh sách các phần tử
#cùng kiểu dữ liệu hoặc khác kiểu dữ liệu, có khả năng chứa nhiều phần tử
#trong 1 biến duy nhất.
#1 Khởi tạo list: List được khởi tạo bằng cặp dấu ngoạc vuông []
#các phần tử cách nhau bằng dấu ,
my_list = [1, 2, 3, 4, 5]
print(my_list)
#2 Phần tử của list: List có thể chứa bất kì kiểu dữ liệu nào bao gồm
#số nguyên, số thập phân, và cách danh sách khác
fruits = ["banana", 'apple', "orange"]
print(fruits)
    #index: 0 , 1,   2
list_mix = [1, "a", 2.0]
print(list_mix)
#3 Truy cập phần tử của list: truy cập các phần tử cuả list bằng chỉ mục(index)
#bắt đầu từ 0
phantudautien = list_mix[0]
phantuthu2 = list_mix[1]
#print(phantudautien, phantuthu2)
#print(type(phantudautien), type(phantuthu2))
#4 Thay đổi giá trị bằng chỉ mục
list_mix[1] = "b"
print(list_mix)
