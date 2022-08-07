import pygame
import sys
from background import *

def main():
  pygame.init()
  pygame.display.set_caption("Galaxy Lancer Plus")
  screen = pygame.display.set_mode((800, 600))
  clock = pygame.time.Clock()

  background = Background("images/galaxy.png", 16)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    background.draw(screen)

    pygame.display.update()
    clock.tick(10)

if __name__ == '__main__':
  main()