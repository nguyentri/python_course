lst = [4, 5, 7, 8, 1, 3, 1]
i = 0
pos = []
n = int(input(""))
while (i < len(lst)):
  m = lst[i]
  if (m == n):
    pos.append(i)
  i = i + 1

if (not pos):
  print ("Không tìm thấy so")
else:
  print ("Vị trí la  : ", pos)
