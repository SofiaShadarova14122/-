import pygame
import random

spisok_kart = ['Туз','Король', 'Дама', 'Валет', 'Десятка', 'Девятка', 'Восьмерка', 'Семерка', 'Шестерка']
mast = ['Крести', 'Буби', 'Черви', 'Пики']
karta = [random.choice(spisok_kart)]
karta_mast = [random.choice(mast)]
print(karta_mast, ' ', karta)

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont("Arial", 25)
myfont1 = pygame.font.SysFont("Arial", 60)
screen = pygame.display.set_mode((600,700))
screen.fill((204,204,255))
clock = pygame.time.Clock()
run=True
x=140
y=400
a=0
b=0
frame=0

front = pygame.Surface((138, 210))
front.fill((255,255,255))
front.set_alpha(255)

cards = pygame.image.load( "рубашка.png").convert_alpha()

bubi = pygame.image.load( "Буби.png")
bubi.set_alpha(255)

bubi_flip = pygame.transform.flip(bubi, False, True)
bubi_flip.set_alpha(255)

chervy = pygame.image.load( "Черви.png")
chervy.set_alpha(255)

chervy_flip = pygame.transform.flip(chervy, False, True)
chervy_flip.set_alpha(255)

piki = pygame.image.load( "Пики.png")
piki.set_alpha(255)

piki_flip = pygame.transform.flip(piki, False, True)
piki_flip.set_alpha(255)

kresty = pygame.image.load( "Крести.png")
kresty.set_alpha(255)

kresty_flip = pygame.transform.flip(kresty, False, True)
kresty_flip.set_alpha(255)

chervy1 = pygame.image.load( "Черви1.png")
chervy1.set_alpha(255)

piki1 = pygame.image.load( "Пики1.png")
piki1.set_alpha(255)

bubi1 = pygame.image.load( "Буби1.png")
bubi1.set_alpha(255)

kresty1 = pygame.image.load( "Крести1.png")
kresty1.set_alpha(255)


if "Буби" in karta_mast:
    front.blit(bubi, (25, 5))
    if ("Туз" not in karta) and ("Король" not in karta) and ("Дама" not in karta) and ("Валет" not in karta):
        front.blit(bubi1, (43,65))
    front.blit(bubi_flip, (93, 182))
    color = (255,0,0)

if "Крести" in karta_mast:
    front.blit(kresty, (25, 5))
    if ("Туз" not in karta) and ("Король" not in karta) and ("Дама" not in karta) and ("Валет" not in karta):
        front.blit(kresty1, (43,65))
    front.blit(kresty_flip, (93, 182))
    color = (0,0,0)

if "Черви" in karta_mast:
    front.blit(chervy, (25, 5))
    if ("Туз" not in karta) and ("Король" not in karta) and ("Дама" not in karta) and ("Валет" not in karta):
        front.blit(chervy1, (43,65))
    front.blit(chervy_flip, (93, 182))
    color = (255,0,0)

if "Пики" in karta_mast:
    front.blit(piki, (25, 5))
    if ("Туз" not in karta) and ("Король" not in karta) and ("Дама" not in karta) and ("Валет" not in karta):
        front.blit(piki1, (43,65))
    front.blit(piki_flip, (93, 182))
    color = (0,0,0)


if "Десятка" in karta:
    label = myfont.render("10", 1, color)
    label_flip = pygame.transform.flip(label, True, True)
    front.blit(label, (3,3))
    front.blit(label_flip, (117, 179))

if "Девятка" in karta:
    label = myfont.render("9", 1, color)
    label_flip = pygame.transform.flip(label, True, True)
    front.blit(label, (6,4))
    front.blit(label_flip, (121, 179))

if "Восьмерка" in karta:
    label = myfont.render("8", 1, color)
    label_flip = pygame.transform.flip(label, True, True)
    front.blit(label, (6,4))
    front.blit(label_flip, (121, 179))

if "Шестерка" in karta:
    label = myfont.render("6", 1, color)
    label_flip = pygame.transform.flip(label, True, True)
    front.blit(label, (4,3))
    front.blit(label_flip, (117, 179))

if "Семерка" in karta:
    label = myfont.render("7", 1, color)
    label_flip = pygame.transform.flip(label, True, True)
    front.blit(label, (4,3))
    front.blit(label_flip, (117, 179))

if "Валет" in karta:
    label = myfont.render("J", 1, color)
    label_flip = pygame.transform.flip(label, True, True)
    front.blit(label, (6,4))
    front.blit(label_flip, (121, 179))
    label1 = myfont1.render("J", 1, color)
    front.blit(label1, (53,65))

if "Дама" in karta:
    label = myfont.render("Q", 1, color)
    label_flip = pygame.transform.flip(label, True, True)
    front.blit(label, (6,4))
    front.blit(label_flip, (121, 179))
    label1 = myfont1.render("Q", 1, color)
    front.blit(label1, (50,65))

if "Король" in karta:
    label = myfont.render("К", 1, color)
    label_flip = pygame.transform.flip(label, True, True)
    front.blit(label, (6,4))
    front.blit(label_flip, (121, 179))
    label1 = myfont1.render("K", 1, color)
    front.blit(label1, (50,65))

if "Туз" in karta:
    label = myfont.render("А", 1, color)
    label_flip = pygame.transform.flip(label, True, True)
    front.blit(label, (6,4))
    front.blit(label_flip, (121, 179))
    label1 = myfont1.render("A", 1, color)
    front.blit(label1, (50,65))


def drawWindow():

    pygame.display.update()

while run:
    clock.tick(25)
    screen.fill((204,204,255))

    screen.blit(cards, (x, y))
    screen.blit(cards, (x+40, y))
    screen.blit(cards, (x+80, y))
    screen.blit(cards, (x+120, y))
   

    if (x+a+160!=250) and (y+b!=50):
        screen.blit(cards, (x+160-a, y-b))
    else:
        screen.blit(cards, (250, 50))
    if (a!=50):
        a+=5
    if (b!=350):
        b+=35
    

    if frame>40:
        screen.blit(front, (252,52))


    frame+=1

    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    
    drawWindow()


pygame.QUIT