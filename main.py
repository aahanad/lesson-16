import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
player1=pygame.image.load("C:\Aahana\Game Dev 2\lesson 6\Things\player 1.png")
player2=pygame.image.load("C:\Aahana\Game Dev 2\lesson 6\Things\player 2.png")
bg=pygame.image.load("C:\Aahana\Game Dev 2\lesson 6\Things\sky.png")
player1x=50
player2x=700
player1y=300
player2y=300
bg=pygame.transform.scale(bg,(800,600))
player1=pygame.transform.scale(player1,(50,50))
player2=pygame.transform.scale(player2,(50,50))
border=pygame.Rect(395,0,10,800)
player1=pygame.transform.rotate(player1,90)
player2=pygame.transform.rotate(player2,270)

while True:
    screen.blit(bg,(0,0))
    screen.blit(player1,(player1x,player1y))
    screen.blit(player2,(player2x,player2y))
    pygame.draw.rect(screen,"black",border)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                player1y=player1y-15
            if event.key==pygame.K_DOWN:
                player1y=player1y+15
            if event.key==pygame.K_LEFT:
                player1x=player1x-15
            if event.key==pygame.K_RIGHT:
                player1x=player1x+15
        
            if event.key==pygame.K_w:
                player2y=player2y-15
            if event.key==pygame.K_a:
                player2y=player2y+15
            if event.key==pygame.K_s:
                player2x=player2x-15
            if event.key==pygame.K_d:
                player2y=player2y+15
                #Make your own game with a choice of background and cartoon character