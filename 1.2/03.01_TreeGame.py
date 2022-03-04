import pygame
import time

pygame.init()
screen=pygame.display.set_mode([500, 500])
pygame.display.set_caption("Tree Game")
screen.fill((255, 240, 245))

x=50
y=430
width=40
height=60
speed=5
run=True
   
screen.fill((255, 240, 245))

font=pygame.font.Font(None,20)
text=font.render("ЛКМ - дерево красное, ПКМ - дерево зеленое",True,[0,0,0])
textpos=(18,20)
screen.blit(text, textpos)

pygame.draw.polygon(screen, (185,122,87),[[250,100],[235,495],[265,495]])
pygame.draw.circle(screen,(34,177,76),[200,290],80)
pygame.draw.circle(screen,(181,230,29),[290,250],80)
pygame.draw.circle(screen,(34,177,76),[200,110],40)
pygame.draw.circle(screen,(181,230,29),[165,200],80)
pygame.draw.circle(screen,(34,177,76),[195,223],45)
pygame.draw.circle(screen,(34,177,76),[280,160],90)
pygame.display.update()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==1:
            pygame.draw.circle(screen,(178, 34, 34),[200,290],80)
            pygame.draw.circle(screen,(255,127,39),[290,250],80)
            pygame.draw.circle(screen,(178, 34, 34),[200,110],40)
            pygame.draw.circle(screen,(255,0,0),[165,200],80)
            pygame.draw.circle(screen,(178, 34, 34),[195,223],45)
            pygame.draw.circle(screen,(235,85,20),[280,160],90)
            pygame.display.update()

    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==3:
            pygame.draw.circle(screen,(34,177,76),[200,290],80)
            pygame.draw.circle(screen,(181,230,29),[290,250],80)
            pygame.draw.circle(screen,(34,177,76),[200,110],40)
            pygame.draw.circle(screen,(181,230,29),[165,200],80)
            pygame.draw.circle(screen,(34,177,76),[195,223],45)
            pygame.draw.circle(screen,(34,177,76),[280,160],90)
            pygame.display.update()
pygame.quit()
