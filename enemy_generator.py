import random
from enemy import *

class EnemyGenerator:
  def __init__(self, count_per_second):
    self.MAX_FREQUENCY = count_per_second * 30
    self.children = []
    self.frequency = 0

  def draw(self, screen):
    # generator 클래스는 자신 자신을 그릴것이 없다.
    for item in self.children:
      item.draw(screen)

    self.frequency = (self.frequency + 1) % self.MAX_FREQUENCY
    if (self.frequency == 0):
      x = random.randint(0, 800)
      y = 0
      print("적 출현 x={}, y={}".format(x, y))
      # self.children.append(Enemy(x, y))


