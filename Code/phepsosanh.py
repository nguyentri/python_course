'''
Lệnh điều kiện if else trong python:

Giải thích lệnh if và else:
  Lệnh if được sử dụng để kiểm tra một điều kiện.
    Nếu điều kiện bên trong ngoặc sau if là đúng(true) hoặc khác 0 thì những dòng lệnh phía dưới của khối if (những dòng lệnh lùi vào một khoảng giống nhau) sẽ được thực thi,
    Nếu không nó sẽ bị bỏ qua và thực thi lệnh else nếu có.
  Lệnh else chứa khối code mà thực thi nếu biểu thức điều kiện trong lệnh if là sai(false) hoặc bằng 0
  Thử các ví dụ sau để hiểu if và else

Cú pháp viết lệnh if else:
if (Biểu thức):
    lệnh 1
    lệnh 2
    ...
    lệnh n
else:
    lệnh 1
    lệnh 2
    ...
    lệnh m

Đoạn lệnh trên có thể hiểu nghĩa theo từng dòng là:
  if hiểu là nếu
    Dấu hai chấm (:) hiểu là thì
  else hiểu là nếu không

=> Nếu (Biểu thức) bằng 0 hoặc không đúng thì thực hiện lệnh 1 đến lệnh n
'''

'''
Cách dấu so sánh thường dùng trong "Biểu thức" lệnh if
  Dấu == dùng để so sánh bằng
   Dấu != dùng để so sánh khác nhau
   Dấu > dùng để so sánh lớn hơn
   Dấu < dùng để so sanh bé hơn
   Dấu >= dùng để so sánh lớn hơn hoặc bằng
   Dấu < dùng để so sanh bé hơn hoặc bằng
'''
# Ví dụ 1
# Kết quả in ra màn hình là: "a bằng 1 là đúng!"" vì a bằng 1 (a == 1) là đúng
a = 1
if (a == 1):
  print ("a bằng 1!")

# Ví dụ 2
# Thử đổi gán giá trị a = 2, thì sẽ không có thông tin in ra màn hình nữa vì lúc này a = 2 và việc so sánh 2 bằng 1 (2==1) là bị sai
a = 2
if (a == 1):
  print ("a bằng 1!")

# Ví dụ 3
# Thêm lệnh else để in thông tin ra màn hình nếu việc so sánh a băng 1 ở if là sai
# Kết quả in ra màn hình là: "a không bằng 1!" vì a được gán giá trị bằng 2 nên so sánh a bằng 1 (a == 1) là sai
a = 2
if (a == 1):
  print ("a bằng 1!")
else:
  print ("a không bằng 1!")
