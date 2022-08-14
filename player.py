import math
import pygame

from game_object import GameObject

class Player(GameObject):
  def __init__(self, starship_normal_image_file, starship_lef_image_file, starship_rigt_image_file, burner_image_file, speed):
    # 나중에 윈도우 크기 조정
    super().__init__(400, 300)

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

    self.MAX_FREQUENCY_SPACE_KEY = 15
    self.frequency_space_key = 0
    self.MAX_FREQUENCY_Z_KEY = 15
    self.frequency_z_key = 0

    self.deleting_children = []

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

  def postDraw(self):
    for child in self.deleting_children:
      self.children.remove(child)

    self.deleting_children = []

  def appendDeletingChild(self, child):
    self.deleting_children.append(child)



class PlayerBullet(GameObject):
  def __init__(self, x, y, image_file, angle, speed, player) -> None:
    super().__init__(x, y)

    self.image = pygame.image.load(image_file)
    self.angle = angle
    self.speed = speed
    self.player = player

  def draw(self, screen):
    self.x += self.speed * math.cos(math.radians(self.angle))
    self.y += self.speed * math.sin(math.radians(self.angle))

    # 마이너스 각도는 시간 반대방향 회전
    final_image = pygame.transform.rotozoom(self.image, -90 - self.angle, 1)
    final_width = final_image.get_width()
    final_height = final_image.get_height()
    final_half_width = final_width / 2
    fianl_half_height = final_height / 2

    screen.blit(final_image, [self.x - final_half_width, self.y - fianl_half_height])

    if (self.y < -final_height or self.y > screen.get_height() + final_height or self.x < -final_width or self.x > screen.get_width() + final_width):
      self.player.appendDeletingChild(self)
