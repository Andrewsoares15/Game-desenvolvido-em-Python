import pygame
import random

class RedGuy(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/poco.png')
        #self.image = pygame.transform.scale(self.image, [95, 60])
        self.rect = pygame.Rect(60, 90, 60, 90)

        self.rect.x = 850
        self.rect.y = 610

class RedGuy2(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/poco.png')
        # self.image = pygame.transform.scale(self.image, [95, 60])
        self.rect = pygame.Rect(60, 90, 60, 90)

        self.rect.x = 550
        self.rect.y = 610

class RedGuy3(pygame.sprite.Sprite):

    def __init__(self, *groups):
            super().__init__(*groups)
            self.image = pygame.image.load('Restos/poco.png')
            # self.image = pygame.transform.scale(self.image, [95, 60])
            self.rect = pygame.Rect(60, 90, 60, 90)

            self.rect.x = 320
            self.rect.y = 610

class RedGuy4(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/poco.png')
        #self.image = pygame.transform.scale(self.image, [95, 60])
        self.rect = pygame.Rect(60, 90, 60, 90)

        self.rect.x = 325
        self.rect.y = 490
class RedGuy5(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/poco.png')
        #self.image = pygame.transform.scale(self.image, [95, 60])
        self.rect = pygame.Rect(60, 90, 60, 90)

        self.rect.x = 549
        self.rect.y = 490
class RedGuy6(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/poco.png')
        #self.image = pygame.transform.scale(self.image, [95, 60])
        self.rect = pygame.Rect(60, 90, 60, 90)

        self.rect.x = 849
        self.rect.y = 490
class RedGuy7(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/poco.png')
        #self.image = pygame.transform.scale(self.image, [95, 60])
        self.rect = pygame.Rect(60, 90, 60, 90)

        self.rect.x = 849
        self.rect.y = 375
class RedGuy8(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/poco.png')
        #self.image = pygame.transform.scale(self.image, [95, 60])
        self.rect = pygame.Rect(60, 90, 60, 90)

        self.rect.x = 550
        self.rect.y = 375

class RedGuy9(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/poco.png')
        #self.image = pygame.transform.scale(self.image, [95, 60])
        self.rect = pygame.Rect(60, 90, 60, 90)

        self.rect.x = 320
        self.rect.y = 375
class RedGuy10(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/poco.png')
        #self.image = pygame.transform.scale(self.image, [95, 60])
        self.rect = pygame.Rect(60, 90, 60, 90)

        self.rect.x = 320
        self.rect.y = 255
class RedGuy11(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/poco.png')
        #self.image = pygame.transform.scale(self.image, [95, 60])
        self.rect = pygame.Rect(60, 90, 60, 90)

        self.rect.x = 550
        self.rect.y = 255
class RedGuy12(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/poco.png')
        #self.image = pygame.transform.scale(self.image, [95, 60])
        self.rect = pygame.Rect(60, 90, 60, 90)

        self.rect.x = 849
        self.rect.y = 255