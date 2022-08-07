import pygame

class Background:
  def __init__(self, image_file, speed):
    self.image_file = image_file
    self.image = pygame.image.load(image_file)
    self.speed = speed
    self.y = 0

  def draw(self, screen):
    screen.blit(self.image, [0, self.y - screen.get_height()])
    screen.blit(self.image, [0, self.y])
    self.y = (self.y + self.speed) % screen.get_height()
