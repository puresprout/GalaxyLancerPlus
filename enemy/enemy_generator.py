import random
from enemy.enemy_type1 import *
from enemy.enemy_type2 import *
from game_object import GameObject

class EnemyGenerator(GameObject):
  def __init__(self):
    super().__init__(0, 0)

    count_per_second = 1

    self.MAX_FREQUENCY = count_per_second * 30
    self.frequency = 0

  def draw(self, screen):
    # generator 클래스는 자신 자신을 그릴것이 없다.

    self.frequency = (self.frequency + 1) % self.MAX_FREQUENCY
    if (self.frequency == 0):
      y = 0
      type = random.randint(1, 1)
      if type == 1:
        x = random.randint(0, 800)
        self.children.append(EnemyType1(x, y, 10, 90, self))
      elif type == 2:
        x = random.randint(0, 800)
        speed = random.randint(15, 25)
        angle = random.randint(70, 110)
        self.children.append(EnemyType2(x, y, speed, angle, self))

    super().draw(screen)

    # print("enemy count {}".format(len(self.children)))
