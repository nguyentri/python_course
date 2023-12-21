import pygame, sys, random
from pygame.locals import *
pygame.init()
 
# Biến màu nền cửa sổ trò chơi
# Biểu diễn 3 giá trị màu RED, GREEN, BLUE
# Giá trị 0 là màu tối nhất (đen), 255 là biểu thị giá trị sáng nhất (trắng)
BACKGROUND = (255, 255, 255)
 
#
# Cài đặt game
#
#Max
MAX_BULLET = 5
FPS = 60 #khung hình trên giây, giá trị càng cao chuyển động càng mượt
fpsClock = pygame.time.Clock()
#Chiều rộng cửa sổ game
WINDOW_WIDTH = 800
#Chiều cao cửa sổ game
WINDOW_HEIGHT = 600
#Tạo biến window với chiều rộng, chiều cao
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Hiển thị tên game
pygame.display.set_caption('Game Đầu Tay')
#Đóng gói chương trình game bằng 1 hàm
def gamedautay () :
  # Khai báo biến gắn True - luôn luôn đúng
  looping = True
  charW = 100
  charH = 160
  charX = WINDOW_WIDTH - charW
  charY = 0
  char = pygame.image.load('char.jpg')
  char = pygame.transform.scale(char, (charW, charH))
  bullet_width = 10
  bullet_height = 20
  bullet_x = 50
  bullet_y = WINDOW_HEIGHT - 40
  move_x = [0, 0, 0, 0, 0]
  bullet_speed = 5
  bullets = []
  bullet_Idx = 0
  # Force (v) up and mass m.
  v = 8
  m = 2
  # Stores if player is jumping or not
  isjump = False
  # Vòng lặp chạy game luôn chạy vì looping == True
  # Chương trình sẽ chạy lặp lại từ lệnh sau vòng while tới kết thúc của vòng lặp
  # và chạy lại tới khi có sự kiện thoát chương trình
  for i in range(MAX_BULLET):
    move_x.append(0)

  while looping :
    # Lấy tất cả sự kiện từ người dùng, bấm bàn phím, click chuột,... 
    for event in pygame.event.get() :
      #Kiểm tra nếu bấm vào nút "x" trên giao diện để thoát game
      if event.type == QUIT :
        # Nếu đúng là nút "x", thoát pygame
        pygame.quit()
        # Thoát chương trình
        sys.exit()
    # Chạy cửa sổ game
    WINDOW.fill(BACKGROUND)

    #Khai báo biến hình chữ nhật tạo từ pygame
    #Hàm Rec cần đưa thông tin vị trí bắt đầu vẽ (đỉnh bên trái) và chiều rộng chiều ngang của hình chữ nhật
    #rec = pygame.Rect(400, #Khoảng cách từ đỉnh bên trái của hình chữ nhật theo chiều ngang
    #                  WINDOW_HEIGHT - 50,  #Khoảng cách từ đỉnh bên trái theo chiều dọc
    #                  30, #Chiều rộng hình chữ nhật
    #                  60) #Chiều dài hình chữ nhật
#
    #recColor = (220, 30, 70)
    #pygame.draw.rect(WINDOW, recColor, rec)
    #circleColor = (16, 12, 80)
    #pygame.draw.circle(WINDOW, circleColor, (WINDOW_WIDTH - 400, WINDOW_HEIGHT - 30), 30)
    pressed = pygame.key.get_pressed()
    if (pressed[K_RIGHT]):
      charX = charX + 3
      if (charX >= WINDOW_WIDTH):
        charX = 0
    if (pressed[K_LEFT]):
      if (charX >= 3):
        charX = charX - 3
      else:
        charX = WINDOW_WIDTH
    if (pressed[K_DOWN]):
      charY = charY + 3
      if (charY >= WINDOW_HEIGHT):
        charY = 0
    if (pressed[K_UP]):
      if (charY >= 3):
        charY = charY - 3
      else:
        charY = WINDOW_HEIGHT

    # if space bar is pressed
    #if pressed[pygame.K_SPACE]:
    #  # make isjump equal to True
    #  isjump = True
    #  if isjump :
    #    # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
    #    F =(1 / 2)*m*(v**2)
    #    # change in the y co-ordinate
    #    charY-= F
    #    if charY <= 0:
    #      charY = WINDOW_HEIGHT
    #    # decreasing velocity while going up and become negative while coming down
    #    v = v-1
    #    # object reached its maximum height
    #    if v<0:
    #        # negative sign is added to counter negative velocity
    #        m =-1
    #    # objected reaches its original state
    #    if v ==-8:
    #        # making isjump equal to false 
    #        isjump = False
    #        # setting original values to v and m 
    #        v = 8
    #        m = 2
    #if pressed[pygame.K_SPACE] and bullet_Idx < MAX_BULLET:
    #  bullet_rect = pygame.Rect(50, WINDOW_HEIGHT - 40, bullet_width, bullet_height)
    #  bullet_y = charY + char.get_height() / 2 + 5
    #  bullets.append(bullet_rect)
    #  move_x[bullet_Idx] = +1
    #  bullet_Idx = +1
    #  idx = 0
    #  for bullet in bullets:
    #    bullet_x += move_x[idx] * bullet_speed
    #    bullet.topleft = (bullet_x, bullet_y)
    #    idx = +1
    #    if bullet_x > charX + 10:
    #        pygame.draw.rect(WINDOW, (0, 120, 230), bullet)
    #
    #    if bullet_x > WINDOW_WIDTH:
    #        bullet_x = charX
    #        move_x[idx] = 0
    #
    #  if (bullet_Idx >= MAX_BULLET):
    #    bullet_Idx = 0
    #    bullets.clear()
    # creates time delay of 5ms
    #pygame.time.delay(5)
    WINDOW.blit(char, (700, 440))
    # Hiển thị thông tin cập nhật
    pygame.display.update()
    # Chạy cửa sổ game với fps đã gắn ở trên
    fpsClock.tick(FPS)

#Gọi hàm chạy chính của game
gamedautay()