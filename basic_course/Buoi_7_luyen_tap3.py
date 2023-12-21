#Viết chương trình máy tính giá sản phẩm tự động sau khi đã áp dụng giảm giá. 
#Hỏi người dùng về giá sản phẩm (theo đơn vị đô la $),
#Cho biết:
#nếu giá lớn hơn hoặc bằng 20$ thì giảm 20%,
#nhỏ hơn 20$ lớn hơn 10$ thì giảm 10%
#Còn lại sẽ giảm 5%

#Bước 1: #Hỏi người dùng về giá sản phẩm (theo đơn vị đô la $)
price = float(input("Nhập giá sản phẩm $: "))
print("Giá sản phẩm là", price, "$")
if (price >= 20) :
    price = price - (price * 20/100) # = 0.8 * price
elif (price > 10 ) :
    price = price * 0.9  #(1 - 10/100)
else:
    price = price * 0.95 #(1- 5/100)
print("Giá sau khi giảm", price, "$")
      
