#Phép and, trả True về nếu tất cả các biểu thức đều đúng
#Ngược lại là False
x = 2
print(x < 2 and x < 5) #False
print(x < 3 and x < 5) #True
print(x < 2 and x < 1) #False
print(x < 3 and x < 1) #False

#Phép or, trả về True nếu một trong các biểu thức so sánh là đúng
print(x < 1 or x < 2 or x == 2) # True vì x == 2 là đúng
print(x < 1 or x < 2 or x != 2) # False vì tất cả đều sai

#Phép not, trả về giá trị ngược lại của biến đó,
# nếu đang là True thì trả False, nếu đang là False thì trả về True
x = True
y = not x
x = not y
print(f"x, y : {x} {y}")
#Cach in dung dau ,
print("x, y: ", x, y)