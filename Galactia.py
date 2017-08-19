import pygame
import time
import random
import math
from player import Player
from player import Bullet
from player import Enemy
from player import Landmine
from player import Catapult

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
red2 = (255, 45, 45)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (242, 136, 16)
lime_yellow = (225, 246, 33)
purple = (129, 22, 191)
blue_green = (30, 191, 115)
yellow = (255, 255, 0)
magenta = (139, 0, 139)
pygame.init()
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Galactia")
Clock = pygame.time.Clock()
fps = 60
pygame.init()
#pygame.image.load('D:/COMPUTER SCIENCE/PYGAME/watertexture.jpg')
#st = pygame.image.tostring(screen, 'RGBA', False)
#bg = pygame.image.fromstring(st, [800, 600], 'RGBA')


class Game:
    def __init__(self):
        self.w = display_width
        self.h = display_height
        self.gameOn = False
        self.ship = Player(black, display_width/2, display_height - 50, 50, 30, screen)
        self.slug = Enemy(random.randrange(100, 700), -10, screen)
        self.mine_deployed = False
        self.catapult = Catapult(random.randrange(30, 770), 10, screen)

    def isHit(self):
        if abs(self.ship.bullet.x - self.slug.x) <= self.slug.radius + self.ship.bullet.width/2:
            if abs(self.ship.bullet.y - self.slug.y) <= self.slug.radius + self.ship.bullet.height/2:
                self.slug.respawn()

        if abs(self.slug.x - self.ship.mine.x) <= self.slug.radius + self.ship.mine.base_radius:
            if abs(self.slug.y - self.ship.mine.y) <= self.slug.radius + self.ship.mine.base_radius:
                if self.mine_deployed:
                    self.ship.mine.explode()
                    self.slug.respawn()

    def call_funcs(self):
        self.ship.draw()
        self.ship.move()
        self.ship.bullet.move()
        self.slug.draw()
        self.slug.move()
        self.isHit()
        self.ship.gun.draw()
        self.catapult.draw()
        if self.mine_deployed:
            self.ship.mine.draw()

    def lazer_hit(self, x, y):
        if abs(self.slug.x - x) <= self.slug.radius:
            if abs(self.slug.y - y) <= self.slug.radius:
                self.slug.respawn()

    def gameLoop(self):
        self.gameOn = True
        while self.gameOn:
            Clock.tick(fps)
            screen.fill(white)
            #screen.blit(bg, [0, 0, 800, 600])
            self.call_funcs()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOn = False
                    self.quitGame()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.ship.x_vel = -5
                    if event.key == pygame.K_d:
                        self.ship.x_vel = 5
                    if event.key == pygame.K_SPACE:
                        self.ship.shoot()
                    if event.key == pygame.K_1:
                        self.ship.mine.color = (0, 0, 0)
                        self.ship.drop_landmine()
                        self.mine_deployed = True
                    if event.key == pygame.K_2:
                        self.mine_deployed = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    a = pygame.mouse.get_pos()
                    self.ship.gun.lazer(a[0], a[1])
                    self.lazer_hit(a[0], a[1])

            pygame.display.update()

    def quitGame(self):
        pygame.quit()


def main():
    game_01 = Game()
    game_01.gameLoop()

main()
quit()
