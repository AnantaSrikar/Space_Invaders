import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('res/rocket.png')
pygame.display.set_icon(icon)

#player
playerImage = pygame.image.load('res/spaceship.png')
playerPos = (370, 480) # (X, Y)

def player():
    screen.blit(playerImage, playerPos) #draws the player

running = True

#game loop
while(running):

    screen.fill((0,0,0)) #(R, G, B)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quits game when close button is pressed
            running = False

    player()
    pygame.display.update()