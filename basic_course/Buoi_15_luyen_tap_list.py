# Nhập một chuỗi số bàn phím ít nhất 3 phần tử
list1 = input("Nhập chuỗi >= 3 phần tử: ")
print (list1)
# Phân tách từng ký tự nhập vào thành list
list1 = list1.split()
print (list1)
# Đổi cách phần tử trong list thành số
list1 = list(map(int, list1))
print (list1)

#1. print phần tử đầu tiên và cuối cùng của list1
print(list1[0], list1[-1]) # hoặc là print(list1[0], list1[len(list1) - 1])

#2. Chèn số 10 vào trước phần tử cuối cùng của list1, print list1
list1.append(10)
print(list1)

#3. Chèn 3 số 1, 2, 3 vào sau phần tử đầu tiên của list1, print list1
list1.insert(1, 1)
print (list1)
list1.insert(2, 2)
print (list1)
list1.insert(3, 3)
#print (list1)
#Cach khac
#list3 = [1 ,2 , 3]
#list2 = list([list1[0]]) + list3 + list1[1:]
#print(list2)

#4. print chiều dài của list, dùng hàm len(<list>)
print(len(list1))

#5. Xóa phần tử cuối cùng trong list1 bằng hàm remove(), print list1
list1.remove(10)
print(list1)

