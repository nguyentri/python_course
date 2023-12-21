list1 = [1, 2, 3, 3, 4]

#6. lấy ra và xóa 1 phần tử dùng pop
rmv_elm = list1.pop(0)
print(rmv_elm)
print("#6", list1)

#7. Copy 1 list1 ra list2, print list2
list2 = list1.copy()
print ("#7", list2)

#8. Ghép list1 và list2, lưu vào list1, print list1
list1 = list1 + list2
print("#8", list1)

#9. Đếm số lần xuất hiện của số 3 trong list1 sau đó:
#   a. Nếu số lần xuất hiện lớn hơn 2, đổi số 3 đầu tiên thành 2
#   b. Nếu ít 2 hơn xóa đi số 3 đầu tiên
#   print list1
# (Gợi ý hàm index(<giá trị>) 
# sẽ lấy ra được chỉ mục đầu tiên giống <giá trị> )
# Đếm số lần dùng hàm count
times_3 = list1.count(3)
print("#9a:", times_3)
# Đếm số lần xuất hiện dùng hàm count
if times_3 > 2:
    # Lặp cho tới lúc không còn số 3 trong list
    while list1.count(3):
    # Lấy index của số 3 đầu tiên tìm được
        idx_3 = list1.index(3) # [1, 2, 3]
        list1[idx_3] = 2
else:
    list1.remove(3)
print(list1)

#10. Đảo thứ tự trong list
list1.reverse()
print ("#10", list1)

#11. Xóa và trả về 2 phần tử cuối cùng của list
list1.pop() # tương đương với list1.pop(-1)
list1.pop()
print("#11", list1)
list1 = [1, 2, 3]
#12. Tìm giá trị lớn nhất của list
print("#12", max(list1))
#13. Tìm giá trị nhỏ nhất của list
print("#13", min(list1))
#14. Tìm giá trị trung bình cộng của list
print("#14", sum(list1)/len(list1))
