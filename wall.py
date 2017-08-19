import pygame
import random
import time


class wall:
    def __init__(self, X, Y, H, W):
        self.HeightBreak = random.randrange(0, 600)
        self.x = X
        self.y = Y
        self.HEIGHT = H
        self.WIDTH = W

    def setX(self, X):
        self.x = X

