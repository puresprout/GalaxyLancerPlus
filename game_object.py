class GameObject:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.children = []

  def key_pressed(self, screen):
    for child in self.children:
      child.key_pressed(screen)

  def draw(self, screen):
    for child in self.children:
      child.draw(screen)
