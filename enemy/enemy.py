import math
import pygame
from game_object import GameObject

class Enemy(GameObject):
  def __init__(self, x, y, speed, angle, parent):
    super().__init__(x, y, parent)
    self.speed = speed
    self.angle = angle
    
    # print("적 출현 x={}, y={}".format(x, y))

  def draw(self, screen):
    self.x += self.speed * math.cos(math.radians(self.angle))
    self.y += self.speed * math.sin(math.radians(self.angle))

    final_image = pygame.transform.rotozoom(self.image, -90 - self.angle, 1)
    final_width = final_image.get_width()
    final_height = final_image.get_height()
    final_half_width = final_width / 2
    fianl_half_height = final_height / 2

    screen.blit(final_image, [self.x - final_half_width, self.y - fianl_half_height])

    if (self.y < -final_height or self.y > screen.get_height() + final_height or self.x < -final_width or self.x > screen.get_width() + final_width):
      self.parent.appendDeletingChild(self)
    