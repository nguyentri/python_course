#Kiểm tra tuổi nghỉ hưu với giới tính nhập vào vào số tuối
#Biết nam nghỉ hưu ở tuổi 60, nữ nghỉ hưu ở tuổi 56
#In ra kết quả là "Đủ tuổi nghỉ hưu!" hoặc "Chưa đủ tuổi nghỉ hưu!"
gioitinh = input("Nhập giới tính nam/nu:")
tuoi = int(input("Tuổi: "))
if (gioitinh == "nam"):
    if (tuoi >= 60):
        print("Đủ tuổi nghỉ hưu!")
    else:
        print("Chưa đủ tuổi nhỉ hưu:")
elif (gioitinh == "nu"):        
    if (tuoi >= 56):
        print("Đủ tuổi nghỉ hưu!")
    else:
        print("Chưa đủ tuổi nhỉ hưu:")
else:
    print("Nhập sai giới tính!")
