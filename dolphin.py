import pygame
import random
from seagul import Bird
pygame.init()

class Bullet:
    def __init__(self, x, y, caliber):
        self.x = x
        self.y = y
        self.radius = caliber
        self.vx = 0
        self.vy = 0

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def move_with_dolphin(self, vx, vy):
        self.x += vx
        self.y += vy

    def respawn(self, cx, cy):
        if self.x > 800:
            self.x = cx
            self.y = cy
            self.vx = 0
class DolphinGun:
    def __init__(self, clipsize, x, y, cal):
        self.x = x
        self.y = y
        self.cal = cal
        self.clip = []
        self.num_clips = 10
        self.width = 15
        self.height = 10
        self.bullets_left = clipsize
        self.b = Bullet(x + 5, y + 3, cal)
        #print('bullets loaded')


class Stars:
    def __init__(self):
        self.num_stars = 200
        self.width_sky = 800
        self.height_sky= 300
        self.stars = []
        self.sx_vel = random.randrange(40,61)
        self.sy_vel = random.randrange(30, 71)
        for i in range(100):
            star_x = random.randrange(800)
            star_y = random.randrange(300)
            self.stars.append([star_x, star_y])

    def shooting_stars(self):
        c = 0
        for i in self.stars:
            c += 1
            if c % 10 is 0:
                x = i[0]
                y = i[1]



class Waves:
    def __init__(self):
        self.radius = 30
        self.vx = 10
        self.accel = 0
        self.x = -30
        self.y = 322

    def move(self):
        if self.accel == 0:
            self.x += self.vx
        else:
            self.x += (self.vx + self.accel)

        if self.x > 830:
            self.respawn()

    def respawn(self):
        self.x = -30
        self.vx = 10
        self.accel = 0
        self.y = 322

class Orca:
    def __init__(self):
        self.set_vals()
        self.gun = DolphinGun(30, self.bodyX, self.headrightY, 5)

    def set_vals(self):
        self.tailMidx = 20
        # following three have same x = tailMidx = 20
        self.tailMidy = 450
        self.tailTopY = 460
        self.tailBotY = 440
        # right x has the same y as tailMidY
        self.tailRightX = 37.3

        # body
        self.bodyH = 10
        self.bodyW = 26
        self.bodyX = 30
        self.bodyY = 446

        # head
        self.headMidX = 56
        # following three have same x = headMidX
        self.headMidY = 450
        self.headtopY = 460
        self.headbotY = 450
        self.headrightY = 450
        self.headrightx = 56 + 15
        self.vx = 0
        self.vy = 0

    def moveX(self, x_net):
        if self.bodyX > 800 | self.bodyX < 0:
            self.respawn()
        self.tailMidx += x_net
        self.tailRightX += x_net
        self.bodyX += x_net
        self.headMidX += x_net
        self.headrightx += x_net
        self.gun.x += x_net

    def moveY(self, y_net):
        if self.bodyY > 600 | self.bodyY < 0:
            self.respawn()
        self.tailMidy += y_net
        self.tailTopY += y_net
        self.tailBotY += y_net
        self.bodyY += y_net
        self.headMidY += y_net
        self.headtopY += y_net
        self.headbotY += y_net
        self.headrightY += y_net
        self.gun.y += y_net

    def vMove(self):
        self.moveX(self.vx)
        self.moveY(self.vy)


    def getVxVy(self):
        return self.vx, self.vy

    def respawn(self):
        self.set_vals()
        self.gun = DolphinGun(30, self.bodyX, self.headrightY, 5)

class Fish(Orca):
    def __init__(self):
        Orca.__init__(self)
        self.tailH = random.randrange(15, 22)
        self.x = 770
        self.y = random.randrange(310, 550)
        self.tailLength = random.randrange(15, 22)
        self.tailMidy = self.y
        self.tailMidx = self.x
        self.tailTopY = self.tailMidy + self.tailH
        self.tailBotY = self.tailMidy - self.tailH
        self.tailLeftX = self.x - self.tailLength
        self.tailLeftY = self.y
        self.radius = random.randrange(10, 23)
        self.circleX = self.tailLeftX - self.radius
        self.circleY = self.y
        self.topEyeX = self.circleX + .453*self.radius
        self.botEyeX = self.topEyeX
        self.topEyeY = self.circleY - self.radius/2
        self.botEyeY = self.circleY + self.radius/2
        self.vy = 0
        self.vx =(random.randrange(3, 9)) * -1
        self.gun = DolphinGun(10, 40, self.x, self.y)

    def moveY(self, y_net):
        #print('in move y func')
        if self.tailMidy > 610 | self.tailMidy < -10:
            self.respawn()
        self.tailMidy += y_net
        self.tailTopY += y_net
        self.tailBotY += y_net
        self.tailLeftY += y_net
        self.circleY += y_net
        self.topEyeY += y_net
        self.botEyeY += y_net

    def moveX(self, x_net):
        #print('in move x func')
        #print(self.tailMidx)
        if self.tailMidx < 0:
            self.respawn()
        self.tailMidx += x_net
        self.tailLeftX += x_net
        self.circleX += x_net
        self.topEyeX += x_net
        self.botEyeX += x_net
        self.gun.b.x += x_net
        #self.bodyX += x_net
        """todo: make respawn function actually respawn the dolphin"""
    def respawn(self):
        #print("spawning de fish")
        self.tailH = random.randrange(15, 22)
        self.x = 770
        self.y = random.randrange(310, 550)
        self.tailLength = random.randrange(15, 22)
        self.tailMidy = self.y
        self.tailMidx = self.x
        self.tailTopY = self.tailMidy + self.tailH
        self.tailBotY = self.tailMidy - self.tailH
        self.tailLeftX = self.x - self.tailLength
        self.tailLeftY = self.y
        self.radius = random.randrange(10, 23)
        self.circleX = self.tailLeftX - self.radius
        self.circleY = self.y
        self.topEyeX = self.circleX + .453 * self.radius
        self.botEyeX = self.topEyeX
        self.topEyeY = self.circleY - self.radius / 2
        self.botEyeY = self.circleY + self.radius / 2
        self.vy = 0
        self.vx = (random.randrange(3, 9)) * -1


class Game:
    def __init__(self):
        self.height = 600
        self.width = 800
        self.window = pygame.display.set_mode((800, 600))
        self.Clock = pygame.time.Clock()
        self.gameOn = False
        self.fps = 30
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)
        self.magenta = (139,0,139)
        self.dolphin = Orca()
        self.ocean = Waves()
        self.stars = Stars()
        self.fish = Fish()
        self.bird = Bird(800)
        self.frame_counter = 0

    def game_init(self):
        pygame.display.set_caption("dolympics")
        self.gameOn = True

    def collision(self):
        if abs(self.dolphin.gun.b.x - self.fish.topEyeX) <= self.fish.bodyW:
            if abs(self.dolphin.gun.b.y - self.fish.topEyeY) <= self.fish.radius:
                self.fish.respawn()
        if abs(self.dolphin.bodyX - self.bird.bomb_x) < ((self.dolphin.bodyW/2) + abs(self.dolphin.headMidX - self.dolphin.headrightx) + 5):
            if abs(self.dolphin.bodyY - self.bird.bomb_y) < 20:
                #print 'dolphin respawn'
                self.dolphin.respawn()

    def update(self):
        self.dolphin.gun.b.move_with_dolphin(self.dolphin.vx, self.dolphin.vy)
        self.frame_counter += 1
        self.bird.fly(self.dolphin.bodyX, self.dolphin.bodyY)
        self.collision()
        #print self.dolphin.gun.b.x
        self.Clock.tick(self.fps)
        self.dolphin.vMove()
        self.fish.vMove()
        #self.dolphin.gun.b.vx = self.dolphin.vx
        if self.dolphin.bodyY < 300:
            self.dolphin.vy = 0
        if self.dolphin.bodyY > 600:
            self.dolphin.vy = 0
        if self.dolphin.bodyX > 800:
            self.dolphin.vx = 0
        if self.dolphin.bodyX < 0:
            self.dolphin.vx = 0
        pygame.display.update()
        self.dolphin.gun.b.move()
        self.dolphin.gun.b.respawn(self.dolphin.gun.x, self.dolphin.gun.y)
        if self.dolphin.gun.b.vx == 0:
            self.dolphin.gun.b.y = self.dolphin.gun.y

    def draw(self):
        self.window.fill(self.blue)
        pygame.draw.rect(self.window, self.black, [0, 0, self.width, self.height/2])
        for starCoord in self.stars.stars:
            pygame.draw.circle(self.window, self.white, [starCoord[0], starCoord[1]], 1)
        pygame.draw.circle(self.window, self.yellow, [self.width/2, 50], 50)
        pygame.draw.polygon(self.window, self.green, [[self.dolphin.tailMidx, self.dolphin.tailBotY], [self.dolphin.tailMidx, self.dolphin.tailTopY],
                                                      [self.dolphin.tailRightX, self.dolphin.tailMidy]], 3)
        pygame.draw.rect(self.window, self.green, [self.dolphin.bodyX, self.dolphin.bodyY, self.dolphin.bodyW, self.dolphin.bodyH], 5)
        pygame.draw.polygon(self.window, self.green, [[self.dolphin.headMidX, self.dolphin.headtopY],
                                                      [self.dolphin.headMidX, self.dolphin.tailBotY],
                                                      [self.dolphin.headrightx, self.dolphin.headrightY]], 3)
        pygame.draw.polygon(self.window, self.green, [[self.fish.tailMidx, self.fish.tailTopY],[self.fish.tailMidx,
                            self.fish.tailBotY],[self.fish.tailLeftX, self.fish.tailLeftY]])
        pygame.draw.circle(self.window, self.black, [self.fish.circleX, self.fish.circleY], self.fish.radius)
        pygame.draw.circle(self.window, self.white, [int(self.fish.botEyeX), int(self.fish.botEyeY)], int(self.fish.radius/3))
        pygame.draw.circle(self.window, self.white, [int(self.fish.topEyeX), int(self.fish.topEyeY)], int(self.fish.radius/3))
        pygame.draw.polygon(self.window, self.magenta, [[self.dolphin.gun.x, self.dolphin.gun.y], [self.dolphin.gun.x, self.dolphin.gun.y - 20]], 10)
        pygame.draw.polygon(self.window, self.magenta,
                            [[self.dolphin.gun.x, self.dolphin.gun.y - 20], [self.dolphin.gun.x + 10, self.dolphin.gun.y - 20]],
                            10)
        pygame.draw.circle(self.window, self.black, [self.dolphin.gun.b.x, self.dolphin.gun.b.y], self.dolphin.gun.cal)
        pygame.draw.rect(self.window, self.yellow, [self.bird.x, self.bird.y, self.bird.square_side_len, self.bird.square_side_len])
        pygame.draw.rect(self.window, self.white, [self.bird.bomb_x, self.bird.bomb_y, 10, 10])
    #To DO: make def collision function to return if fish collides with bullet is true or false.
    #def collision(self, bullet_radius, fishHeadMid, fishHeadTop, fishHeadBot, fishRightMid):
    def gameLoop(self):
        self.game_init()
        while self.gameOn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOn = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.dolphin.vy = - 3
                    if event.key == pygame.K_a:
                        self.dolphin.vx = - 3
                    if event.key == pygame.K_d:
                        self.dolphin.vx = 3
                    if event.key == pygame.K_s:
                        self.dolphin.vy = 3
                    if event.key == pygame.K_SPACE:
                        self.dolphin.gun.b.vx = 30

            self.draw()
            self.update()


def main():
    game_001 = Game()
    game_001.gameLoop()

main()