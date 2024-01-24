import pygame
import numpy as np
import time
import math
#creamos la pantalla de nuestro juego 
pygame.init()
#definimos el tamaño de la pantalla
size = width, height = 700, 700
#definimos el numero de celdas 
numberXCells = 60
numberYCells = 60
#calculamos el tamaño de nuestra tabla a lo ancho y largo
sizeCellWidth = (width - 1) / numberXCells
sizeCellHeight = (height - 1) / numberYCells
#color de fondo
background = 25, 25, 25
screen = pygame.display.set_mode((height, width), pygame.RESIZABLE)
screen.fill(background) 
#guradamos los resultados en gameState
gameState = np.zeros((numberXCells, numberYCells))
print(gameState)
pauseExec = False
while 1:
    #actualizamos los datos en un nuevo registro
    newGameState = np.copy(gameState)
    eventt = pygame.event.get()        
    #con clic izq creamos y con derecho borramos 
    for event in eventt:
        if event.type == pygame.KEYDOWN:
            pauseExec = not pauseExec
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            positionX, positionY = pygame.mouse.get_pos()
            if positionX > 0 and positionX < (width - 1) and positionY > 0 and positionY <(height - 1):
                newGameState[math.floor(positionX / sizeCellWidth),
                             math.floor(positionY / sizeCellHeight)] = mouseClick[0] and not  mouseClick[2]
    screen.fill(background)

    for y in range(0, numberYCells):
        for x in range(0, numberXCells):    
            if not pauseExec:
                 ##calculamos el numero de vecinos cerca usando continuidad con %
                numberNeigh = gameState[(x - 1) % numberXCells, (y - 1) % numberYCells] + \
                            gameState[(x) % numberXCells, (y - 1) % numberYCells] + \
                            gameState[(x + 1) % numberXCells, (y - 1) % numberYCells] + \
                            gameState[(x - 1) % numberXCells, (y) % numberYCells] + \
                            gameState[(x + 1) % numberXCells, (y) % numberYCells] + \
                            gameState[(x - 1)  % numberXCells, (y + 1) % numberYCells] + \
                            gameState[(x) % numberXCells, (y + 1) % numberYCells] + \
                            gameState[(x + 1) % numberXCells, (y + 1) % numberYCells]
                ##primer criterio: una muerta con 3 vecinos vivos entonces revives
                if gameState[x, y] == 0 and numberNeigh ==3:
                    newGameState[x, y] = 1
                ##segundo criterio: una viva con 2 muertos o mas de 3  vecinos vivos entonces mueres
                elif gameState[x, y] == 1 and (numberNeigh < 2 or numberNeigh > 3):
                    newGameState[x, y] = 0

            ##definimos los puntos de nuestra celda en forma de cuadro
            poly = [((x) * sizeCellWidth, (y) * sizeCellHeight),
                    ((x + 1) * sizeCellWidth, (y) * sizeCellHeight),
                    ((x + 1) * sizeCellWidth, (y + 1) * sizeCellHeight),
                    ((x) * sizeCellWidth,  (y + 1) * sizeCellHeight)]
           ##dibujamos las lineas del juego y los pixeles
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1) 
            else:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 0) 
    time.sleep(1 / 30)
    gameState = np.copy(newGameState)
    pygame.display.flip()
