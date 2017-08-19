import pygame
import random

class Catapult:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.shape = 'square'
        self.width = 17
        self.barrel_len = 30
        self.screen = screen
        self.vx = 0
        self.vy = 0

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pygame.draw.rect(self.screen, (0,0,0), [self.x, self.y, self.width, self.width])
        pygame.draw.rect(self.screen, (0,0,0), [self.x + self.width/2, self.y, 2, self.barrel_len])

    def spawn_move(self):
        if self.x >= 400:
            self.vx = -1
            self.vy = 0
        elif self.x <= 400:
            self.vx = 1
            self.vy = 0

class MiniGun:
    def __init__(self, x, y, clip_size, rad, height, width, base_col, barrel_col, screen):
        self.x = x
        self.y = y
        self.clip_size = clip_size
        self.bullet_rad = rad
        self.height = height
        self.width = width
        self.barrel_1_x = self.x + width/3
        self.barrel_2_x = self.x + 2*(width / 3)
        self.barrel_3_x = self.x + width
        self.base_col = base_col
        self.barrel_col = barrel_col
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.base_col, [self.x, self.y, self.width, self.height])
        pygame.draw.rect(self.screen, self.barrel_col, [self.barrel_1_x, self.y, self.width/6, self.height-4])
        pygame.draw.rect(self.screen, self.barrel_col, [self.barrel_2_x, self.y, self.width / 6, self.height - 4])
        pygame.draw.rect(self.screen, self.barrel_col, [self.barrel_3_x, self.y, self.width / 6, self.height - 4])

    def lazer(self, x, y):
        pygame.draw.line(self.screen, (255, 0, 0), [self.x, self.y], [x,y], 5)

class Landmine:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.base_radius = 20
        self.red_bar_length = 5
        self.red_bar_height = 20
        self.color = (0, 0, 0)
        self.screen = screen
        self.animation_complete = False

    def draw(self):
        pygame.draw.circle(self.screen, self.color, [self.x, self.y], self.base_radius)
        pygame.draw.rect(self.screen, (255, 45, 45), [self.x - self.base_radius, self.y, self.red_bar_height, self.red_bar_length])

    def explode(self):
        self.color = (242, 136, 16)
        pygame.draw.polygon(self.screen, (255, 45, 45), [[self.x, self.y],
                                                         [self.x-self.base_radius, self.y],
                                                         [self.x + self.base_radius, self.y],
                                                         [self.x - self.base_radius, self.y - 10],
                                                         [self.x + self.base_radius, self.y + 10],
                                                         [self.x-self.base_radius, self.y - self.base_radius - 10],
                                                         [self.x + self.base_radius, self.y + self.base_radius + 10],
                                                         [self.x, self.y + self.base_radius + 10],
                                                         [self.x + self.base_radius / 2,
                                                          self.y + (self.base_radius * (2 / 3))],
                                                         [self.x + self.base_radius/2, self.y-(self.base_radius*(2/3))],
                                                         [self.x + self.base_radius + 10, self.y],
                                                         [self.x + self.base_radius/2, self.y + self.base_radius/2],
                                                         [self.x - self.base_radius / 3*2, self.y - self.base_radius / 2*3],
                                                         [self.x + self.base_radius / 2,
                                                          self.y - (self.base_radius * (2 / 3))],
                                                         [self.x - self.base_radius + 10, self.y],
                                                         [self.x - self.base_radius / 2, self.y + self.base_radius / 2],
                                                         [self.x + self.base_radius / 3 * 2,
                                                          self.y + self.base_radius / 2 * 3]])
        pygame.draw.polygon(self.screen, (242, 136, 18), [[self.x-5, self.y+5],
                                                         [self.x + self.base_radius, self.y-3],
                                                         [self.x - self.base_radius, self.y],
                                                         [self.x + self.base_radius, self.y - 10],
                                                         [self.x - self.base_radius, self.y + 10],
                                                         [self.x + self.base_radius, self.y - self.base_radius - 10],
                                                         [self.x - self.base_radius, self.y + self.base_radius + 10],
                                                         [self.x, self.y - self.base_radius + 10],
                                                         [self.x - self.base_radius / 2,
                                                          self.y - (self.base_radius * (2 / 3))],
                                                         [self.x - self.base_radius / 2,
                                                          self.y + (self.base_radius * (2 / 3))],
                                                         [self.x - self.base_radius + 10, self.y],
                                                         [self.x - self.base_radius / 2, self.y - self.base_radius / 2],
                                                         [self.x + self.base_radius / 3 * 2,
                                                          self.y + self.base_radius / 2 * 3],
                                                         [self.x - self.base_radius / 2,
                                                          self.y + (self.base_radius * (2 / 3))],
                                                         [self.x - self.base_radius - 10, self.y],
                                                         [self.x - self.base_radius / 2, self.y - self.base_radius / 2],
                                                         [self.x + self.base_radius / 3 * 2,
                                                          self.y + self.base_radius / 2 * 3]])
        self.x = -100


class Enemy:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.health = 100
        self.y_vel = 5
        self.x_vel = 0
        self.radius = 20
        self.screen = screen

    def take_damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            self.die()

    def die(self):
        del self

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

        if self.y >= 600:
            self.respawn()

    def respawn(self):
        self.x = random.randrange(100, 700)
        self.y = -10

    def draw(self):
        pygame.draw.circle(self.screen,(225, 246, 33),[self.x, self.y], self.radius)


class Bullet:
    def __init__(self, x, y, width, height, velocity, color):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.color = color
        self.width = width
        self.height = height

    def move(self):
        self.y += self.velocity

    def respawn(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0


class Player:
    def __init__(self, color, x, y, width, height, screen):
        self.color = color
        self.x = x
        self.y = y
        #top vertex
        self.top_vert_x = self.x
        self.top_vert_y = self.y - height/2
        #left vertex
        self.left_vert_x = self.x - width/2
        self.left_vert_y = self.y + height/2
        #right vertex
        self.right_vert_x = self.x + width / 2
        self.right_vert_y = self.y + height / 2
        self.screen = screen
        self.x_vel = 0
        self.bullet = Bullet(self.top_vert_x, self.top_vert_y, 7, 15, 0, (129, 22, 191))
        self.isShot = False
        self.mine = Landmine(self.top_vert_x, self.top_vert_y, screen)

        #def __init__(self, x, y, clip_size, rad, height, width, base_col, barrel_col, screen):
        self.gun = MiniGun(self.left_vert_x, self.top_vert_y, 30, 5, 43, 13,(30, 191, 115), (225, 246, 33), screen)

    def draw(self):
        pygame.draw.polygon(self.screen, self.color, [[self.top_vert_x,self.top_vert_y],[self.left_vert_x,
                                                      self.left_vert_y],[self.right_vert_x,  self.right_vert_y]])
        pygame.draw.rect(self.screen, self.bullet.color, [self.bullet.x, self.bullet.y, self.bullet.width, self.bullet.height])

    def drop_landmine(self):
        self.mine.x = self.top_vert_x
        self.mine.y = self.top_vert_y

    def move(self):
        if self.left_vert_x < 0 or self.right_vert_x > 800:
            self.x_vel = self.x_vel * -1
        self.top_vert_x += self.x_vel
        # left vertex
        self.left_vert_x += self.x_vel
        # right vertex
        self.right_vert_x += self.x_vel
        #mine
        self.gun.x += self.x_vel
        self.gun.barrel_1_x += self.x_vel
        self.gun.barrel_2_x += self.x_vel
        self.gun.barrel_3_x += self.x_vel

        if not self.isShot:
            self.bullet.x += self.x_vel

        if self.bullet.y <= 0:
            self.bullet.respawn(self.top_vert_x, self.top_vert_y)
            self.isShot = False

    def shoot(self):
        self.isShot = True
        self.bullet.velocity = -12






