import math
import pygame
from game_object import GameObject
from player_bullet import PlayerBullet

class Player(GameObject):
  def __init__(self):
    # 나중에 윈도우 크기 조정
    super().__init__(400, 300)

    self.starship_images = [ pygame.image.load("images/starship.png"),
          pygame.image.load("images/starship_l.png"),
          pygame.image.load("images/starship_r.png") ]
    self.burner_image = pygame.image.load("images/starship_burner.png")
    self.starship_half_width = self.starship_images[0].get_width() / 2
    self.starship_half_height = self.starship_images[0].get_height() / 2
    self.burner_half_width = self.burner_image.get_width() / 2
    self.burner_half_height = self.burner_image.get_height() / 2
    self.speed = 10
    self.slode = 0
    self.MAX_BURNER_POSITION = 3
    self.burner_position = 0

    self.MAX_FREQUENCY_SPACE_KEY = 15
    self.frequency_space_key = 0
    self.MAX_FREQUENCY_Z_KEY = 15
    self.frequency_z_key = 0

  def key_pressed(self, key):
    if key[pygame.K_UP] == 1:
      self.slode = 0
      self.y -= self.speed
      if self.y < 0:
        self.y = 0
    if key[pygame.K_DOWN] == 1:
      self.slode = 0
      self.y += self.speed
      if self.y > 600:
        self.y = 600
    if key[pygame.K_LEFT] == 1:
      self.slode = 1
      self.x -= self.speed
      if self.x < 0:
        self.x = 0
    if key[pygame.K_RIGHT] == 1:
      self.slode = 2
      self.x += self.speed
      if self.x > 800:
        self.x = 800
    if key[pygame.K_LEFT] == 0 and key[pygame.K_RIGHT] == 0:
      self.slode = 0

    self.frequency_space_key = (self.frequency_space_key + 1) * key[pygame.K_SPACE]
    if (self.frequency_space_key % self.MAX_FREQUENCY_SPACE_KEY == 1):
      self.children.append(PlayerBullet(self.x, self.y - self.starship_half_height, "images/bullet.png", 270, 30, self))
    
    self.frequency_z_key = (self.frequency_z_key + 1) * key[pygame.K_z]
    if (self.frequency_z_key % self.MAX_FREQUENCY_Z_KEY == 1):
      for angle in range(0, 360, 10):
        self.children.append(PlayerBullet(self.x, self.y - self.starship_half_height, "images/bullet.png", angle, 30, self))

  def draw(self, screen):
    super().draw(screen)

    self.burner_position = (self.burner_position + 1) % self.MAX_BURNER_POSITION
    final_burner_position = (self.MAX_BURNER_POSITION - 1) * 2 + self.burner_position * 2

    # 그릴때 x, y 위치는 starship 이미지의 정중앙으로 한다. (burner 이미지는 고려하지 않는다.)
    screen.blit(self.burner_image, [self.x - self.burner_half_width, self.y + self.starship_half_height - final_burner_position])
    screen.blit(self.starship_images[self.slode], [self.x - self.starship_half_width, self.y - self.starship_half_height])
