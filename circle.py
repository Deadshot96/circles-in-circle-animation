import math
import pygame
from settings import *

class Circle(object):

    def __init__(self, x, y, level):
        self.cx = x
        self.cy = y
        self.x = x
        self.y = y
        self.level = level
        self.level = level
        self.radius = LEVELS[level][0]
        self.color = level
        self.nextAngle = 0
        self.currAngle = 0
        self.children = []


    def draw(self, win) -> None:
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

        for circle in self.children:
            circle.draw(win)


    def animate(self, frame: int) -> None:
        angle = pygame.math.lerp(self.currAngle, self.nextAngle, frame / TOTAL_FRAMES)
        radVector = pygame.math.Vector2(self.radius, 0)
        posVector = pygame.math.Vector2(self.cx, self.cy)
        
        radVector.rotate(angle)
        posVector = radVector + posVector
        
        self.x, self.y = int(posVector.x), int(posVector.y)
        
        for chlid in self.children:
            child.animate(frame)


    def getAngle(self) -> float:
        return self.currAngle


    def setAngle(self, angle: float) -> None:
        self.currAngle = self.nextAngle
        self.nextAngle = self.angle


    def addChild(self, level, levels):
        if level == levels:
            return
        
        cx, cy = self.x, self.y - self.radius
        angle = 360 // (len(self.children) + 1) + 90
        
        child = Circle(cx, cy, level)
        self.children.insert(0, child)
        
        for i, child in enumerate(self.children):
            nextAngle = i * angle + math.pi / 2
            child.setAngle(nextAngle)
            child.addChild(level + 1, levels)
