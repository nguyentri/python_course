#Tạo một danh sánh số bất kì ít nhất 5 phần tử
#In list và chiều dài của list
nums = [5, 3, 2, 1, 0]
#và tìm giá lớn nhất và nhỏ nhất của list (dùng hàm max(<list đưa vào), min)
#In ra max, min
max_num = max(nums)
print(max_num)
min_num = min(nums)
print(min_num)
#In phần tử ở giữa bằng chỉ mục âm
print(nums[-3])
#In nhiều phần tử bằng cách đưa vào chỉ mục đầu tiên và chỉ mục kết thúc
print(nums[-4:-1])
#Sắp xếp thứ tự tăng dần = hàm sort (<list>.sort) và in ra kết quả
nums.sort()
print(nums)
#hoac dung hàm sorted
new_nums = sorted(nums)
print(new_nums)
