import pygame
import sys
from background import *
from player import *
from enemy.enemy_generator import *
from enemy.enemy_bullet import *
from collision_detector import *

def get_object_count(game_object):
  sum = 0

  for child in game_object.children:
    sum += get_object_count(child)
    if type(child) == EnemyBullet:
      sum += 1

  return sum

def main():
  pygame.init()
  pygame.display.set_caption("Galaxy Lancer Plus")
  screen = pygame.display.set_mode((800, 600))
  clock = pygame.time.Clock()

  root = GameObject(0, 0)
  GameObject.root = root
  root.children.append(Background())
  root.children.append(Player())
  root.children.append(EnemyGenerator())

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    key = pygame.key.get_pressed()

    root.key_pressed(key)
    root.preDraw()
    root.draw(screen)
    root.postDraw()

    CollisionDetector.detect(root)
    
    # print("enemy_bullet count {}".format(get_object_count(root)))

    pygame.display.update()
    clock.tick(30)

if __name__ == '__main__':
  main()
