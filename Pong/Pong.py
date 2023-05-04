# Importing necessary modules
from glob import glob
from platform import python_branch
import pygame

# Initializing pygame module
pygame.init()

# Creating a display window with dimensions 1280 x 720
display = pygame.display.set_mode([1280, 720])

# Setting the caption of the window as 'Pong'
title = pygame.display.set_caption('Pong')

# Loading all the required images from the given file paths and storing them in corresponding variables
map = pygame.image.load("Python Course/Pong/assets/field.png")
player1 = pygame.image.load("Python Course/Pong/assets/player1.png")
player2 = pygame.image.load("Python Course/Pong/assets/player2.png")
ball = pygame.image.load("Python Course/Pong/assets/ball.png")
scorep1_img = pygame.image.load("Python Course/Pong/assets/score/0.png")
scorep2_img = pygame.image.load("Python Course/Pong/assets/score/0.png")
gameover = pygame.image.load("Python Course/Pong/assets/win.png")

# Setting the main loop variable as True
loop = True

# Initializing the scores of player1 and player2 as 0
score_p1 = 0
score_p2 = 0

# Setting the initial position of player1 as 290 on the y-axis
player1_y = 290

# Setting flags to move player1 up and down
player1_moveup = False
player1_movedown = False


# Setting the initial position of player2 as 290 on the y-axis
player2_y = 290

# Setting flags to move player2 up and down
player2_moveup = False
player2_movedown = False

# Setting the initial position of ball at the center of the screen
ball_x = 617
ball_y = 337

# Setting the horizontal direction/speed of the ball
ball_direction = -17

# Setting the vertical direction of the ball
ball_y_dir = 1

# Function to move player1
def player1_movement():
    global player1_y
    
    # If player1 is moving up
    if player1_moveup:
        player1_y -= 5
    else:
        player1_y += 0

    # If player1 is moving down
    if player1_movedown:
        player1_y += 5
    else:
        player1_y += 0

    # Setting boundaries for player1 movement
    if player1_y >= 575:
        player1_y = 575
    elif player1_y <= 0:
        player1_y = 0


def player2_movement():
    global player2_y

    # If player2 is moving up
    if player2_moveup:
        player2_y -= 5
    else:
        player2_y += 0

    # If player2 is moving down
    if player2_movedown:
        player2_y += 5
    else:
        player2_y += 0

    # Setting boundaries for player2 movement
    if player2_y >= 575:
        player2_y = 575
    elif player2_y <= 0:
        player2_y = 0

# Function to move the ball
def ball_movement():
    global ball_x
    global ball_y
    global ball_direction
    global ball_y_dir
    global score_p1
    global score_p2
    global scorep1_img
    global scorep2_img

    # Moving the ball
    ball_x += ball_direction
    ball_y += ball_y_dir

    # Checks for collision between the ball and the players' paddles

    # Check for collision with player 1 paddle
    if ball_x < 125:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_direction *= -1
    
    # Check for collision with player 2 paddle
    if ball_x > 1100:
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_direction *= -1

    # Check if ball hits the top or bottom walls
    if ball_y > 675:
        ball_y_dir *= -1
    elif ball_y <= 0:
        ball_y_dir *= -1

    # Reset the ball if it goes out of bounds and update the score
    if ball_x < -50:
        ball_x = 617
        ball_y = 337
        ball_direction *= -1
        ball_y_dir *= -1
        score_p2 += 1
        scorep2_img = pygame.image.load(
            "Python Course/Pong/assets/score/" + str(score_p2) + ".png")
    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_direction *= -1
        ball_y_dir *= -1
        score_p1 += 1
        scorep1_img = pygame.image.load(
            "Python Course/Pong/assets/score/" + str(score_p1) + ".png")

# Display game assets
def assets():
    if score_p1 < 9 and score_p2 < 9:
        display.blit(map, (0, 0))
        display.blit(player1, (50, player1_y))
        display.blit(player2, (1150, player2_y))
        display.blit(ball, (ball_x, ball_y))
        display.blit(scorep1_img, (500, 50))
        display.blit(scorep2_img, (710, 50))
        ball_movement()
        player1_movement()
        player2_movement()
    else:
        display.blit(gameover, (300, 300))

# Check for player 1 controls
def player1_controls():
    global player1_moveup
    global player1_movedown

    if events.type == pygame.KEYDOWN:
        if events.key == pygame.K_w:
            player1_moveup = True
        elif events.key == pygame.K_s:
            player1_movedown = True

    if events.type == pygame.KEYUP:
        if events.key == pygame.K_w:
            player1_moveup = False
        elif events.key == pygame.K_s:
            player1_movedown = False

# Check for player 2 controls
def player2_controls():
    global player2_moveup
    global player2_movedown

    # Check if a key is pressed down
    if events.type == pygame.KEYDOWN:
        # If the key pressed is the up arrow key
        if events.key == pygame.K_UP:
            player2_moveup = True

        # If the key pressed is the down arrow key
        elif events.key == pygame.K_DOWN:
            player2_movedown = True

    # Check if a key is released
    if events.type == pygame.KEYUP:
        # If the key released is the up arrow key
        if events.key == pygame.K_UP:
            player2_moveup = False

        # If the key released is the down arrow key    
        elif events.key == pygame.K_DOWN:
            player2_movedown = False

# Main game loop
while loop:

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

        player1_controls()
        player2_controls()

    assets()
    pygame.display.update()