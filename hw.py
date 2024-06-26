import pygame
import random
pygame.init()
WIDTH=600
HEIGHT=500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
flower=pygame.image.load("flower.png")
flowerx=250
flowery=300
bee=pygame.image.load("bee.png")
grass=pygame.image.load("grass.png")
beex=175
beey=400
score=0
score2=0
game=True
font=pygame.font.SysFont("Times new Roman",72)
text1=font.render(str(score),1,"green")
text2=font.render(str(score2),1,"green")
text3=font.render(("GAME OVER!!!"),1,"tomato")
brect=pygame.Rect(beex,beey,5,5)
frect=pygame.Rect(flowerx,flowery,64,64)
while True:
    screen.fill("cornflower blue")
    screen.blit(grass,(0,0))
    screen.blit(flower,(flowerx,flowery))
    screen.blit(bee,(beex,beey))
    screen.blit(text1,(15,15))
    screen.blit(text2,(550,15))
    if game==False:
        screen.fill("lightsage")
        screen.blit(text3,(400,250))
    for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    beey=beey-15
                if event.key==pygame.K_DOWN:
                    beey=beey+15
                if event.key==pygame.K_LEFT:
                    beex=beex-15
                    #Collect pictures for your game
                if event.key==pygame.K_RIGHT:
                    beex=beex+15
                
           
        
    if bee.get_rect().collidepoint(flowerx,flowery):
        print("collide")
        flowerx=random.randint(50,475)
        flowery=random.randint(50,350)
        score=score+1
    pygame.display.update()
