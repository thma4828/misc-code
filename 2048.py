import pygame
import time
import random
import math

pygame.init()
white = (255,255,255)
grey = (155,155,155)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
turqoise = (85, 255, 255)
yellow = (255, 255, 85)
width = 640
tileW = 640/5
height = 480
tileH = 480/3
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game1")
pygame.display.update()
Clock = pygame.time.Clock()
fps = 24
tiles = [[0 for x in range(5)],
         [0 for y in range(5)],
         [0 for z in range(5)],
         [0 for k in range(5)]]
INTarray= [[0 for x in range(5)],
           [0 for y in range(5)],
           [0 for z in range(5)],
           [0 for k in range(5)]]

def slidelist(M):
    sum = 0
    for i in M:
        sum += i
    M[0] = sum
    for i in range(1, len(M)):
        M[i] = 0

    return M

def sumList(M1):
    sum = 0
    for i in range(len(M1)):
        sum += M1[i]
    return sum

def getColumn(matrix, i):
    return [row[i] for row in matrix]

def gameLoop():
    gameOn = True
    INTarray[0][0] = 2
    row = random.randrange(4)
    collumn = random.randrange(1, 5)
    while gameOn:
        INTarray[row][collumn] = 2
        Clock.tick(fps)
        font = pygame.font.SysFont("monospace", 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    row = random.randrange(4)
                    collumn = random.randrange(1, 5)
                if event.key == pygame.K_w:
                    C1 = getColumn(INTarray, 0)
                    C2 = getColumn(INTarray, 1)
                    C3 = getColumn(INTarray, 2)
                    C4 = getColumn(INTarray, 3)

                    C1sum = sumList(C1)
                    C2sum = sumList(C2)
                    C3sum = sumList(C3)
                    C4sum = sumList(C4)

                    sumL = [C1sum, C2sum, C3sum, C4sum]

                    for i in range(4):
                        INTarray[0][i] = sumL[i]

                    row = random.randrange(4)
                    collumn = random.randrange(1, 5)
                if event.key == pygame.K_a:
                    M1 = INTarray[0]
                    M2 = INTarray[1]
                    M3 = INTarray[2]
                    M4 = INTarray[3]
                    M1new = slidelist(M1)
                    M2new = slidelist(M2)
                    M3new = slidelist(M3)
                    M4new = slidelist(M4)
                    INTarray[0] = M1new
                    INTarray[1] = M2new
                    INTarray[2] = M3new
                    INTarray[3] = M4new
                    row = random.randrange(4)
                    collumn = random.randrange(1, 5)
                if event.key == pygame.K_d:
                    row = random.randrange(4)
                    collumn = random.randrange(1, 5)

        x = tileW/3 + 20
        y = tileW/3 + 20
        color = yellow
        for i in range(len(tiles)):
            for j in range(len(tiles[i])):
                pygame.draw.circle(window, color, [x, y], tileW/3)
                integer = INTarray[i][j]
                num = font.render(str(integer), 1, blue)
                window.blit(num, [x-20, y-20])
                x = x + tileW
            y = y + tileH
            x = tileW/3 + 20
        pygame.display.update()


def main():
    gameLoop()


main()
pygame.quit()


