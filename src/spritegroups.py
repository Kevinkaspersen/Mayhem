import pygame
import random
import config
import items
import players


#Spritegroups

#A container for all sprite groups
all_sprites = pygame.sprite.Group() 

#Group for projectiles for each player
projectiles_group_1 = pygame.sprite.Group()
projectiles_group_2 = pygame.sprite.Group() 

#Player sprite groups
spaceship_1 = players.Spaceship_1()
spaceship_group_1 = pygame.sprite.Group(spaceship_1)

spaceship_2 = players.Spaceship_2()
spaceship_group_2 = pygame.sprite.Group(spaceship_2)

#Obsticle sprite group
obsticle_sprites = pygame.sprite.Group()
for i in range(2):
    obs_position = (random.randint(200, config.WIDTH - 200), random.randint(200, config.HEIGHT - 200))
    obsticle = items.obsticles(obs_position)
    obsticle_sprites.add(obsticle) # add the obsticle to surface

#Fuel can sprite group
fuel_can_sprites = pygame.sprite.Group()
fuel_position = (random.randint(200, config.WIDTH - 200), random.randint(200, config.HEIGHT - 200))
fuel_ob = items.Fuel_can(fuel_position)
fuel_can_sprites.add(fuel_ob) # add the obsticle to surface

#Adds all the groups into one group
all_sprites.add(spaceship_group_1, spaceship_group_2, obsticle_sprites, fuel_can_sprites)
