import pygame
import math

pygame.init()
WIDTH = 800
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_in = [0, 0]
background_pictures = pygame.image.load("fon.jpg")
A = 400
B = 300
sun_in = [A - 90, B - 90]
sun_pictures = pygame.image.load("sun2.png")
pygame.display.set_icon(pygame.image.load("app.png"))
clock = pygame.time.Clock()
run = True
teta = []
name = []
distance = []
pictures = []
spisok = []
time = 0.5
teta = 1

with open('dannye.txt', encoding="UTF-8") as f:
    for line in f:
        name.append(line.split()[0])
        #teta.append(line.split()[1])
        distance.append(line.split()[2])
        pictures.append(line.split()[3])


"""class с даными по планетам:"""
class Planet():
    def __init__(self, name, distance, pictures):
        self.name = name
        #self.teta = float(teta)
        self.distance = float(distance)
        self.pictures = pictures
        x = 0
        y = 0

    def offset(self):
        global A, B, time, teta
        self.x = A + self.distance * math.cos(teta*time)
        self.y = B + self.distance * math.sin(teta*time)
        time += 0.1
        if self.name == "saturn":
            print(self.x, self.y)
        screen.blit(pygame.image.load(self.pictures), (self.x - 90, self.y - 90))


for i in range(len(name)):
    spisok.append(Planet(name[i], distance[i], pictures[i]))
print(spisok)
while run:
    clock.tick(5)
    pygame.display.update()
    screen.blit(background_pictures, background_in)
    screen.blit(sun_pictures, sun_in)
    for i in spisok:
        i.offset()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
