import pygame
import math
from collider import Collider
from game_object import GameObject

class EnemyBullet(GameObject):
  def __init__(self, x, y, speed, angle):
    super().__init__(x, y)
    
    self.speed = speed
    self.angle = angle
    self.image = pygame.image.load("images/enemy_bullet.png")

    # self.collider = Collider.CIRCLE
    self.tag = "ENEMY_BULLET"

  def get_width(self):
    return self.final_width

  def get_height(self):
    return self.final_height

  def draw(self, screen):
    self.x += self.speed * math.cos(math.radians(self.angle))
    self.y += self.speed * math.sin(math.radians(self.angle))
    
    final_image = pygame.transform.rotozoom(self.image, -90 - self.angle, 1)
    self.final_width = final_image.get_width()
    self.final_height = final_image.get_height()
    final_half_width = self.final_width / 2
    fianl_half_height = self.final_height / 2

    screen.blit(final_image, [self.x - final_half_width, self.y - fianl_half_height])

    if (self.y < -self.final_height or self.y > screen.get_height() + self.final_height or self.x < -self.final_width or self.x > screen.get_width() + self.final_width):
      self.reserve_removing_myself()

  def onCollision(self, game_object):
    pass
