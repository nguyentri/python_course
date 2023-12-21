#Giá trị c = bao nhiêu
a = 30
b = 3
c = a%b
if(not c):
   c = b
   a = b
if(c != a):
   c = c + 1
else:
   c = c + 2
print(c)