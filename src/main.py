import pygame
import config
import spritegroups
import items
import random
import players
import cProfile

pygame.init()

#Function to draw text on screeen
font = pygame.font.SysFont('Calibri', 25)
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    config.screen.blit(img, (x, y))


def loop():
    """
    Method:
    -------
    this is where the game loop is 
    
    Hits:
    -----
    uses if tests and callable functions to add things to run in the loop
    """
    run = True
    while run:

        config.clock.tick(config.FPS)
        
                        #HITS
    #-----------------------------------------------------

        #Hits between projectiles and obsticles
        pygame.sprite.groupcollide(spritegroups.obsticle_sprites, spritegroups.projectiles_group_1, False, True)
        pygame.sprite.groupcollide(spritegroups.obsticle_sprites, spritegroups.projectiles_group_2, False, True)

        #Hits between ship and projectiles
        projectile_hit_1 = pygame.sprite.groupcollide(spritegroups.spaceship_group_1, spritegroups.projectiles_group_2, False, True)
        projectile_hit_2 = pygame.sprite.groupcollide(spritegroups.spaceship_group_2, spritegroups.projectiles_group_1, False, True)

        if projectile_hit_1:
            config.score_spaceship_2 += 10
            config.score_spaceship_1 -= 5
            spritegroups.spaceship_1.get_damage(100)

            if spritegroups.spaceship_1.current_health == 0:
                # spritegroups.spaceship_1.kill()
                print("Spaceship_2 WON!")
            Run = False

            # print("Score spaceship 2:", config.score_spaceship_2)
            # print("Score spaceship 1:", config.score_spaceship_1)
        
        if projectile_hit_2:
            config.score_spaceship_1 += 10
            config.score_spaceship_2 -= 5
            spritegroups.spaceship_2.get_damage(100)

            if spritegroups.spaceship_2.current_health == 0: 
                #  spritegroups.spaceship_2.kill()
                print("Spaceship_1 WON!")

            # print("Score spaceship 2:", config.score_spaceship_2)
            # print("Score spaceship 1:", config.score_spaceship_1)

        #Hits between ships and obsticles
        obs_hit_1 = pygame.sprite.spritecollide(spritegroups.spaceship_1, spritegroups.obsticle_sprites, True)
        obs_hit_2 = pygame.sprite.spritecollide(spritegroups.spaceship_2, spritegroups.obsticle_sprites, True) 

        for hit in obs_hit_1:
            new_obs = items.obsticles((random.randint(200, config.WIDTH - 200), random.randint(0, 20)))
            spritegroups.spaceship_1.get_damage(100)
            config.score_spaceship_1 -= 1
            spritegroups.all_sprites.add(new_obs)
            spritegroups.obsticle_sprites.add(new_obs)

        for hit in obs_hit_2:
            new_obs = items.obsticles((random.randint(200, config.WIDTH - 200), random.randint(0, 20)))
            spritegroups.spaceship_2.get_damage(100)
            config.score_spaceship_2 -= 1
            spritegroups.all_sprites.add(new_obs)
            spritegroups.obsticle_sprites.add(new_obs)
        
        #Hits between fuelcan and spaceships
        fuel_hit_1 = pygame.sprite.spritecollide(spritegroups.spaceship_1, spritegroups.fuel_can_sprites, True)
        fuel_hit_2 = pygame.sprite.spritecollide(spritegroups.spaceship_2, spritegroups.fuel_can_sprites, True)
        
        for hit in fuel_hit_1:
            new_fuel = items.Fuel_can((random.randint(200, config.WIDTH - 200), random.randint(200, config.HEIGHT - 200)))
            spritegroups.spaceship_1.get_fuel(100)
            spritegroups.all_sprites.add(new_fuel)
            spritegroups.fuel_can_sprites.add(new_fuel)
            # print(new_fuel.pos)

        for hit in fuel_hit_2:
            new_fuel = items.Fuel_can((random.randint(200, config.WIDTH - 200), random.randint(200, config.HEIGHT - 200)))
            spritegroups.spaceship_2.get_fuel(100)
            spritegroups.all_sprites.add(new_fuel)
            spritegroups.fuel_can_sprites.add(new_fuel)
        
        # Checks for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:

                #Spaceship 1
                #Shoot bullets
                if event.key == pygame.K_SPACE:
                    players.Spaceship_1.shoot1(spritegroups.spaceship_1)   

                # Spaceship 2
                #Shoot bullets
                if event.key == pygame.K_RCTRL:
                    players.Spaceship_2.shoot2(spritegroups.spaceship_2) 

        # Update calls and draw calls
        config.screen.blit(config.screen_image,[0, 0])

        spritegroups.all_sprites.update()

        #Draw
        spritegroups.all_sprites.draw(config.screen)

        #Draw text on screen
        config.score_spaceship_1_text = "SCORE: %d" % config.score_spaceship_1
        config.score_spaceship_2_text = "SCORE: %d" % config.score_spaceship_2

        draw_text(config.score_spaceship_1_text, font, config.YELLOW , 10 , 50)

        draw_text(config.score_spaceship_2_text, font, config.YELLOW , 750 , 50)

        pygame.display.flip()

    pygame.quit()
    
if __name__ == "__main__":
    loop()
    # cProfile.run('loop()')

        
       
