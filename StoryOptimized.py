import sys, pygame
import json
pygame.init()

<<<<<<< HEAD
Restart = True
while Restart:
    size = width, height = 1280, 900
    black = (0, 0, 0)
    white = (255, 255, 255)
    screen = pygame.display.set_mode(size)

    def printtext(data):
        background = pygame.image.load(data["inicio"]["imagen"])

        TextFont = pygame.font.Font('freesansbold.ttf', 16)
        TextDisplay1 = TextFont.render((data["inicio"]["texto1"]), True, white)
        TextDisplay2 = TextFont.render((data["inicio"]["texto2"]), True, white)
        TextDisplay3 = TextFont.render((data["inicio"]["texto3"]), True, white)
        TextDisplay4 = TextFont.render((data["inicio"]["texto4"]), True, white)
        TextDisplay5 = TextFont.render((data["inicio"]["texto5"]), True, white)
        TextDisplay6 = TextFont.render((data["inicio"]["texto6"]), True, white)

        screen.fill(black)
        screen.blit(TextDisplay1, (60, 750))
        screen.blit(TextDisplay2, (60, 770))
        screen.blit(TextDisplay3, (60, 790))
        screen.blit(TextDisplay4, (60, 810))
        screen.blit(TextDisplay5, (60, 830))
        screen.blit(TextDisplay6, (60, 850))
        screen.blit(background, (0, 0))
        pygame.display.flip()

    StartupMenu = True
    FirstEvent = False
    E2A = False
    E2B = False
    E3A = False
    E3B = False
    E4A = False
    E4B = False
    E5A = False
    E5B = False
    E6A = False
    E6B = False
    E7A = False
    E7B = False
    E8A = False
    E8B = False
    Credits = False
    
    Doc = open("jsons/MenuInicial.json")
    data = json.load(Doc)
    while StartupMenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    FirstEvent = True
                    StartupMenu = False
        printtext(data)

    Doc = open("jsons/Escena1.json")
    data = json.load(Doc)
    while FirstEvent:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    E2A = True
                    FirstEvent = False
                if event.key == pygame.K_LEFT:
                    E2B = True
                    FirstEvent = False              
        printtext(data)

    Doc = open("jsons/Escena2A.json")
    data = json.load(Doc)
    while E2A:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    E3A = True
                    E2A = False
                if event.key == pygame.K_LEFT:
                    E3B = True
                    E2A = False
        printtext(data)

    Doc = open("jsons/Escena2B.json")
    data = json.load(Doc)
    while E2B:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    E4A = True
                    E2B = False
                if event.key == pygame.K_LEFT:
                    E4B = True
                    E2B = False
        printtext(data)

    Doc = open("jsons/Escena3A.json")
    data = json.load(Doc)
    while E3A: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    E5A = True
                    E3A = False
                if event.key == pygame.K_LEFT:
                    E5B = True
                    E3A = False
        printtext(data)

    Doc = open("jsons/Escena3B.json")
    data = json.load(Doc)
    while E3B:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    E6A = True
                    E3B = False
                if event.key == pygame.K_LEFT:
                    E6B = True
                    E3B = False
        printtext(data)

    Doc = open("jsons/Escena4A.json")
    data = json.load(Doc)
    while E4A:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    E7A = True
                    E4A = False
                if event.key == pygame.K_LEFT:
                    E7B = True
                    E4A = False
        printtext(data)

    Doc = open("jsons/Escena4B.json")
    data = json.load(Doc)
    while E4B:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    E8A = True
                    E4B = False
                if event.key == pygame.K_LEFT:
                    E8B = True
                    E4B = False
        printtext(data)

    Doc = open("jsons/Escena5A.json")
    data = json.load(Doc)
    while E5A:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Credits = True
                    E5A = False
                if event.key == pygame.K_LEFT:
                    Credits = True
                    E5A = False
        printtext(data)

    Doc = open("jsons/Escena5B.json")
    data = json.load(Doc)
    while E5B:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Credits = True
                    E5B = False
                if event.key == pygame.K_LEFT:
                    Credits = True
                    E5B = False
        printtext(data)

    Doc = open("jsons/Escena6A.json")
    data = json.load(Doc)
    while E6A:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Credits = True
                    E6A = False
                if event.key == pygame.K_LEFT:
                    Credits = True
                    E6A = False
        printtext(data)

    Doc = open("jsons/Escena6B.json")
    data = json.load(Doc)
    while E6B:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Credits = True
                    E6B = False
                if event.key == pygame.K_LEFT:
                    Credits = True
                    E6B = False
        printtext(data)

    Doc = open("jsons/Escena7A.json")
    data = json.load(Doc)
    while E7A:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Credits = True
                    E7A = False
                if event.key == pygame.K_LEFT:
                    Credits = True
                    E7A = False
        printtext(data)

    Doc = open("jsons/Escena7B.json")
    data = json.load(Doc)
    while E7B:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Credits = True
                    E7B = False
                if event.key == pygame.K_LEFT:
                    Credits = True
                    E7B = False
        printtext(data)

    Doc = open("jsons/Escena8A.json")
    data = json.load(Doc)
    while E8A:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Credits = True
                    E8A = False
                if event.key == pygame.K_LEFT:
                    Credits = True
                    E8A = False
        printtext(data)

    Doc = open("jsons/Escena8B.json")
    data = json.load(Doc)
    while E8B:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Credits = True
                    E8B = False
                if event.key == pygame.K_LEFT:
                    Credits = True
                    E8B = False
        printtext(data)

    Doc = open("jsons/Creditos.json")
    data = json.load(Doc)
    while Credits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Credits = False
                    Restart = False
                if event.key == pygame.K_r:
                    Credits = False
        printtext(data)
=======
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
>>>>>>> 6509a1ef90328b691c85518bfc6e2a97137ed1ed
