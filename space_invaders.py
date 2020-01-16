# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 09:34:28 2020

@author: ANANTA SRIKAR
"""

import pygame
import random

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

def player(x, y):
    screen.blit(playerImage, (x, y)) #draws the player

# enemy
enemyImage = pygame.image.load('res/enemy.png')

enemyX = random.randint(0,800)
enemyY = random.randint(50,150)

enemyX_change = 0.3
enemyY_change = 40

def enemy(x,y):
    screen.blit(enemyImage, (x,y))

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

    #adding boundaries to player's ship       
    playerX += playerX_change
    
    if (playerX < 0):
        playerX = 0
    
    elif (playerX > 736):
        playerX = 736

    enemyX += enemyX_change
    
    if (enemyX < 0):
        enemyX = 0
        enemyX_change = -enemyX_change
        enemyY += enemyY_change
    
    elif (enemyX > 736):
        enemyX = 736
        enemyX_change = -enemyX_change
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()