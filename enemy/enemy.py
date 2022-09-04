import math
import pygame
from game_object import GameObject
from .enemy_bullet import EnemyBullet
from collider import *

class Enemy(GameObject):
  def __init__(self, x, y, speed, angle, parent):
    super().__init__(x, y, parent)

    self.speed = speed
    self.angle = angle
    self.fired = False

    self.collider = Collider.CIRCLE
    self.tag = "ENEMY"

    # print("적 출현 x={}, y={}".format(x, y))

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

    if (self.fired == False) and (self.y > screen.get_height() / 2):
      self.fired = True
      GameObject.append_to_root(EnemyBullet(self.x, self.y, self.speed * 1.5, self.angle))
      self.angle = -90

    if (self.y < -self.final_height or self.y > screen.get_height() + self.final_height or self.x < -self.final_width or self.x > screen.get_width() + self.final_width):
      self.reserve_removing_myself()

    super().draw(screen)

  def onCollision(self, game_object):
    if game_object.tag == "PLAYER_BULLET":
      print("아군 미사일과 충돌 {}".format(game_object))
      self.reserve_removing_myself()