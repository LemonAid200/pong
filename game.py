import pygame
from tkinter import Tk
import sys

 


#получить параметры экрана
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

winX = 1000
winY = 800
white  = (255,255,255)
flag=True
tupa=0

pygame.init()
win = pygame.display.set_mode((winX,winY))
pygame.display.set_caption("PONG")
clock = pygame.time.Clock()
sound = pygame.mixer.Sound('click.wav')
fail = pygame.mixer.Sound('fail.wav')
pygame.mixer.music.load('music.wav')

x = winX/2
y = winY/2
ballSpeed = 7
xVectorBallSpeed = float(1)
yVectorBallSpeed = float(1)

Player1 = winY/2
Player2 = winY/2
playerSpeed = 10*2
Score1 = 0
Score2 = 0
counter = 0

run = True

while(run):
    clock.tick(60)

    if ((x < 65 and x > 45 and y<=Player1+125 and y>=Player1-25 and xVectorBallSpeed<0)):
        xVectorBallSpeed *= -1
        x+=5*xVectorBallSpeed
        sound.play()
        counter+=2
    elif((x > winX - 65 and x < winX-45 and y <=Player2+125 and y>=Player2-25 and xVectorBallSpeed > 0)):
        xVectorBallSpeed *= -1
        x+=5*xVectorBallSpeed
        sound.play()
        counter+=3
    elif(x>winX): 
        Score1+=1       
        x = winX/2        
        fail.play()
        counter=0
        ballSpeed = 0                       
    elif(x<0):
        x = winX/2
        Score2+=1        
        fail.play()
        counter=0
        ballSpeed = 0
  
    
    if (y > winY -50 or y < 50):
        yVectorBallSpeed *= -1
    
    x += ballSpeed*xVectorBallSpeed
    y += ballSpeed*yVectorBallSpeed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    
    #кнопки
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if (Player2 > 50):
            Player2-=playerSpeed
    if keys[pygame.K_DOWN]:
        if (Player2 < winY- 150):        
            Player2+=playerSpeed
    if keys[pygame.K_w]:
        if (Player1 > 50):
            Player1-=playerSpeed
    if keys[pygame.K_s]:
        if (Player1 < winY -150):
            Player1+=playerSpeed
    if keys[pygame.K_m]:
        if flag:
           pygame.mixer.music.play()
           flag=False
        else:
           pygame.mixer.music.pause()
           flag=True
           tupa+=15
  
    if keys[pygame.K_v]:
        if (winX == 1000):
            win = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            winX = width
            winY = height
            pygame.time.delay(500)
        else:
            winX = 1000
            winY = 800
            win = pygame.display.set_mode((winX,winY))
            pygame.time.delay(500)
    if keys[pygame.K_SPACE]:
        if ballSpeed == 0:
            ballSpeed+=7
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        root.destroy()

    
    #отрисовка
    win.fill((0,0,0))
    pygame.draw.rect(win,white, (30, Player1, winX/50, winY/8))
    pygame.draw.rect(win, white, (winX-50, Player2, winX/50, winY/8))
    pygame.draw.line(win, white, (winX/2,0),(winX/2,winY), 5)
    pygame.draw.circle(win, white, (x, y) ,winX/100)
  
    #конец
    if (Score1 == 12 or Score2 == 12):
        ballSpeed = 0
        textsurface3 = myfont.render("That's all folks!", False, white)
        win.blit(textsurface3,(winX/2+5, 200))
        if keys[pygame.K_SPACE]:
            if ballSpeed == 0:
                ballSpeed+=7
                if Score1 == 12 or Score2 == 12:
                    Score1=0
                    Score2=0

    #счет
    pygame.font.init() 
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    textsurface = myfont.render(str(Score1), False, white)
    win.blit(textsurface,(winX/2-80, 0))
    textsurface2 = myfont.render(str(Score2), False, white)
    win.blit(textsurface2,(winX/2+50, 0))

    pygame.display.update()
    if (counter > 5):
        counter =0
        ballSpeed +=1

  
    

pygame.quit()
root.destroy()
