import pygame
import time
import random
import math
#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
red2 = (255,45,45)
green = (0,255,0)
blue = (0,0,255)
orange = (242, 136, 16)
lime_yellow = (225, 246, 33)
purple = (129, 22, 191)
blue_green = (30, 191, 115)
#initialize pygame module
pygame.init()
display_width = 600
display_height = 600
#set screen variable
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Zombie Defense")
#set clock variable
Clock = pygame.time.Clock()
fps = 24

class Turret:
    def __init__(self, x, y, outer_color, inner_color, in_radius, out_width, out_height):
        self.x = x
        self.y = y
        self.base_color = outer_color
        self.turret_color = inner_color
        self.turret_radius = in_radius
        self.width = out_width
        self.height = out_height
        self.damage = 10
        self.bullets = 100
        self.fire_rate = 1.5
        self.targetxy = [0, 0]
        self.target_set = False
        self.bullet_rad = 5
        self.bullet_vx = 0
        self.bullet_vy = 0
        self.bullet_x = x
        self.bullet_y = y
        self.map_c = []

    def render(self):
        pygame.draw.rect(screen, self.base_color, [self.x - self.turret_radius, self.y - self.turret_radius, self.width, self.height])
        pygame.draw.circle(screen, self.turret_color, [self.x, self.y], self.turret_radius)
        pygame.draw.circle(screen, blue_green, [self.bullet_x, self.bullet_y], self.bullet_rad)

    def set_target(self, xy):
        self.targetxy = xy
        self.target_set = True

    def shoot(self):
        print("Shoot")
        self.get_map_c()
        change_x = self.map_c[1] - self.targetxy[1]
        change_y = self.map_c[0] - self.targetxy[0]
        print('change in x: ', change_x, "  change in y: ", change_y)
        if change_x != 0:
            print('slope: ', float(change_y)/float(change_x))
            slope = float(change_y) / float(change_x)
            self.bullet_vy = -1*change_y
            self.bullet_vx = -1*change_x
            print('vx: ', self.bullet_vx, ' vy: ', self.bullet_vy)
        else:
            print('slope: INFINITE')
        self.move_bullet()

    def res_bullet(self):
        if self.bullet_x >= 600 or self.bullet_x <= 0:
            self.bullet_x = self.x
            self.bullet_y = self.y
            self.bullet_vx = 0
            self.bullet_vy = 0
        if self.bullet_y >= 600 or self.bullet_y <= 0:
            self.bullet_x = self.x
            self.bullet_y = self.y
            self.bullet_vx = 0
            self.bullet_vy = 0

    def move_bullet(self):
        self.bullet_x += self.bullet_vx
        self.bullet_y += self.bullet_vy

        self.res_bullet()

    def get_map_c(self):
        y_factor = float(self.y) / 600
        x_factor = float(self.x) / 600
        y_val = 0
        x_val = 0
        if y_factor < 1 and y_factor > 0.875:
            y_val = 7
        if y_factor <= 0.875 and y_factor > 0.75:
            y_val = 6
        if y_factor <= 0.75 and y_factor > 0.625:
            y_val = 5
        if y_factor <= 0.625 and y_factor > 0.5:
            y_val = 4
        if y_factor <= 0.5 and y_factor > 0.375:
            y_val = 3
        if y_factor <= 0.375 and y_factor > 0.25:
            y_val = 2
        if y_factor <= 0.25 and y_factor > 0.125:
            y_val = 1
        if y_factor <= 0.125 and y_factor > 0:
            y_val = 0


        if x_factor < 1 and x_factor > 0.875:
            x_val = 7
        if x_factor <= 0.875 and x_factor > 0.75:
            x_val = 6
        if x_factor <= 0.75 and x_factor > 0.625:
            x_val = 5
        if x_factor <= 0.625 and x_factor > 0.5:
            x_val = 4
        if x_factor <= 0.5 and x_factor > 0.375:
            x_val = 3
        if x_factor <= 0.375 and x_factor > 0.25:
            x_val = 2
        if x_factor <= 0.25 and x_factor > 0.125:
            x_val = 1
        if x_factor <= 0.125 and x_factor > 0:
            x_val = 0

        self.map_c = [y_val, x_val]


class Enemy:
    def __init__(self, hp, speed, radius, x, y, Map):
        self.x = x
        self.y = y
        self.HP = hp
        self.Speed = speed
        self.Radius = radius
        self.vx = 0
        self.vy = 0
        self.real_vel = 5
        self.direction = 'N'
        self.MAP = Map
        self.map_coord = []
        self.visited_points = []

    def path_find(self):
        self.set_map_coord()
        #case A determines if it is an edge
        #case B determines if it is a corner, There is overlap between the two as handled by isEdge and isCorner
        caseA = "N/A"
        caseB = "N/A"
        isCorner = False
        isEdge = False
        if self.map_coord[0] == 0:
            caseA = "TRow"
            isEdge = True
        if self.map_coord[0] == 7:
            caseA = "BRow"
            isEdge = True
        if self.map_coord[1] == 0:
            caseA = "LColumn"
            isEdge = True
        if self.map_coord[1] == 7:
            caseA = "RColumn"
            isEdge = True
        if self.map_coord == [7, 0]:
            caseB = "BLCorner"
            isEdge = True
            isCorner = True
        if self.map_coord == [0, 0]:
            caseB = "TLCorner"
            isEdge = True
            isCorner = True
        if self.map_coord == [7, 7]:
            caseB = "BRCorner"
            isEdge = True
            isCorner = True
        if self.map_coord == [0, 7]:
            caseB = "TRCorner"
            isEdge = True
            isCorner = True

        self.path_final(caseA, caseB, isEdge, isCorner)


    def path_final(self, a, b, isE, isC):
        if __name__ == '__main__':
            if b is "BLCorner":
                #print('case blcorner')
                tile_right = self.MAP[7][1]
                tile_up = self.MAP[6][0]
                if tile_up == 0 and tile_right == 0:
                    i = random.randrange(2)
                    if i == 0:
                        self.set_direction(1)
                    else:
                        self.set_direction(2)
                elif tile_up == 0:
                    self.set_direction(1)
                elif tile_right == 0:
                    self.set_direction(2)
            elif a is "BRow":
                #print('case bottom row')
                Y = self.map_coord[0]
                X = self.map_coord[1]
                t_right = self.MAP[Y][X + 1]
                t_up = self.MAP[Y - 1][X]
                if t_up == 0 and t_right == 0:
                    i = random.randrange(2)
                    if i == 0:
                        self.set_direction(1)
                    else:
                        self.set_direction(2)
                elif t_up == 0:
                    self.set_direction(1)
                elif t_right == 0:
                    self.set_direction(2)
            elif not isE and not isC:
                #print('middle case')
                yy = self.map_coord[0]
                xx = self.map_coord[1]
                up = self.MAP[yy - 1][xx]
                ri = self.MAP[yy][xx + 1]
                dow = self.MAP[yy + 1][xx]
                if up == 0 and ri == 0 and dow == 0:
                    #print('case a')
                    if [yy+1, xx] in self.visited_points:
                        i = random.randrange(2)
                        if i == 0:
                            self.set_direction(1)
                        else:
                            self.set_direction(2)
                    else:
                        self.set_direction(3)
                elif up == 0 and ri == 0:
                    #print('case b')
                    self.set_direction(2)
                elif up == 0 and dow == 1:
                    self.set_direction(1)
                elif ri == 0:
                    self.set_direction(2)
                elif dow == 0 and up == 1:
                    self.set_direction(3)
                elif up == 0 and dow == 0:
                    #not working...
                    print('not fully functional')
            elif a is "RColumn":
                self.x = 800
                self.__del__()

    def set_map_coord(self):
        y_factor = float(self.y)/600
        x_factor = float(self.x)/600
        y_val = 0
        x_val = 0
        if y_factor < 1 and y_factor > 0.875:
            y_val = 7
        if y_factor <= 0.875 and y_factor > 0.75:
            y_val = 6
        if y_factor <= 0.75 and y_factor > 0.625:
            y_val = 5
        if y_factor <= 0.625 and y_factor > 0.5:
            y_val = 4
        if y_factor <= 0.5 and y_factor > 0.375:
            y_val = 3
        if y_factor <= 0.375 and y_factor > 0.25:
            y_val = 2
        if y_factor <= 0.25 and y_factor > 0.125:
            y_val = 1
        if y_factor <= 0.125 and y_factor > 0:
            y_val = 0


        if x_factor < 1 and x_factor > 0.875:
            x_val = 7
        if x_factor <= 0.875 and x_factor > 0.75:
            x_val = 6
        if x_factor <= 0.75 and x_factor > 0.625:
            x_val = 5
        if x_factor <= 0.625 and x_factor > 0.5:
            x_val = 4
        if x_factor <= 0.5 and x_factor > 0.375:
            x_val = 3
        if x_factor <= 0.375 and x_factor > 0.25:
            x_val = 2
        if x_factor <= 0.25 and x_factor > 0.125:
            x_val = 1
        if x_factor <= 0.125 and x_factor > 0:
            x_val = 0
        #print(y_val, x_val)
        self.map_coord = [y_val, x_val]
        self.visited_points.append(self.map_coord)

    def set_direction(self, dir):
        if dir == 1:
            self.vy = -1 * self.real_vel
            self.direction = 'W'
            self.vx = 0
        elif dir == 2:
            self.vx = self.real_vel
            self.direction = 'D'
            self.vy = 0
        elif dir == 3:
            self.vy = self.real_vel
            self.direction = 'S'
            self.vx = 0
        elif dir == 4:
            self.vx = -1 * self.real_vel
            self.direction = 'A'
            self.vy = 0

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x >= 600:
            self.vx = 0
        if self.y >= 600:
            self.vy = 0

    def die(self):
        #print('death init')
        self.__del__()

    def take_damage(self, damage):
        self.HP -= damage
        if self.HP <= 0:
            self.die()

    def __del__(self):
        del self

#enemy with armor
class Grunt(Enemy):
    def __init__(self, hp, speed, outer_radius, inner_radius, outerShellHP, innerShellHP, x, y, MAP):
        Enemy.__init__(self, hp, speed, outer_radius, x, y, MAP)
        self.Shell_HP = outerShellHP
        self.Body_HP = innerShellHP
        self.Shell_Rad = outer_radius
        self.Body_Rad = inner_radius
        self.isArmor = True

    def take_damage(self, damage):
        if self.Shell_HP <= 0:
            self.isArmor = False
        if self.isArmor:
            self.Shell_HP -= damage
        else:
            self.Body_HP -= damage
        if self.Body_HP <= 0:
            self.die()

    def render(self):
        if self.isArmor:
            pygame.draw.circle(screen, orange, [self.x + self.Shell_Rad, self.y], self.Shell_Rad)
        else:
            pygame.draw.circle(screen, orange, [self.x + self.Shell_Rad, self.y], self.Body_Rad)


class Player:
    def __init__(self, dif):
        self.name = "Theo"
        self.gold = 1500/dif
        self.lives = 99

class Menu:
    def __init__(self, screen_width, screen_height):
        self.menu_height = screen_height/2
        self.menu_width = screen_width/2
        self.menu_color = blue
        self.menu_title = "Zombie Defense 1.1.0"
        self.menu_font = pygame.font.SysFont("verdana", 15)
        self.title_bar_height = self.menu_height/3
        self.diff_menu_height = self.menu_height*(2/3)
        self.easy = "Easy Difficulty"
        self.hard = "Hard Difficulty"
        self.medium = "Medium Difficulty"

    def render_menu(self, screen):
        pygame.draw.rect(screen, self.menu_color, [150, 150, self.menu_width, self.menu_height])
        Cmenu = self.menu_font.render("Choose a difficulty option: 1,2,3", 1, red)
        screen.blit(Cmenu, (150, 150))
        pygame.draw.rect(screen, white, [175, 175, self.menu_width - 50, self.menu_height - 600/3])
        Cez = self.menu_font.render("1. Easy", 1, red)
        screen.blit(Cez, (175, 175))
        pygame.draw.rect(screen, white, [175, 275, self.menu_width - 50, self.menu_height - 600 / 3])
        Cnormal = self.menu_font.render("2. Normal", 1, red)
        screen.blit(Cnormal, (175, 275))
        pygame.draw.rect(screen, white, [175, 375, self.menu_width - 50, self.menu_height - 600 / 3 - 40])
        Chard = self.menu_font.render("3. Hard", 1, red)
        screen.blit(Chard, (175, 375))

def renderMap(map):
    numRows = len(map)
    numC = len(map[0])
    #print('number of rows == ', numRows)
    r = 0
    tileWidth = display_width/numC
    tileHeight = display_height/numRows
    for row in map:
        for i in range(len(row)):
            currentTileX = i*tileWidth
            currentTileY = r*tileHeight
            #print("CURRENT TILE Y: ", currentTileY, '\n', 'CURRENT TILE X: ', currentTileX, '\n')
            color = white
            if row[i] == 0:
                color = black
            elif row[i] == 1:
                color = green
            pygame.draw.rect(screen, color, [currentTileX, currentTileY, tileWidth, tileHeight], 0)
            #print('tile height == ', tileHeight)
        r += 1

def main():
    gameOn = True
    map = [[1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 0, 0, 1, 0, 0, 0],
           [1, 0, 1, 0, 1, 0, 1, 1],
           [1, 0, 1, 0, 1, 0, 1, 1],
           [1, 0, 1, 0, 1, 0, 1, 1],
           [1, 0, 1, 0, 1, 0, 1, 1],
           [1, 0, 1, 0, 0, 0, 1, 1],
           [0, 0, 1, 1, 1, 1, 1, 1]]
    pygame.draw.rect(screen, white, [0, 0, display_width, display_height])
    m = Menu(600,600)
    dif = 0
    menuOn = True
    grunt = Grunt(100, 10, 30, 20, 50, 100, 55, 570, map)
    turret = Turret(320, 33, lime_yellow, purple, 15, 60, 60)
    while menuOn:
        renderMap(map)
        m.render_menu(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
                menuOn = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    dif = 1
                    menuOn = False
                if event.key == pygame.K_2:
                    dif = 2
                    menuOn = False
                if event.key == pygame.K_3:
                    dif = 3
                    menuOn = False
    while gameOn:
        #note: unused difficulty  modulator in variable dif
        Clock.tick(fps)
        renderMap(map)
        grunt.render()
        turret.render()
        grunt.path_find()
        enemy_xy = grunt.map_coord
        turret.set_target(enemy_xy)
        print(enemy_xy)
        turret.shoot()
        grunt.move()
        #print(grunt.map_coord)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
        pygame.display.update()

main()