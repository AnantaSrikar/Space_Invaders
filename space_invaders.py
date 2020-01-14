# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 09:34:28 2020

@author: ANANTA SRIKAR
"""

import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('res/rocket.png')
pygame.display.set_icon(icon)

#player
playerImage = pygame.image.load('res/spaceship.png')

playerX = 370
playerY = 480

playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImage, (x, y)) #draws the player

running = True

#game loop
while(running):

    screen.fill((0,0,0)) #(R, G, B)

    for event in pygame.event.get():
        if (event.type == pygame.QUIT): #quits game when close button is pressed
            running = False
        if (event.type == pygame.KEYDOWN):

            if (event.key == pygame.K_LEFT):
                playerX_change = -0.3

            if (event.key == pygame.K_RIGHT):
                playerX_change += 0.3

        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                playerX_change = 0
            
    playerX += playerX_change
    
    if (playerX < 0):
        playerX = 0
    
    if (playerX > 736):
        playerX = 736

    player(playerX, playerY)
    pygame.display.update()