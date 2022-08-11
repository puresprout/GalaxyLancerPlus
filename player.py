import pygame

class Player:
  def __init__(self, starship_normal_image_file, starship_lef_image_file, starship_rigt_image_file, burner_image_file, speed):
    self.starship_images = [ pygame.image.load(starship_normal_image_file),
          pygame.image.load(starship_lef_image_file),
          pygame.image.load(starship_rigt_image_file) ]
    self.burner_image = pygame.image.load(burner_image_file)
    self.starship_half_width = self.starship_images[0].get_width() / 2
    self.starship_half_height = self.starship_images[0].get_height() / 2
    self.burner_half_width = self.burner_image.get_width() / 2
    self.burner_half_height = self.burner_image.get_height() / 2
    self.speed = speed
    self.slode = 0
    self.MAX_BURNER_POSITION = 3
    self.burner_position = 0

    # 나중에 윈도우 크기 조정
    self.x = 400
    self.y = 300

  def key_pressed(self, key):
    if key[pygame.K_UP] == 1:
      self.slode = 0
      self.y = self.y - 20
      if self.y < 0:
        self.y = 0
    if key[pygame.K_DOWN] == 1:
      self.slode = 0
      self.y = self.y + 20
      if self.y > 600:
        self.y = 600
    if key[pygame.K_LEFT] == 1:
      self.slode = 1
      self.x = self.x - 20
      if self.x < 0:
        self.x = 0
    if key[pygame.K_RIGHT] == 1:
      self.slode = 2
      self.x = self.x + 20
      if self.x > 800:
        self.x = 800
    if key[pygame.K_LEFT] == 0 and key[pygame.K_RIGHT] == 0:
      self.slode = 0

  def draw(self, screen):
    self.burner_position = (self.burner_position + 1) % self.MAX_BURNER_POSITION
    final_burner_position = (self.MAX_BURNER_POSITION - 1) * 2 + self.burner_position * 2

    # 그릴때 x, y 위치는 이미지의 정중앙으로 한다.
    screen.blit(self.burner_image, [self.x - self.burner_half_width, self.y + self.starship_half_height - final_burner_position])
    screen.blit(self.starship_images[self.slode], [self.x - self.starship_half_width, self.y - self.starship_half_height])
