import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroidGroup = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroidGroup, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()
	Player.containers = (updatable, drawable)
	


	player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
	
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill((0,0,0))
		updatable.update(dt)

		for a in asteroids:
			if a.collides_with(player):
				print("Game over!")
				sys.exit()
		
			for shot in shots:
				if a.collides_with(shot):
					shot.kill()
					a.split()

		for p in drawable:
			p.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()

