import random
from collision_detector import CollisionDetector
from enemy.enemy_type1 import *
from enemy.enemy_type2 import *
from game_object import GameObject

class EnemyGenerator(GameObject):
  def __init__(self):
    super().__init__(0, 0)

    ENEMY_COUNT_PER_SECOND = 1

    self.MAX_FREQUENCY = 30 / ENEMY_COUNT_PER_SECOND
    self.frequency = 0

  def draw(self, screen):
    # generator 클래스는 자신 자신을 그릴것이 없다.

    self.frequency = (self.frequency + 1) % self.MAX_FREQUENCY
    if (self.frequency == 0):
      y = 0
      type = random.randint(1, 1)
      if type == 1:
        x = random.randint(0, 800)
        self.append(EnemyType1(x, y, 10, 90, self))
      elif type == 2:
        x = random.randint(0, 800)
        speed = random.randint(15, 25)
        angle = random.randint(70, 110)
        self.append(EnemyType2(x, y, speed, angle, self))

    super().draw(screen)

    # for child1 in self.children:
    #   for child2 in GameObject.root.children:
    #     if child2.tag == "PLAYER_BULLET" and CollisionDetector.detect_collision(child1, child2):
    #       child1.onCollision(child2)

    # print("enemy count {}".format(len(self.children)))
