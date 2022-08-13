import pygame
import sys
from background import *
from player import *
from enemy_generator import *

def main():
  pygame.init()
  pygame.display.set_caption("Galaxy Lancer Plus")
  screen = pygame.display.set_mode((800, 600))
  clock = pygame.time.Clock()

  background = Background("images/galaxy.png", 10)
  player = Player("images/starship.png", "images/starship_l.png", "images/starship_r.png", "images/starship_burner.png", 10)
  enemy_generator = EnemyGenerator(1)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    key = pygame.key.get_pressed()

    background.draw(screen)
    player.key_pressed(key)
    player.draw(screen)
    enemy_generator.draw(screen)

    pygame.display.update()
    clock.tick(30)

if __name__ == '__main__':
  main()