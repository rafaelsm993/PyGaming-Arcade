from asyncio import events
import pygame
from obj import Obj

class Menu:

    def __init__(self, image):
        # Create a menu object using an image file path and set its position to (0, 0)
        self.menu = Obj(image, 0, 0)
        
        # Create a flag to indicate whether or not the scene should change
        self.change_scene = False

    def draw(self, display):
        # Draw the menu object on the display surface
        self.menu.draw(display)

    def events(self, event):
        # Check if a key is pressed
        if event.type == pygame.KEYDOWN:
            # Check if the key is the "return" key (Enter)
            if event.key == pygame.K_RETURN:
                # If the "return" key is pressed, set the change_scene flag to True
                # to indicate that the game should transition to a different scene or menu
                self.change_scene = True

class GameOver(Menu):
    def __init__(self, image):
        # Call the constructor of the Menu class to create a menu object using the given image
        super().__init__(image)
