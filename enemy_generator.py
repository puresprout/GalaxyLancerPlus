import random
from enemy import *
from game_object import GameObject

class EnemyGenerator(GameObject):
  def __init__(self, count_per_second):
    super().__init__(0, 0)

    self.MAX_FREQUENCY = count_per_second * 30
    self.frequency = 0

  def draw(self, screen):
    # generator 클래스는 자신 자신을 그릴것이 없다.

    super().draw(screen)

    self.frequency = (self.frequency + 1) % self.MAX_FREQUENCY
    if (self.frequency == 0):
      x = random.randint(0, 800)
      y = 0
      self.children.append(Enemy(x, y))
