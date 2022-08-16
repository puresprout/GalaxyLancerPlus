import pygame
import sys
from background import *
from player import *
from enemy_generator import *
from enemy.enemy_bullet import *

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
  root.children.append(Background("images/galaxy.png", 10))
  root.children.append(Player("images/starship.png", "images/starship_l.png", "images/starship_r.png", "images/starship_burner.png", 10))
  root.children.append(EnemyGenerator(1))

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

    # print("enemy_bullet count {}".format(get_object_count(root)))

    pygame.display.update()
    clock.tick(30)

if __name__ == '__main__':
  main()
