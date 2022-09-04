class GameObject:
  root = None
  detectable_list = []

  def __init__(self, x, y, parent=None):
    self.x = x
    self.y = y
    self.collider = None
    self.tag = None

    self.children = []
    self.deleting_children = []
    self.parent = parent

  def set_parent(self, parent):
    self.parent = parent

  def get_width(self):
    return None

  def get_height(self):
    return None

  def append(self, game_object):
    self.children.append(game_object)
    
    if game_object.collider != None:
      self.detectable_list.append(game_object)

  def remove(self, game_object):
    try:
      self.children.remove(game_object)
    except:
      pass

    if game_object.collider != None:
      try:
        self.detectable_list.remove(game_object)
      except:
        pass

  def key_pressed(self, screen):
    for child in self.children:
      child.key_pressed(screen)

  def preDraw(self):
    for child in self.children:
      child.preDraw()

  def draw(self, screen):
    for child in self.children:
      child.draw(screen)

  def postDraw(self):
    self.remove_reserved_children()

    for child in self.children:
      child.postDraw()

  def reserve_removing_myself(self):
    self.parent.reserve_removing_child(self)

  # 지울 자식을 추가해 놓으면 현재 프레임 호출이 끝난후 해당 자식이 삭제된다.
  def reserve_removing_child(self, child):
    self.deleting_children.append(child)

  def remove_reserved_children(self):
    for child in self.deleting_children:
        self.remove(child)

    self.deleting_children.clear()

  @staticmethod
  def append_to_root(game_object):
    GameObject.root.append(game_object)
    game_object.set_parent(GameObject.root)