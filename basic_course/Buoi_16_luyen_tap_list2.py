
# Kiểm tra xem một list có rỗng không, sử dụng điều kiện
list1 = [1, 2]
list1.clear() # tương đương với list1 = []
print(list1)
# Cách 1:
if not list1:
    print ("List rỗng")
else:
    print ("List có phần tử!")

# Cách 2:
if list1 == []:
    print ("List rỗng")
else:
    print ("List có phần tử!")

# Cách 3:
if len(list1) == 0:
    print ("List rỗng")
else:
    print ("List có phần tử!")

# Tạo một list chứa các số nguyên từ 1 đến 5;
list2 = list(range(1, 6))
print (list2)

#Bài 1: Điền ? để xác định số phần tử của list là chẵn hay lẻ
my_list = [2, 4, 6, 8, 10]
if len(my_list) % 2 == 0:
    result = "Số phần tử của list là chẵn!"
else:
    result = "Số phần tử của list là lẻ!"
print(result)