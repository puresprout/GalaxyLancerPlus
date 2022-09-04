import math
from game_object import *

class CollisionDetector:
  @staticmethod
  def detect(game_object):
    # object1 = CollisionDetector.get_game_object_list(game_object)
    # object2 = object1

    object1 = GameObject.detectable_list
    object2 = object1

    for item1 in object1:
      if item1.collider != None:
        for item2 in object2:
          if item2.collider != None:
            if item1 is item2:
              continue
            if item1.tag == item2.tag:
              continue

            if CollisionDetector.detect_collision(item1, item2):
              item1.onCollision(item2)

  @staticmethod
  def detect_collision(game_object1, game_object2):
    width1 = game_object1.get_width()
    height1 = game_object1.get_height()
    radius1 = (width1 + height1) / 4

    width2 = game_object2.get_width()
    height2 = game_object2.get_height()
    radius2 = (width2 + height2) / 4

    # if CollisionDetector.get_distance2(game_object1, game_object2) < (radius1 + radius2) * (radius1 + radius2):
    if CollisionDetector.get_distance(game_object1, game_object2) < radius1 + radius2:
      return True
    else:
      return False
  
  @staticmethod
  def get_distance(game_object1, game_object2):
    return math.sqrt(pow(game_object1.x - game_object2.x, 2) + pow(game_object1.y - game_object2.y, 2))

  @staticmethod
  def get_distance2(game_object1, game_object2):
    return pow(game_object1.x - game_object2.x, 2) + pow(game_object1.y - game_object2.y, 2)

  @staticmethod
  def get_game_object_list(game_object):
    if game_object.collider != None:
      list = [ game_object ]
    else:
      list = []
      
    for child in game_object.children:
      list.extend(CollisionDetector.get_game_object_list(child))
    return list