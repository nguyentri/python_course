#Trong python, "if" và 'else" là 2 câu lệnh được sử dụng theo cặp
#để xác định điều kiện đúng sai và thực hiện cách hành động khác nhau
#dựa trên giá trị của biểu thức,
# (1) if "biểu thức":
#   Nếu biểu thức đúng (True), thì các hành động trong khối if sẽ được thực hiện
#   Cú pháp: 
#   if "biểu thức":
        # hành động 1
        # hành động 2
        #...
        # hành động n (cùng lề bên trái)
#  (2) else:
#   Được sử dụng để xác định các hành động khi biểu thức trong if không đùng (False)
#   Cú pháp:
#   if "biểu thức":
        #Các hành động thực hiện khi biểu thức là đúng
    #else:
        #Các hành động thực thi khi biểu thức là không đúng
#Ví dụ
a = 10
b = 10
if (a < b):
    print("Số a nhỏ hơn b")
else:
    print ("Số a lớn hơn hoặc bằng với b")

# (3) elif dùng để thực thi khi biểu thức phía trước không đúng (False) 
# và thử kiểm tra trong biểu thức elif "biểu thức":
# cú pháp

if (a < b):
    print("Số a nhỏ hơn b")
elif (a == b):
    print("Số a bằng số b")
else:
    print("Số a lớn hơn số b")