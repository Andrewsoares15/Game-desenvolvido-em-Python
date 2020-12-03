import pygame

class Guy(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/personagemcerto.png')
        self.image = pygame.transform.scale(self.image, [45, 75])
        self.rect = pygame.Rect(40, 70, 40, 70)
        self.rect.x = 1020
        self.rect.y = 570

    def update(self, *args):

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and self.rect.x >= 2:
            self.rect.x += 5
            #self.image = pygame.image.load('data/Imagens/lado1.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_LEFT]: #and self.rect.x <= 880:
            self.rect.x -= 5
            #self.image = pygame.image.load('data/Imagens/lado2.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 5
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 5

        if self.rect.right < 40:
            self.rect.right = 40

        if self.rect.x >= 1020:
            self.rect.x = 1020
        if self.rect.y >= 610:
            self.rect.y = 610

class Guy2(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/personagemcerto.png')
        self.image = pygame.transform.scale(self.image, [45, 75])
        self.rect = pygame.Rect(40, 70, 40, 70)
        self.rect.x = 850
        self.rect.y = 570

    def update(self, *args):

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and self.rect.x >= 2:
            self.rect.x += 5
            #self.image = pygame.image.load('data/Imagens/lado1.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_LEFT]: #and self.rect.x <= 880:
            self.rect.x -= 5
            #self.image = pygame.image.load('data/Imagens/lado2.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 5
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 5

        if self.rect.x >= 1020:
            self.rect.x = 1020
        if self.rect.y >= 610:
            self.rect.y = 610
class Guy3(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/personagemcerto.png')
        self.image = pygame.transform.scale(self.image, [45, 75])
        self.rect = pygame.Rect(40, 70, 40, 70)
        self.rect.x = 550
        self.rect.y = 570

    def update(self, *args):

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and self.rect.x >= 2:
            self.rect.x += 5
            #self.image = pygame.image.load('data/Imagens/lado1.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_LEFT]: #and self.rect.x <= 880:
            self.rect.x -= 5
            #self.image = pygame.image.load('data/Imagens/lado2.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 5
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 5

        if self.rect.x >= 1020:
            self.rect.x = 1020
        if self.rect.y >= 610:
            self.rect.y = 610

class Guy4(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/personagemcerto.png')
        self.image = pygame.transform.scale(self.image, [45, 75])
        self.rect = pygame.Rect(40, 70, 40, 70)
        self.rect.x = 320
        self.rect.y = 570

    def update(self, *args):

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and self.rect.x >= 2:
            self.rect.x += 5
            #self.image = pygame.image.load('data/Imagens/lado1.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_LEFT]: #and self.rect.x <= 880:
            self.rect.x -= 5
            #self.image = pygame.image.load('data/Imagens/lado2.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 5
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 5

        if self.rect.x >= 1020:
            self.rect.x = 1020
        if self.rect.y >= 610:
            self.rect.y = 610
class Guy5(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/personagemcerto.png')
        self.image = pygame.transform.scale(self.image, [45, 75])
        self.rect = pygame.Rect(40, 70, 40, 70)
        self.rect.x = 325
        self.rect.y = 450

    def update(self, *args):

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and self.rect.x >= 2:
            self.rect.x += 5
            #self.image = pygame.image.load('data/Imagens/lado1.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_LEFT]: #and self.rect.x <= 880:
            self.rect.x -= 5
            #self.image = pygame.image.load('data/Imagens/lado2.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 5
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 5

        if self.rect.x >= 1020:
            self.rect.x = 1020
        if self.rect.y >= 610:
            self.rect.y = 610
class Guy6(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/personagemcerto.png')
        self.image = pygame.transform.scale(self.image, [45, 75])
        self.rect = pygame.Rect(40, 70, 40, 70)
        self.rect.x = 549
        self.rect.y = 450

    def update(self, *args):

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and self.rect.x >= 2:
            self.rect.x += 5
            #self.image = pygame.image.load('data/Imagens/lado1.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_LEFT]: #and self.rect.x <= 880:
            self.rect.x -= 5
            #self.image = pygame.image.load('data/Imagens/lado2.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 5
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 5

        if self.rect.x >= 1020:
            self.rect.x = 1020
        if self.rect.y >= 610:
            self.rect.y = 610
class Guy7(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/personagemcerto.png')
        self.image = pygame.transform.scale(self.image, [45, 75])
        self.rect = pygame.Rect(40, 70, 40, 70)
        self.rect.x = 849
        self.rect.y = 450

    def update(self, *args):

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and self.rect.x >= 2:
            self.rect.x += 5
            #self.image = pygame.image.load('data/Imagens/lado1.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_LEFT]: #and self.rect.x <= 880:
            self.rect.x -= 5
            #self.image = pygame.image.load('data/Imagens/lado2.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 5
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 5

        if self.rect.x >= 1020:
            self.rect.x = 1020
        if self.rect.y >= 610:
            self.rect.y = 610
class Guy8(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/personagemcerto.png')
        self.image = pygame.transform.scale(self.image, [45, 75])
        self.rect = pygame.Rect(40, 70, 40, 70)
        self.rect.x = 849
        self.rect.y = 335

    def update(self, *args):

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and self.rect.x >= 2:
            self.rect.x += 5
            #self.image = pygame.image.load('data/Imagens/lado1.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_LEFT]: #and self.rect.x <= 880:
            self.rect.x -= 5
            #self.image = pygame.image.load('data/Imagens/lado2.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 5
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 5

        if self.rect.x >= 1020:
            self.rect.x = 1020
        if self.rect.y >= 610:
            self.rect.y = 610
class Guy9(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/personagemcerto.png')
        self.image = pygame.transform.scale(self.image, [45, 75])
        self.rect = pygame.Rect(40, 70, 40, 70)
        self.rect.x = 550
        self.rect.y = 335

    def update(self, *args):

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and self.rect.x >= 2:
            self.rect.x += 5
            #self.image = pygame.image.load('data/Imagens/lado1.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_LEFT]: #and self.rect.x <= 880:
            self.rect.x -= 5
            #self.image = pygame.image.load('data/Imagens/lado2.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 5
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 5

        if self.rect.x >= 1020:
            self.rect.x = 1020
        if self.rect.y >= 610:
            self.rect.y = 610
class Guy10(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/personagemcerto.png')
        self.image = pygame.transform.scale(self.image, [45, 75])
        self.rect = pygame.Rect(40, 70, 40, 70)
        self.rect.x = 320
        self.rect.y = 335

    def update(self, *args):

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and self.rect.x >= 2:
            self.rect.x += 5
            #self.image = pygame.image.load('data/Imagens/lado1.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_LEFT]: #and self.rect.x <= 880:
            self.rect.x -= 5
            #self.image = pygame.image.load('data/Imagens/lado2.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 5
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 5

        if self.rect.x >= 1020:
            self.rect.x = 1020
        if self.rect.y >= 610:
            self.rect.y = 610
class Guy11(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/personagemcerto.png')
        self.image = pygame.transform.scale(self.image, [45, 75])
        self.rect = pygame.Rect(40, 70, 40, 70)
        self.rect.x = 320
        self.rect.y = 225

    def update(self, *args):

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and self.rect.x >= 2:
            self.rect.x += 5
            #self.image = pygame.image.load('data/Imagens/lado1.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_LEFT]: #and self.rect.x <= 880:
            self.rect.x -= 5
            #self.image = pygame.image.load('data/Imagens/lado2.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 5
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 5

        if self.rect.x >= 1020:
            self.rect.x = 1020
        if self.rect.y >= 610:
            self.rect.y = 610
class Guy12(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('Restos/personagemcerto.png')
        self.image = pygame.transform.scale(self.image, [45, 75])
        self.rect = pygame.Rect(40, 70, 40, 70)
        self.rect.x = 550
        self.rect.y = 225

    def update(self, *args):

        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_RIGHT]: # and self.rect.x >= 2:
            self.rect.x += 5
            #self.image = pygame.image.load('data/Imagens/lado1.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_LEFT]: #and self.rect.x <= 880:
            self.rect.x -= 5
            #self.image = pygame.image.load('data/Imagens/lado2.png')
            #self.image = pygame.transform.scale(self.image, [45, 75])

        if comandos[pygame.K_UP]: # and pos_x <= 870:
            self.rect.y -= 5
        if comandos[pygame.K_DOWN]: # and pos_x <= 870:
            self.rect.y += 5

        if self.rect.x >= 1020:
            self.rect.x = 1020
        if self.rect.y >= 610:
            self.rect.y = 610