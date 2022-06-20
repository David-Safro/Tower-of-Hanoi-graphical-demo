import pygame


class Tower:
    def __init__(self, height, width, x, y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.color = "black"

    def draw(self, win):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, self.color, rect)


class Ring:
    def __init__(self, width, x, y, tower, color):
        self.width = width
        self.x = x
        self.y = y
        self.color = color
        self.tower = tower

    def draw(self, win):
        rect = pygame.Rect(self.x, self.y, self.width, 20)
        pygame.draw.rect(win, self.color, rect)

    def switch_towers(self, start, end, order, ):
        if order == 0:
            self.y -= Tower.height - (650-self.y)

