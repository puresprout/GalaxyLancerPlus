import math
import pygame
from game_object import GameObject
from collider import *

class PlayerBullet(GameObject):
  def __init__(self, x, y, image_file, angle, speed):
    super().__init__(x, y)

    self.image = pygame.image.load(image_file)
    self.angle = angle
    self.speed = speed
    self.final_width = 0
    self.final_height = 0

    self.collider = Collider.CIRCLE
    self.tag = "PLAYER_BULLET"

  def get_width(self):
    return self.final_width

  def get_height(self):
    return self.final_height

  def draw(self, screen):
    self.x += self.speed * math.cos(math.radians(self.angle))
    self.y += self.speed * math.sin(math.radians(self.angle))

    # 마이너스 각도는 시간 반대방향 회전
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
