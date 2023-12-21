#Thư viện pygame
import pygame
import os
pygame.init ()

p=0.2 #Hằng trọng lực
bird_y=0 #Tọa độ y của bird
score=0 #Khởi tạo điểm
#Score
#C:\Python game\game1\FileGame\04B_19.TTF
path_game1 = os.path.abspath(__file__)
dir_game1 = os.path.dirname(path_game1)

game_font=pygame.font.Font(dir_game1 + '\\FileGame\\04B_19.TTF', 40)
def score_view():
    score_f=game_font.render(str(int(score)),True,(255,255,255))
    score_hcn=score_f.get_rect(center=(200,100))
    screen.blit (score_f,score_hcn)
#Tiêu đề và icon game
pygame.display.set_caption('Game 1')
icon=pygame.image.load(dir_game1 + '\\FileGame\\assets\\yellowbird-downflap.png')
#Thêm background cho game
bg=pygame.image.load(dir_game1 + '\\FileGame\\assets\\background-night.png')
bg=pygame.transform.scale2x(bg)
fl=pygame.image.load(dir_game1 + '\\FileGame\\assets\\floor.png')
fl=pygame.transform.scale2x(fl)
fl_x=0
pygame.display.set_icon(fl)
#Cửa sổ game
screen=pygame.display.set_mode((432,768))
#Bird
bird=pygame.image.load(dir_game1 + '\\FileGame\\assets\\yellowbird-midflap.png')
bird=pygame.transform.scale2x(bird)
bird_hcn=bird.get_rect(center=(100,368))
#Vòng lặp xử lý game
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                bird_y=-8
    screen.blit(bg,(0,0))
    fl_x-=1
    screen.blit(fl,(fl_x,600 ))
    screen.blit(fl,(fl_x+432,600 ))
    if fl_x==-432:
        fl_x=0
    #Bird
    screen.blit(bird,bird_hcn)
    bird_y+=p
    bird_hcn.centery+=bird_y
    score+=0.01
    score_view()
    pygame.display.update()