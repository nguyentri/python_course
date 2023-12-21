import random

#Biến lưu tổng ván chơi
tongvanchoi = 1
#Biến lưu Tổng số ván bạn thắng
banthang = 0
#Biến lưu Tổng số ván bạn thua
banthua  = 0
#Biến lưu Tổng số ván bạn hòa
banhoa   = 0
#Biến lưu Tổng số ván bạn ra không hợp lệ
khonghople     = 0

print ("Đấu búa kéo Giấy với máy tính nào!")

# Vòng lặp vô tận để chạy game
while True:
  #In khoảng trống giữa các ván chơi
  print ("\n")
  print ("Ván chơi số:", tongvanchoi)
  danhsachbkg = ["Búa", "Kéo", "Giấy"]
  #Hàm random mỗi lần chạy sẽ chọn ngẫu nhiên 1 giá trị trong danh sách
  maytinhchon = random.choice(danhsachbkg)
  banchon   = input("Mời bạn ra Búa, Kéo hoặc Giấy: ")
  print ("Máy tính ra :", maytinhchon)
  print ("Bạn ra:", banchon)
  if (maytinhchon == "Búa"):
    if (banchon == "Búa"):
      print ("HÒA NHAU!")
      banhoa+=1
    else:
      if (banchon == "Giấy"):
        print ("BẠN THUA!")
        banthua+=1
      else:
        if (banchon == "Kéo"):
          print ("BẠN THẮNG!")
          banthang+=1
        else:
          print ("Không tính, Chỉ chọn Kéo hoặc Búa hoặc Giấy!")
          khonghople+=1

  if (maytinhchon == "Kéo"):
    if (banchon == "Kéo"):
      print ("HÒA NHAU!")
      banhoa+=1
    else:
      if (banchon == "Giấy"):
        print ("BẠN THUA!")
        banthang+=1
      else:
        if (banchon == "Búa"):
          print ("BẠN THẮNG!")
          banthua+=1
        else:
          print ("Không tính, Chỉ chọn Kéo hoặc Búa hoặc Giấy!")
          khonghople+=1

  if (maytinhchon == "Giấy"):
    if (banchon == "Giấy"):
      print ("HÒA NHAU!")
      banhoa+=1
    else:
      if (banchon  == "Búa"):
        print ("BẠN THẮNG!")
        banthang+=1
      else:
        if (banchon == "Kéo"):
          print ("BẠN THUA!")
          banthua+=1
        else:
          print ("Không tính, Chỉ chọn Kéo hoặc Búa hoặc Giấy!")
          khonghople+=1

  print ("Tổng ván chơi: ", tongvanchoi, " ván")
  print ("Bạn thắng:", banthang, " ván")
  print ("Bạn thua :", banthua, " ván")
  print ("Bạn hòa  :", banhoa, " ván")
  print ("Ván chơi không hợp lệ  :", khonghople, " ván")
  tongvanchoi = tongvanchoi + 1
