nums = [1, 2, 3, 4]
#1a. Truy cập list chỉ mục âm
print(nums[-4], nums[-3], nums[-2], nums[-1])
#Tương đương với
#nums [-4] == nums [0], nums [-3] == nums [1],
#nums [-2] == nums [2], nums [-1] == nums [3]
print(nums[0], nums[1], nums[2], nums[3])

#1b. Truy xuất nhiều phần tử trong list
#bằng cách đưa vào chỉ mục đầu tiên và chỉ mục kết thúc cách nhau dấu :
#Sẽ trả về phần tử ở chỉ mục đầu tiên và trước chỉ mục kết thúc.
print(nums[1:3]) #Kết quả [2, 3] 
#Kết luận list có n phần tử thì -1 là chỉ mục của phần tử cuối cùng
#0 là chỉ mục của phần tử đầu tiên.

#2.Thêm phần tử vào list vaò sau phần tử cuối cùng dùng hàm append
nums.append([5, 6])
print(nums)
print("chiều dài list/số phần tử của list", len(nums))

#3. Chèn 1 phần tử vào giữa của list, dùng hàm insert
#Cú pháp: list.insert(<chỉ mục cần thêm>, <giá trị>)
nums.insert(1, "6")
print(nums)
print(nums[2])

#4. Tìm chiều dài của list, dùng hàm len
print("chiều dài list/số phần tử của list", len(nums))

#5. Xóa 1 phần tử trong list bằng hàm remove()
# Cần đưa chính xác phần tử cần xóa
print(nums)
nums.remove("6")
print(nums)

#6. Xóa 1 list dùng hàm clear()
nums.clear()
print(nums)

#7. Copy 1 list
list1 = ['a', 'b', 'c']
# Phép gán khi thao tác trên biến được gán vào sẽ làm thay đổi
# list ban đầu được gán.
#list2 = list1 
list2 = list1.copy()
list2.append('d')
print(list1)
print(list2)

#8. Nối hai list dùng phép +
list3 = list1 + list2
print(list3)

#9. Đếm số lần xuất hiện của 1 phần tử trong list
a_time = list3.count('a')
print(a_time)
e_time = list3.count('e')
print(e_time)
if(not e_time) :
    list3.append('e')
print(list3)

#10. Đảo thứ tự trong list
list3.reverse()
print(list3)

#11. Xóa và trả về phần tử cuối cùng của list
elm = list3.pop()
print(elm)
print(list3)
elm = list3.pop()
print(elm)
print(list3)
elm = list3.pop()
print(elm)
print(list3)
