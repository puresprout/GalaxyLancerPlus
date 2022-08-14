from game_object import GameObject

class Enemy(GameObject):
  def __init__(self, x, y):
    super().__init__(x, y)
    
    print("적 출현 x={}, y={}".format(x, y))
