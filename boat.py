import pygame
import random

from dolphin import Game
from dolphin import Fish

class Boat(Fish):
    def __init__(self):
        Fish.__init__(self)
        self.bodyX = 800
        self.bodyY = 300
