import pygame
import andrew

class Menu:

    def __init__(self):

        self.bg = andrew("Restos/telastart.png", 0, 0)

        self.change_scene = False

    def draw(self, window):
        self.bg.draw(window)

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_scene = True