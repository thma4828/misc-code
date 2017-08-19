import pygame
import random

class Bird:
    def __init__(self, screen_width):
        self.x = screen_width + 30
        self.y = 0 + 30
        self.shape = "SQUARE"
        self.square_side_len = 30
        self.color = (255, 0, 0)
        self.vx = -15
        self.vy = (-10*self.x) / 200 + 17
        self.screen_width = 800
        self.screen_height = 600
        self.bomb_x = self.x
        self.bomb_y = self.y
        self.bomb_vx = -17
        self.bomb_vy = (2*self.x) / 200 + 17
        self.isBOMBING = False

    def fly(self, target_x, target_y):
        #print self.x, '-', target_x
        self.x += self.vx
        self.y -= self.vy

        self.vy = (-7*self.x / 200) + 17

        if not self.isBOMBING:
            self.bomb_x += self.vx
            self.bomb_y += self.vy

        if self.x < - 20:
            self.respawn()

        if self.y < 20 and self.y >= 0:
            if abs(self.x - target_x) < 600:
                self.isBOMBING = True
        elif self.y < 40 and self.y >= 20:
            if abs(self.x - target_x) < 420:
                self.isBOMBING = True
        elif self.y < 60 and self.y >= 40:
            if abs(self.x - target_x) < 330:
                self.isBOMBING = True
        elif self.y < 80 and self.y >= 60:
            if abs(self.x - target_x) < 250:
                self.isBOMBING = True
        elif self.y < 100 and self.y >= 80:
            if abs(self.x - target_x) < 175:
                self.isBOMBING = True

        if abs(self.x - target_x) < 175:
            self.isBOMBING = True

        if self.isBOMBING:
            self.bomb(target_x, target_y)

        if self.bomb_x < 0:
            self.isBOMBING = False

        if self.x < 0 and self.bomb_y > 610:
            self.isBOMBING = False

    def bomb(self, target_x, target_y):
        self.bomb_x += self.bomb_vx
        self.bomb_y += self.bomb_vy

        if self.bomb_x - target_x > abs(target_y - self.bomb_y):
            self.bomb_vx -= 1
        elif self.bomb_x - target_x < abs(target_y - self.bomb_y):
            self.bomb_vy += 1

        self.bomb_vy = (7*self.x / 200) + 17

        if self.bomb_x < 0:
            self.bomb_x = self.x
            self.bomb_y = self.y
            self.bomb_vx = -17
            self.bomb_vy = (2 * self.x) / 200 + 17

        if self.bomb_x < target_x + 30:
            if(self.bomb_y > 630):
                self.bomb_x = self.x
                self.bomb_y = self.y
                self.bomb_vx = -17
                self.bomb_vy = (2 * self.x) / 200 + 17
                self.isBOMBING = False

    def respawn(self):
        self.x = 830
        self.y = 30
        self.vx = -15
        self.vy = (-10 * self.x) / 200 + 17







