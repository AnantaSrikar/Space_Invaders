import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

running = True

#game loop
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #quits game when close button is pressed
            running = False
