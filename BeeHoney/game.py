from obj import Obj, Bee, Text
import random


class Game:

    # Initialize the game object and set its initial properties
    def __init__(self):

        # Set the background and its position
        self.bg = Obj("Python Course/BeeHoney/assets/bg.png", 0, 0)
        self.bg2 = Obj("Python Course/BeeHoney/assets/bg.png", 0, -640)

        # Set the spider and its position
        self.spider = Obj(
            "Python Course/BeeHoney/assets/spider1.png", random.randrange(0, 295), -50)

        self.flower = Obj(
            "Python Course/BeeHoney/assets/florwer1.png", random.randrange(0, 295), -50)
        
        # Set the bee and its initial position
        self.bee = Bee("Python Course/BeeHoney/assets/bee1.png", 150, 600)

        # Set the change_scene flag to False, to indicate that the game is not over yet
        self.change_scene = False

        # Set the score and lives text objects
        self.score = Text(120, "0")
        self.lives = Text(55, "3")

    # Draw the objects on the display
    def draw(self, display):
        self.bg.draw(display)
        self.bg2.draw(display)
        self.spider.draw(display)
        self.flower.draw(display)
        self.bee.draw(display)
        self.score.draw(display, 160, 50)
        self.lives.draw(display, 20, 20)

    # Update the game state
    def update(self):
        # Move the background
        self.move_bg()

        # Animate the spider and move it
        self.spider.animation("spider", 6.5, 4)
        self.move_spiders()

         # Animate the flower and move it
        self.flower.animation("florwer", 3.5, 2)
        self.move_flower()

        # Animate the bee and check for collision with spider and flower
        self.bee.animation("bee", 3, 4)
        self.bee.colision(self.spider.group, "spider")
        self.bee.colision(self.flower.group, "flower")

        # Update the score and lives text objects
        self.score.update_text(str(self.bee.points))
        self.lives.update_text(str(self.bee.hp))

        # Check if the game is over
        self.endgame()

    # Move the background objects
    def move_bg(self):
        self.bg.sprite.rect[1] += 5
        self.bg2.sprite.rect[1] += 5

        # If the background goes out of screen, reset its position 
        if self.bg.sprite.rect[1] >= 640 or self.bg2.sprite.rect[1] >= 0:
            self.bg.sprite.rect[1] = 0
            self.bg2.sprite.rect[1] = -640

    # Move the spiders and reset their position when they go out of screen
    def move_spiders(self):
        self.spider.sprite.rect[1] += 10
        if self.spider.sprite.rect[1] >= 700:
            self.spider.sprite.kill()
            self.spider = Obj(
                "Python Course/BeeHoney/assets/spider1.png", random.randrange(0, 295), -50)

    # Move the flowers and reset their position when they go out of screen
    def move_flower(self):
        self.flower.sprite.rect[1] += 7
        if self.flower.sprite.rect[1] >= 700:
            self.flower.sprite.kill()
            self.flower = Obj(
                "Python Course/BeeHoney/assets/florwer1.png", random.randrange(0, 295), -50)

    def endgame(self):
        # Check if the bee has run out of hit points (hp)
        if self.bee.hp <= 0:
            # If the bee is out of hp, set the change_scene attribute to True
            # To indicate that the game should transition to a different scene or menu
            self.change_scene = True
