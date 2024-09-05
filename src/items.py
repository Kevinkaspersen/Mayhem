import pygame
import random
from pygame import Vector2
import config

class obsticles(pygame.sprite.Sprite):
    """
    A class for the astoroids

    Attributes:
    -----------
        random width
        random height
        image for the rect
        speed for each direction
        using vector for position and velocity
    """
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        width = random.randint(40, 80)
        height = random.randint(40, 80)
        self.image = pygame.transform.smoothscale(pygame.image.load("images/Asteroid_Huge_Minerals.png"), (width, height))
        self.speedx = random.uniform(-1.5, 1.5)
        self.speedy = random.uniform(-1.5, 1.5)
        self.pos = Vector2(position)
        self.vel = Vector2(self.speedx, self.speedy)
        self.original_image = self.image
        self.rect = self.image.get_rect(center=position)

    def update(self):
        """
        Method:
        ------- 
           updates position based on velocity
           and imports borders
        """
        self.pos += self.vel
        self.rect.center = self.pos
        
        self.borders()

    def borders(self):
        """
        Method:
        ------- 
            defines the borders using an if for each side
        """
        if self.pos.x > config.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = config.WIDTH
        if self.pos.y <= 0:
            self.pos.y = config.HEIGHT
        if self.pos.y > config.HEIGHT:
            self.pos.y = 0

class Fuel_can(pygame.sprite.Sprite):
    """
    A class for the fuel can

    Attributes:
    -----------
        width
        height
        image for the rect
        speed for each direction
        using vector for position and velocity
    """
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self) 
        width = 30
        height = 40
        self.image = pygame.transform.smoothscale(pygame.image.load("images/jerrycan.png"), (width, height))
        self.original_image = self.image
        self.pos = Vector2(position)
        self.rect = self.image.get_rect(center=position)

   

class Projectile(pygame.sprite.Sprite):
    """
    A class for the projectile

    Attributes:
    -----------
        image on the surface for size
        color them yellow
        using vector for position 
    """
    def __init__(self, pos, direction):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(config.YELLOW)
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction
        self.pos = pygame.Vector2(self.rect.center)

    def update(self):
        """
        Method:
        -------
        uses position and defines the direction speed is 10
        center the rect and the position
        if test, for projectile hitting border
         """
        self.pos += self.direction * 10
        self.rect.center = self.pos
        if not pygame.display.get_surface().get_rect().contains(self.rect):
            self.kill()
               