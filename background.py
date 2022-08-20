import pygame

from game_object import *

class Background(GameObject):
  def __init__(self):
    super().__init__(0, 0)

    self.image = pygame.image.load("images/galaxy.png")
    self.speed = 10

  def draw(self, screen):
    self.y = (self.y + self.speed) % screen.get_height()

    # 물체의 정중앙이 아닌 좌상단 좌표를 기준으로 그린다.
    screen.blit(self.image, [self.x, self.y - screen.get_height()])
    screen.blit(self.image, [self.x, self.y])
