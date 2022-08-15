from .enemy import *

class EnemyType1(Enemy):
  def __init__(self, x, y, speed, angle, parent) -> None:
    super().__init__(x, y, speed, angle, parent)
    self.image = pygame.image.load('images/enemy_type1.png')

