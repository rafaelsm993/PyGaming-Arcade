import pygame


class Obj:
    # Constructor for class Obj
    def __init__(self, asset, x, y):

        # Create a group of sprites
        self.group = pygame.sprite.Group()
        # Create a sprite object from the group
        self.sprite = pygame.sprite.Sprite(self.group)

        # Load the image from the given asset path
        self.sprite.image = pygame.image.load(asset)

        # Get the rectangle for the sprite's image and set its position
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        # Initialize the frame and tick for animation
        self.frame = 1
        self.tick = 0

        # Initialize the points and health points
        self.points = 0
        self.hp = 3

    # Method to draw the sprite on the display
    def draw(self, display):
        self.group.draw(display)
    
    # Method for sprite animation
    def animation(self, image, tick, frame):
        # Increment the tick count
        self.tick += 1

        # If the tick count has reached the given value
        if self.tick >= tick:
            self.tick = 0
            self.frame += 1
        
        # If the frame has reached the given limit, reset it to 1
        if self.frame > frame:
            self.frame = 1
        
        # Load the image file for the current frame and update the sprite image
        self.sprite.image = pygame.image.load(
            "Python Course/BeeHoney/assets/" + image + str(self.frame) + ".png")


class Bee(Obj):
    def __init__(self, asset, x, y):
        # Call the constructor of parent class Obj
        super().__init__(asset, x, y)

    # Method for moving the bee sprite
    def bee_move(self, event):
        # If the event type is MOUSEMOTION
        if event.type == pygame.MOUSEMOTION:
            # Update the x and y positions of the sprite
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 30
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 40

    # Method for collision detection with other sprites
    def colision(self, group, name):

        # Store the name of the sprite to be collided with
        name = name


        # Store the name of the sprite to be collided with
        colision = pygame.sprite.spritecollide(self.sprite, group, True)

        # If the collided sprite is a spider, decrement the health points
        if name == "spider" and colision:
            self.hp -= 1
        # If the collided sprite is a flower, increment the points
        elif name == "flower" and colision:
            self.points += 1


class Text:
    # Initialize pygame module
    pygame.init()

    # Constructor for class Text
    def __init__(self, size, text):
        # Set the font type and size
        self.font = pygame.font.SysFont("Arial bold", size)

        # Render the text with the font and color
        self.render = self.font.render(text, True, (255, 255, 255))

    # Method to draw the text on the display
    def draw(self, display, x, y):
        display.blit(self.render, (x, y))

    # Method to update the text with new content
    def update_text(self, update):
        self.render = self.font.render(update, True, (255, 255, 255))
    
