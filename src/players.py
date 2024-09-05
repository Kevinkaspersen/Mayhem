import pygame
import random
from pygame import Vector2
import config
import items
import spritegroups


class Spaceships(pygame.sprite.Sprite):
    def __init__(self): 
        """
    A class to represent inheritable traits to the subclasses.

    Attributes:
    -----------
        random spawn position
        rect center
        speedy and speedx
        positional vector 
        velocity vector
        angle and angle speed
        acc = velocity

    Methods: 
    ---------
            gives inheritable traits, the sublclasses can use.
            updates callable functions for the subclasses. 
    """
        super().__init__()
        position= (random.randint(30, config.WIDTH - 30), random.randint(30, config.HEIGHT - 30))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=position)
        self.speedx = 0
        self.speedy = 0
        
        self.pos = Vector2(position)
        self.vel = Vector2(self.speedx, self.speedy)
        self.direction = Vector2(0, -1)
        self.angle = 0
        self.angle_speed = 0
        self.acc = 3

        #HEALTH
        """
        Attributes:
        -----------
        generates funnctions for health
        set variable for max healt
        variable for current health
        makes a ratio for healt 
        """
        self.current_health = 1000
        self.maximum_health = 1000
        self. health_bar_lenght = 200
        self.health_ratio = self.maximum_health / self.health_bar_lenght
        
        #fuel
        """
        Attributes:
        -----------
        generates funnctions for fuel
        set variable for max fuel
        variable for current fuel
        makes a ratio for fuel 
        """
        self.current_fuel = 1000
        self.maximum_fuel = 1000
        self. fuel_bar_lenght = 200
        self.fuel_ratio = self.maximum_fuel / self.fuel_bar_lenght
        
    #Method to give the player speed in the facing direction
    def accelerate(self):
        """
        Method:
        -------
        Method to give the player speed in the facing direction
        """
        self.vel += self.direction * self.acc

    #Checks for damage 
    def get_damage(self, amount):
        """
        Method:
        -------
        Checks for damage and assign an amount     
        """
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0: 
            self.current_health = 0
    
    def get_health(self, amount): 
        """
        Method:
        -------
        if test for checking health and adding healt
      
        """
        if self.current_health < self.maximum_health:
            self.current_health += amount
        if self.current_health >= self.maximum_health:
            self.current_health = self.maximum_health

    def lose_fuel(self, amount):
        """
        Method:
        -------
        if test, for checking fuel and lose fuel
      
        """
        if self.current_fuel > 0:
            self.current_fuel -= amount 
        if self.current_fuel <= 0: 
            self.current_fuel = 0

    def get_fuel(self, amount):
        """
        Method:
        -------
        if test, for checking fuel and add fuel
      
        """
        if self.current_fuel < self.maximum_fuel:
            self.current_fuel += amount
        if self.current_fuel >= self.maximum_fuel:
            self.current_fuel = self.maximum_fuel


#Player 1      
class Spaceship_1(Spaceships):
    """
    A class for the first spaceship

    Attributes:
    -----------
        width 
        height
        image for the rect
        

    method: 
    ---------
        innherited traits from the parent class.
    """
    def __init__(self):
        width = 40
        height = 45
        self.image = pygame.transform.smoothscale(pygame.image.load("../images/Green_Ship_Space.png"), (width, height))
        super().__init__()
        
    def update(self):
        """
        Method: 
        -------
            updates position based on velocity
            defines rotation based on ange and speed
            uses pre-defined updates in subclass
        """
        self.pos += self.vel
        self.rect.center = self.pos
    
        # Determines the speed of the rotation
        self.angle += self.angle_speed
        # Rotate the direction vector.
        self.direction.rotate_ip(self.angle_speed)
        # Function that rotates the image and updates the rect
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        # Makes sure that the image is in the center by taking the old one and setting the new one to be the same
        self.rect = self.image.get_rect(center=self.rect.center)

        #Screen borders
        items.obsticles.borders(self)
        #Steering
        self.move()
        #Health
        self.basic_health()
        #Fuel
        self.basic_fuel()  
        
    # Keybindings for steering the ship
    def move(self):
        """
        Method:
        -------
        define gravity effect on ship
        defines keybinds for movement
        """
        self.angle_speed = 0
        self.vel = (0,0.5)
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.angle_speed += -5
        if key[pygame.K_d]:
            self.angle_speed += 5
        if key[pygame.K_w]:
            self.lose_fuel(1)
            self.accelerate()
        if self.current_fuel == 0:
            self.acc = 0
        if self.current_fuel != 0:
            self.acc = 3

    
    def shoot1(self):
        """
        method:
        -------
        defines projectiles and allows the spaceship to shoot
        """
        projectile = items.Projectile(self.pos, self.direction.normalize())
        spritegroups.all_sprites.add(projectile)
        spritegroups.projectiles_group_1.add(projectile) 
        
    #Draws the fuel and health bars
    def basic_health(self):
       """
        Method:
        -------
        draws health
        """
       pygame.draw.rect(config.screen, (255,0,0), (10,10, self.current_health/self.health_ratio,10)) 
       pygame.draw.rect(config.screen, (255,255,255),(10,10,self.health_bar_lenght,10),1)         
    
    def basic_fuel(self):
       """
        Method:
        -------
        draws fuel
        """
       pygame.draw.rect(config.screen, (205,127,50), (10,30, self.current_fuel/self.fuel_ratio,10)) 
       pygame.draw.rect(config.screen, (255,255,255),(10,30,self.fuel_bar_lenght,10),1)
       
       
    
#Player 2 
class Spaceship_2(Spaceships):
    """
    A class for the second spaceship

    Attributes:
    -----------
        width 
        height
        image for the rect
        

    method: 
    ---------
        innherited traits from the parent class.
    """
    def __init__(self):
        width = 40
        height = 45
        self.image = pygame.transform.smoothscale(pygame.image.load("../images/Red_Ship_Space.png"), (width, height))
        super().__init__()

       
    def update(self):
        """
        Method:
        ------- 
            updates position based on velocity
            defines rotation based on ange and speed
            uses pre-defined updates in subclass
        """
        self.pos += self.vel
        self.rect.center = self.pos
        
        # Determines the speed of the rotation
        self.angle += self.angle_speed
        # Rotate the direction vector.
        self.direction.rotate_ip(self.angle_speed)
        # Function that rotates the image and updates the rect
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        # Makes sure that the image is in the center by taking the old one and setting the new one to be the same
        self.rect = self.image.get_rect(center=self.rect.center)

    

        #Screen borders
        items.obsticles.borders(self)
        #Steering
        self.move()
        #Health
        self.basic_health()
        #Fuel
        self.basic_fuel()  
      
    
    def move(self):
        """
        Method:
        -------
        define gravity effect on ship
        defines keybinds for movement
        """
        self.angle_speed = 0
        self.vel = (0,0.5)
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.angle_speed += 5
        if key[pygame.K_LEFT]:
            self.angle_speed += -5
        if key[pygame.K_UP]:
            self.accelerate()
            self.lose_fuel(1)
        if self.current_fuel == 0:
            self.acc = 0
        if self.current_fuel != 0:
            self.acc = 3
            
         
    def shoot2(self):
        """
        method:
        -------
        defines projectiles and allows the spaceship to shoot
        """
        projectile = items.Projectile(self.pos, self.direction.normalize())
        spritegroups.all_sprites.add(projectile)
        spritegroups.projectiles_group_2.add(projectile) 
    
          
    def basic_health(self):
       """
        Method:
        -------
        draws health
        """
       pygame.draw.rect(config.screen, (255,0,0), (750,10, self.current_health/self.health_ratio,10)) 
       pygame.draw.rect(config.screen, (255,255,255),(750,10,self.health_bar_lenght,10),1)
    
    def basic_fuel(self):
       """
        Method:
        -------
        draws fuel
        """
       pygame.draw.rect(config.screen, (205,127,50), (750,30, self.current_fuel/self.fuel_ratio,10)) 
       pygame.draw.rect(config.screen, (255,255,255),(750,30,self.fuel_bar_lenght,10),1)
    