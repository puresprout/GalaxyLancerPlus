import math
import pygame
from game_object import GameObject

class Enemy(GameObject):
  def __init__(self, x, y, speed, angle, parent):
    super().__init__(x, y, parent)
    self.image = pygame.image.load('images/enemy.png')
    self.speed = speed
    self.angle = angle
    
    # print("적 출현 x={}, y={}".format(x, y))

  def draw(self, screen):
    self.x += self.speed * math.cos(math.radians(self.angle))
    self.y += self.speed * math.sin(math.radians(self.angle))

    width = self.image.get_width()
    height = self.image.get_height()
    half_width = width / 2
    half_height = height / 2

    screen.blit(self.image, [self.x - half_width, self.y - half_height])

    if (self.y < -height or self.y > screen.get_height() + height or self.x < -width or self.x > screen.get_width() + width):
      self.parent.appendDeletingChild(self)
    