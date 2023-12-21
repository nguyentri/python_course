'''Tìm tất cả các số chia hết cho 7 nhưng không chia hết cho 8 bằng python.
từ 1-99. Kết quả in thành chuỗi trên một dòng, cách nhau dấu phẩy.
Kiến thức cần có:
1. Vòng lặp for
2. Phép modulo
3. if else condition
4. str
4. Hàm Print
'''

#Cách 1
j=''
for i in range (1, 99):
  if ((i%7 == 0) and (i%8 != 0)):
    if (i == 7):
      j += str(i)
    else:
      j += ", " + str(i)
print (j)


#Cách 2
k=[]
for i in range (1, 99):
  if ((i%7 == 0) and (i%8!=0)):
    k.append(str(i))
print (', '.join(k))