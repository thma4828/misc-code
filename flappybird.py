import pygame
import time
import random
from wall import wall

pygame.init()

class Bullet:
    def __init__(self, x, y, vx, vy, radius):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius

    def move(self):
        self.x += self.vx

    def respawn(self):
        if self.x + self.radius< 0:
            self.x = 770

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y


class Enemy:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.vy = -10
        self.vx = 0
        self.bullet = Bullet(x, y, -20, 0, 10)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.y - self.height > 600:
            self.respawn()
            self.vy = self.vy * -1

        if self.y < 0 or self.y > 600:
            self.respawn()
            self.vy = self.vy * -1

    def respawn(self):
        self.x = 770
        self.y = random.randrange(250, 450)

    def respawnBullet(self):
        self.bullet.x = self.x
        self.bullet.y = self.y

    def getBulletX(self):
        return self.bullet.x

    def getBulletY(self):
        return self.bullet.y


class Helicopter:
    def __init__(self, X, Y, height, width):
        self.x = X
        self.y = Y
        self.h = height
        self.w = width
        self.vy = 5
        self.vx = 0

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def Move(self):
        self.y += self.vy
        self.x += self.vx

    def Respawn(self):
        self.x = 50
        self.y = 300

    def Jump(self):
        self.vy -= 15
        self.y -= 15
        while self.vy < 0:
            self.vy += 1
            self.Move()
        self.vy = 5

class Game:
    def __init__(self, H, W):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)
        self.HEIGHT = H
        self.WIDTH = W
        self.Window = pygame.display.set_mode((H, W))
        self.Clock = pygame.time.Clock()
        self.gameOn = False
        self.fps = 24
        self.WALL = wall(0, 0, 100, 100)
        self.heli = Helicopter(50, 300, 25, 25)
        slugX = 770
        slugY = random.randrange(0, 575)
        self.slug = Enemy(slugX, slugY, 25, 25)

    def loadGame(self):
        pygame.display.set_caption("Flappy Bird")
        pygame.display.update()
        self.gameOn = True

    def isHeliSHOT(self):
        if abs(self.slug.bullet.x - self.heli.x) < self.slug.bullet.radius + self.heli.w/2:
            if abs(self.slug.bullet.y - self.heli.y) < self.slug.bullet.radius + self.heli.h/2:
                print('impact')
                self.heli.Respawn()

    def isCollision(self, wx, ww, wh, wy):
        if self.heli.y > wy - 25:
            if self.heli.y < wy + wh:
                if abs(self.heli.x - wx) <= 25:
                    print(True)
                    return True
        else:
            return False

    def EShoot(self):
        self.slug.bullet.move()

        if self.slug.bullet.x + self.slug.bullet.radius < 0:
            if abs(self.slug.y - self.heli.y) < 50:
                self.slug.respawnBullet()

    def update(self):
        self.Clock.tick(self.fps)
        self.slug.move()
        self.isHeliSHOT()
        pygame.display.update()
        self.EShoot()

    def draw(self, wallX, wallY, wallW, wallH):
        self.Window.fill(self.black)
        pygame.draw.rect(self.Window, self.red, [0, 0, 800, 30])
        pygame.draw.rect(self.Window, self.red, [0, 570, 800, 30])
        pygame.draw.rect(self.Window, self.red, [wallX, wallY, wallW, wallH])
        pygame.draw.rect(self.Window, self.green, [self.heli.x, self.heli.y, self.heli.w, self.heli.h])
        pygame.draw.rect(self.Window, self.yellow, [self.slug.x, self.slug.y, self.slug.width, self.slug.height])
        pygame.draw.circle(self.Window, self.yellow, [self.slug.bullet.x, self.slug.bullet.y], self.slug.bullet.radius)

    def gameLoop(self):
        self.loadGame()
        wallX = 800
        wallY = 0
        wallW = 100
        wallH = 300
        count = 0

        while self.gameOn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOn = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.heli.Jump()
                    # if event.key == pygame.K_w:
                    # if event.key == pygame.K_a:
                    # if event.key == pygame.K_d:
            if wallX + 100 < 0:
                wallX = 800
                wallH = random.randrange(200, 400)
                wallY = random.randrange(0, 300)
            self.heli.Move()
            if self.heli.y > self.HEIGHT:
                self.heli.Respawn()
            C = self.isCollision(wallX, wallW, wallH, wallY)
            if C:
                self.heli.Respawn()
                wallX = 800
                wallH = random.randrange(200, 400)
                wallY = random.randrange(0, 300)

            if self.slug.x == self.heli.x:
                self.slug.respawnBullet()
            else:
                count += 1

            print(count)

            if self.heli.y > 800:
                self.heli.Respawn()
            wallX = wallX - 10
            self.draw(wallX, wallY, wallW, wallH)
            self.update()

def main():
    game001 = Game(800, 600)
    game001.gameLoop()

main()
pygame.quit()
quit()