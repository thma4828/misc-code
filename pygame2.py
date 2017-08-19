import pygame
import time
import random
import math

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
red2 = (255,45,45)
green = (0,255,0)
blue = (0,0,255)

#initialize pygame
pygame.init()
#set width/height
display_width = 800
display_height = 600
#initialize screen variable
screen = pygame.display.set_mode((display_width, display_height))
#set screen caption
pygame.display.set_caption("Game1")
pygame.display.update()
Clock = pygame.time.Clock()
gameOn = True
fps = 24


class BALL:
    def __init__(self):
        self.radius = 10
        self.color = white
        self.x = display_width/2
        self.y = display_height/2
        self.Xvel = -10
        self.Yvel = 0

    def respawn(self):
        if self.x >= display_width or self.x <= 0:
            self.x = display_width / 2
            self.y = display_height / 2
            self.Yvel = 0
            return True
        return False

    def draw(self):
        pygame.draw.circle(screen, black, [self.x, self.y], self.radius, self.radius)

    def MoveX(self):
        self.x += self.Xvel

    def MoveY(self):
        self.y += self.Yvel

    def setX(self, X):
        self.x = X

    def setY(self, Y):
        self.y = Y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getRadius(self):
        return self.radius

    def setVelocityX(self):
        self.Xvel = self.Xvel * -1

    def setVelocityY(self, vel):
        self.Yvel = vel

    def InvertYvel(self):
        self.Yvel = self.Yvel * -1

    def BounceP1(self):
        self.x += 10

    def BounceP2(self):
        self.x -= 10

    def BounceTopWall(self):
        self.y += 10

    def BounceBotWall(self):
        self.y -= 10


class PADDLE:
    def __init__(self, x, y, name, color):
        self.solid = True
        self.x = x
        self.y = y
        self.height = 50
        self.width = 10
        self.player = name
        self.color = color
        self.velocity = 0
        self.SCORE = 0

    def draw(self):
        pygame.draw.polygon(screen, self.color, [[self.x-(self.width/2), self.y -(self.height/2)],
                                           [self.x + (self.width/2), self.y -(self.height/2)],
                                           [self.x + (self.width/2), self.y + (self.height/2)],
                                           [self.x-(self.width/2), self.y + (self.height/2)]])

    def Update(self):
        self.y += self.velocity

    def getY(self):
        return self.y

    def getX(self):
        return self.x

    def setVelocity(self, vel):
        self.velocity = vel

    def invertVel(self):
        self.velocity = self.velocity * -1

    def move(self, m):
        if m is 'up':
            self.velocity = -10
        if m is 'down':
            self.velocity = 10

    def getVel(self):
        return self.velocity

    def updateScore(self):
        self.SCORE += 1

    def getScore(self):
        return self.SCORE

b1 = BALL()
play1 = PADDLE(5, display_height/2, 'Theo', blue)
play2 = PADDLE(display_width - 5, display_height/2, "Enemy", green)

def getCollision(bX, bY, bR, pX, pY, pW, pL):
    if abs(bY - pY) < pL/2 + bR:
        if abs(bX - pX) <= pW/2 + bR:
            return True

    return False

def getWallC(ballY, ballRad):
    if ballY + ballRad >= display_height - 10:
        return True
    if ballY - ballRad - 10 <= 0:
        return True

    return False

def getPaddleOB(pY, pL):
    if pY - pL/2 -10 <= 0:
        return True
    if pY + pL/2 >= display_height - 10:
        return True

    return False


def gameLoop(gameOn):
    volleyCount = 0
    while gameOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    play1.move('down')
                if event.key == pygame.K_w:
                    play1.move('up')
                if event.key == pygame.K_DOWN:
                    play2.move('down')
                if event.key == pygame.K_UP:
                    play2.move('up')

        Clock.tick(fps)
        screen.fill(white)
        pygame.draw.line(screen, red, [0, display_height-3], [display_width, display_height-3], 10)
        pygame.draw.line(screen, red, [0, 0], [display_width, 0], 10)
        b1.draw()
        b1.MoveX()
        b1.MoveY()

        play1.draw()
        play2.draw()
        play1.Update()
        play2.Update()

        ballX = b1.getX()
        ballY = b1.getY()
        ballRad = b1.getRadius()

        PadY = play1.getY()
        PadX = play1.getX()

        PadX2 = play2.getX()
        PadY2 = play2.getY()

        PadVel = play1.getVel()
        PadVel2 = play2.getVel()

        isColideP1 = getCollision(ballX, ballY, ballRad, PadX, PadY, 10, 30)
        isColideP2 = getCollision(ballX, ballY, ballRad, PadX2, PadY2, 10, 30)

        isWallC = getWallC(ballY, ballRad)

        isplay1OB = getPaddleOB(PadY, 30)
        isplay2OB = getPaddleOB(PadY2, 30)

        if isColideP1:
            b1.BounceP1()
            b1.setVelocityX()
            b1.setVelocityY(PadVel)
            volleyCount += 1

        if isColideP2:
            b1.BounceP2()
            b1.setVelocityX()
            b1.setVelocityY(PadVel2)
            volleyCount += 1

        if isWallC:
            if ballY < display_height/2:
                b1.BounceTopWall()
                b1.InvertYvel()
            else:
                b1.BounceBotWall()
                b1.InvertYvel()

        if isplay1OB:
            play1.invertVel()

        if isplay2OB:
            play2.invertVel()

        if b1.getX() < 9:
            play2.updateScore()
            volleyCount = 0

        if b1.getX() > display_width - 9:
            play1.updateScore()
            volleyCount = 0

        myfont = pygame.font.SysFont("monospace", 20)

        play1score = myfont.render(str(play1.getScore()), 1, (blue))
        play2score = myfont.render(str(play2.getScore()), 1, (green))
        vCount = myfont.render(str(volleyCount) + " VOLLIES", 1, black)

        screen.blit(play1score, (10, 15))
        screen.blit(play2score, (display_width-30, 15))
        screen.blit(vCount, (display_width/2 - 50, 15))

        b1.respawn()

        pygame.display.update()


def main():
    gameLoop(gameOn)
    print('loop executed succesfully')

main()
