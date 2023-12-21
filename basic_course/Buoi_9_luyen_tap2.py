#Viết chương trình nhập vào điểm toán, điểm văn, và điểm tiếng anh.
#Xếp loại A, B, C theo điểm trung bình toán văn anh nhập vào với toán nhân hệ số 2 
#– Nếu điểm trung bình >=8 =>Xếp loại A
#– Nếu điểm trung bình >= 6 và < 8 => Xếp loại B
#– Nếu điểm trung bình <6 => Xếp loại C
toan = float(input("Nhập điểm toán: "))
van = float(input("Nhập điểm văn: "))
anh = float(input("Nhập điểm tiếng anh: "))

if (toan < 0 or toan > 10):
    print("Nhập sai điểm toán!")
elif(van < 0 or van > 10):
    print("Nhập sai điểm văn!")
elif(anh < 0 or anh > 10):
    print("Nhập sai điểm tiếng anh!")
else:
    tb = (toan*2 + van + anh)/4
    if(tb >= 8):
        print("Xếp loại A!")
    elif(tb >= 6 and tb <8):
        print("Xếp loại B!")
    else: #tb < 6
        print("Xếp loại C!")
