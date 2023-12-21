#Viết chương trình hỏi tuổi của người dùng và 
#in ra xem họ là trẻ vị thành niên (<18), người lớn(>=18, < 65) hay người cao tuổi (>=65).
age = int(input("Nhập tuổi: "))
if(age < 18):
    print("Trẻ vị thành niên!")
elif(age >=18 and age < 65):
    print("Người lớn!")
else:
    print("Người cao tuổi!")
