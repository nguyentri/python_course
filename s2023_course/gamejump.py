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
FPS = 60 #khung hình trên giây, giá trị càng cao chuyển động càng mượt
fpsClock = pygame.time.Clock()
#Chiều rộng cửa sổ game
WINDOW_WIDTH  = 960
#Chiều cao cửa sổ game
WINDOW_HEIGHT = 480
#Tạo biến window với chiều rộng, chiều cao
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#Hiển thị tên game
pygame.display.set_caption('Game Đầu Tay')
#game over font
font = pygame.font.Font(None, 48)
game_over_text = font.render("Game Over", True, (255, 0, 0))
#Đóng gói chương trình game bằng 1 hàm
def gamedautay () :
  # Khai báo biến gắn True - luôn luôn đúng
  charW = 25
  charH = 40
  charX = 0
  charY = WINDOW_HEIGHT - charH
  charV = 5
  recW = 50
  recH = 180
  recX = 200
  recY = WINDOW_HEIGHT - recH
  is_game_over = False
  is_change_bg = False
  is_jumping = False
  jump_count = 10
  char = pygame.image.load('char.jpg')
  char = pygame.transform.scale(char, (charW, charH))
  # Hình nền của game
  bgimage = pygame.image.load("background.jpg")
  bgimage = pygame.transform.scale(bgimage, (WINDOW_WIDTH, WINDOW_HEIGHT))

  # Vòng lặp chạy game luôn chạy vì looping == True
  # Chương trình sẽ chạy lặp lại từ lệnh sau vòng while tới kết thúc của vòng lặp
  # và chạy lại tới khi có sự kiện thoát chương trình
  while True :
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
    # Vẽ hình nền
    WINDOW.blit(bgimage, (0, 0))
    #Lưu nút nhấn từ bàn phím
    pressed = pygame.key.get_pressed()
    if (not is_game_over):
      #Kiểm tra xem nút nhấn mũi tên bên phải > 
      if (pressed[K_RIGHT]):
          # Nếu đúng tăng tọa độ của nhân vật lên 3 mỗi lần bấm phím
          charX = charX + charV
          #Nếu tọa độ nhân vật theo chiều ngang vượt khung hình thì reset về 0
          if (charX >= WINDOW_WIDTH):
              charX = 0
              if (not is_change_bg):
                is_change_bg = 1
              else:
                is_change_bg = 0
      #Kiểm tra nút nhấn là mũi tên bên trái hay không
      if (pressed[K_LEFT]):
      #Kiểm tra tọa độ x của nhân vật lớn hơn 3 hay không
        if (charX >= charV):
          # Nếu lớn hơn 3 giảm tọa độ để di chuyển trái
          charX = charX - charV
        else:
          # Nếu khác di chuyển nhân vật tới góc phải
          charX = WINDOW_WIDTH
      # Di chuyển xuống
      if (pressed[K_DOWN]):
        charY = charY + charV
        if (charY >= WINDOW_HEIGHT):
          charY = 0
      # Di chuyển lên
      if (pressed[K_UP]):
        if (charY >= charV):
          charY = charY - charV
        else:
          charY = WINDOW_HEIGHT
      # Nhảy
      if not is_jumping:
          if pressed[K_SPACE]:
              is_jumping = True
      else:
          if jump_count >= -8:
              neg = 1
              if jump_count < 0:
                  neg = -1
              charY -= (jump_count ** 2) * 0.5 * neg
              jump_count -= 1
          else:
              is_jumping = False
              jump_count = 8

    #Khai báo biến hình chữ nhật tạo từ pygame
    #Hàm Rec cần đưa thông tin vị trí bắt đầu vẽ (đỉnh bên trái) và chiều rộng chiều ngang của hình chữ nhật
    rec = pygame.Rect(recX, #Khoảng cách từ đỉnh bên trái của hình chữ nhật theo chiều ngang
                      recY,  #Khoảng cách từ đỉnh bên trái theo chiều dọc
                      recW, #Chiều rộng hình chữ nhật
                      recH) #Chiều dài hình chữ nhật
    #Màu hình chữ nhật
    recColor = (220, 30, 70)
    #Vẽ hình chữ nhật lên cửa sổ game
    pygame.draw.rect(WINDOW, recColor, rec)

    #Khai báo biến hình chữ nhật tạo từ pygame
    #Hàm Rec cần đưa thông tin vị trí bắt đầu vẽ (đỉnh bên trái) và chiều rộng chiều ngang của hình chữ nhật
    rec = pygame.Rect(recX, #Khoảng cách từ đỉnh bên trái của hình chữ nhật theo chiều ngang
                      0,  #Khoảng cách từ đỉnh bên trái theo chiều dọc
                      recW, #Chiều rộng hình chữ nhật
                      recH) #Chiều dài hình chữ nhật
    #Vẽ hình chữ nhật lên cửa sổ game
    pygame.draw.rect(WINDOW, recColor, rec)

    #Kiểm tra điều kiện game over
    if (charX >= recX + recW):
       is_game_over = False
    elif ((charX + charW >= recX) and (charY + charH >= recY)):
       is_game_over = True
    elif ((charX + charW >= recX) and (charY <= recH)):
       is_game_over = True

    # Hiển thị "Game Over"
    if (is_game_over):
      font = pygame.font.Font(None, 48)
      game_over_text = font.render("Game Over", True, (255, 0, 0))
      WINDOW.blit(game_over_text, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

    if (pressed[K_ESCAPE]):
      charX = 0
      charY = WINDOW_HEIGHT - charH
      is_game_over = False

    #Vẽ hình nhân vật lên cửa sổ game
    WINDOW.blit(char, (charX, charY))
    # Hiển thị thông tin cập nhật
    pygame.display.update()
    # Chạy cửa sổ game với fps đã gắn ở trên
    fpsClock.tick(FPS)

#Gọi hàm chạy chính của game
gamedautay()
