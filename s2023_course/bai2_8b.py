#Xác định loại tam giác 
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if (a == b) and (b == c):
    print ("Tam giác đều")
elif (a == b) or (b == c) or (a == c):
    print ("Tam giác cân")
elif (a*a == (b*b + c*c)) or (b*b == (a*a + c*c)) or (c*c == (a*a + b*b)):
    print ("Tam giác vuông")   
else:
    print ("Tam giác không xác định!")
