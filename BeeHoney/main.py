import pygame
from menu import Menu, GameOver
from game import Game


class Main:
    # Initializes the game window and the Menu, Game, and GameOver classes. It also sets a loop flag and initializes a Pygame clock.
    def __init__(self, resx, resy, title):

        self.display = pygame.display.set_mode([resx, resy])
        self.title = pygame.display.set_caption(title)

        self.menu = Menu("Python Course/BeeHoney/assets/start.png")
        self.game = Game()
        self.gameover = GameOver("Python Course/BeeHoney/assets/gameover.png")

        # Initialize loop flag and Pygame clock
        self.loop = True
        self.fps = pygame.time.Clock()

    # Handles drawing of the Menu, Game, and GameOver screens depending on which one is active.
    def draw(self):
        if self.menu.change_scene == False:
            self.menu.draw(self.display)
        elif self.game.change_scene == False:
            self.game.draw(self.display)
            self.game.update()
        elif self.gameover.change_scene == False:
            self.gameover.draw(self.display)
        else:
            self.menu.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.bee.hp = 3
            self.game.bee.points = 0

    # Handles Pygame events, such as quitting the game or moving the bee character in the game.
    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            elif self.menu.change_scene == False:
                self.menu.events(events)
            elif self.game.change_scene == False:
                self.game.bee.bee_move(events)
            else:
                self.gameover.events(events)
    # Runs the main game loop, calling the draw and events methods and updating the display.
    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pygame.display.update()

# Create an instance of the Main class with a window size of 360x640 pixels and a title of "BeeHoney"
game = Main(360, 640, "BeeHoney")

# Call the update method to start the game loop
game.update()
