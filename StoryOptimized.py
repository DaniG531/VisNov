from io import StringIO
import sys, pygame
import json
pygame.init()

size = width, height = 1280, 900
black = (0, 0, 0)
white = (255, 255, 255)
screen = pygame.display.set_mode(size)
TextFont = pygame.font.Font('freesansbold.ttf', 16)

A = True
Doc = open("jsons/Menuinicial.json")
p = Doc.read()
data = json.loads(p)
while A:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                seleccion = 0
            if event.key == pygame.K_LEFT:
                seleccion = 1
            if event.key == pygame.K_r:
                data = open("jsons/Menuinicial.json")
                p = Doc.read()
                data = json.loads(p)
            if event.key == pygame.K_SPACE:
                A = False

            Doc = open(data["opciones"][seleccion]["node"])
            p = Doc.read()
            data = json.loads(p)
    background = pygame.image.load(data["imagen"])
    y = 750
    screen.fill(black)
    screen.blit(background, (0, 0))
    for i in data["textos"]:
        TextDisplay = TextFont.render((i), True, white)
        screen.blit(TextDisplay, (60, y))
        y += 20
    y = 870
    for i in data["opciones"]:
        TextDisplay = TextFont.render((i["texto"]), True, white)
        screen.blit(TextDisplay, (60, y))
        y += 20

    pygame.display.flip()