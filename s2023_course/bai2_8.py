#Xác định loại tam giác 
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

#if (a == b) and (b == c):
if (a == b == c):
    print ("Tam giac deu")
elif (a == b):
    print ("Tam giac can")
elif (b == c):    
    print ("Tam giac can")
elif (a == c):
    print ("Tam giac can")
elif (a*a == (b*b + c*c)):
    print ("Tam giác vuông cạnh huyền a!")
elif (b*b == (a*a + c*c)):
    print ("Tam giác vuông cạnh huyền b!")
elif (c*c == (a*a + b*b)):
    print ("Tam giác vuông cạnh huyền c!")    
else:
    print ("Tam giác không xác định!")
