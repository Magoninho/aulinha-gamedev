import pygame

class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height):
		super().__init__()

		self.image = pygame.image.load("coin.png")
		self.rect = self.image.get_rect()

		self.image = pygame.transform.scale(self.image, (width, height))
		self.rect.topleft = x, y
