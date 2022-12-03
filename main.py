import pygame
import math
from coin import *
from goomba import *
pygame.init()

screen = pygame.display.set_mode((600, 360))

bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg, (600, 360))

time = 0

coin_initial_x = 270
coin_initial_y = 140

goomba_initial_x = 190
goomba_initial_y = 280

coin = Coin(coin_initial_x, coin_initial_y, 40, 40)
goomba = Goomba(goomba_initial_x, goomba_initial_y, 40, 50)

all_sprites = pygame.sprite.Group()
all_sprites.add(coin)
all_sprites.add(goomba)

clock = pygame.time.Clock()
while True:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				exit()
			
	time += 1
	
	
	coin.rect.y = coin_initial_y + math.sin(time * 0.05) * 10
	goomba.rect.x = goomba_initial_x + math.sin(time * 0.0069) * 150
	
	screen.fill((0, 150, 255))

	screen.blit(bg, (0, 0, 600, 360))

	all_sprites.draw(screen)

	pygame.display.update()
