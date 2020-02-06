# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 09:34:28 2020

@author: ANANTA SRIKAR
"""

import pygame
from pygame import mixer
import random
import math

bullet_state = "ready"

restart = True

def main():

    global restart
    global bullet_state

    pygame.init()

    score = 0

    red = (200, 0, 0)
    bright_red = (255, 0, 0)

    screen = pygame.display.set_mode((800,600))

    #Background

    background = pygame.image.load('res/background.png')

    #Background Sound

    mixer.music.load('res/background.wav')

    mixer.music.play(-1) # -1 makes sure it playes forever

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

    enemyImage = []

    enemyX = []
    enemyY = []

    enemyX_change = []
    enemyY_change = []

    no_of_enemies = 6

    for i in range (no_of_enemies):
        enemyImage.append(pygame.image.load('res/enemy.png'))
        enemyX.append(random.randint(0,800))
        enemyY.append(random.randint(50,150))
        enemyX_change.append(2)
        enemyY_change.append(40)

    def enemy(x, y, i):
        screen.blit(enemyImage[i], (x,y))

    running = True

    # bullet 
    bulletImage = pygame.image.load('res/bullet.png')

    bulletX = 0
    bulletY = 0

    bulletYchange = 0
    #bullet_state = "ready"

    def fire_bullet(x,y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImage, (x + 16, y + 10))

    # Score
    font = pygame.font.Font('freesansbold.ttf', 32)
    scoreX = 10
    scoreY = 10

    def showScore(x, y):
        score_rend = font.render("Score : {}".format(score), True, (255, 255, 255))
        screen.blit(score_rend, (x, y))

    # Game Over
    over_font = pygame.font.Font('freesansbold.ttf', 64)

    def show_game_over():
        over_text = over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (200 ,250))

    def button_text(text, coor, textSize):
        button_font = pygame.font.Font('freesansbold.ttf', textSize)
        button_texts  = button_font.render(text, True, (255, 255, 255))
        screen.blit(button_texts, coor)

    def restart_button():
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if ((500 < mouse[0] < 500 + 200)) and (400 < mouse[1] < 400 + 100):
            pygame.draw.rect(screen, bright_red, (500, 400, 200, 100))
            button_text("PLAY AGAIN", (505, 440), 30)
            
            if(click[0] == 1):
                return True

            else :
                return False
        
        else:
            pygame.draw.rect(screen, red, (500, 400, 200, 100)) 
            button_text("PLAY AGAIN", (505, 440), 30)

    def exit_button():
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if ((100 < mouse[0] < 100 + 200)) and (400 < mouse[1] < 400 + 100):
            pygame.draw.rect(screen, bright_red, (100, 400, 200, 100))
            button_text("EXIT", (155, 440), 30)
            
            if(click[0] == 1):
                return True

            else :
                return False
        
        else:
            pygame.draw.rect(screen, red, (100, 400, 200, 100)) 
            button_text("EXIT", (155, 440), 30)   
            

    def isCollision(bulletX, bulletY, enemyX, enemyY):
        distance = math.sqrt((math.pow((bulletX - enemyX), 2) + (math.pow((bulletY - enemyY), 2))))

        if (distance < 27):
            return True
        else:
            return False

    #game loop
    while(running):

        screen.fill((0,0,0)) #(R, G, B)

        screen.blit(background,(0,0))

        for event in pygame.event.get():
            if (event.type == pygame.QUIT): #quits game when close button is pressed
                running = False
                restart = False
            if (event.type == pygame.KEYDOWN):

                if (event.key == pygame.K_LEFT):
                    playerX_change = -3

                if (event.key == pygame.K_RIGHT):
                    playerX_change = 3
                
                if (event.key == pygame.K_SPACE):
                    if (bullet_state == "ready"):
                        bullet_sound = mixer.Sound('res/laser.wav')
                        bullet_sound.play()
                        bulletX = playerX
                        bulletY = playerY
                        bulletYchange = -9
                        fire_bullet(bulletX, bulletY)

            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    playerX_change = 0
                
                
        #adding boundaries to player's ship       
        playerX += playerX_change

        if (bullet_state == "fire"):
            fire_bullet(bulletX, bulletY)
            bulletY += bulletYchange
        
        if (playerX < 0):
            playerX = 0
        
        elif (playerX > 736):
            playerX = 736

        for i in range(no_of_enemies):

            #Game Over

            if (enemyY[i] > 440):
                for j in range(no_of_enemies):
                    enemyY[j] = 2000
                playerY = 2000
                bullet_state = "ready"
                show_game_over()
                if(restart_button()):
                    restart = True
                    running = False

                elif(exit_button()):
                    restart = False
                    running = False
                break
            
            enemyX[i] += enemyX_change[i]
            
            if (enemyX[i] < 0):
                enemyX[i] = 0
                enemyX_change[i] = -enemyX_change[i]
                enemyY[i] += enemyY_change[i]
            
            elif (enemyX[i] > 736):
                enemyX[i] = 736
                enemyX_change[i] = -enemyX_change[i]
                enemyY[i] += enemyY_change[i]
            
            if (isCollision(bulletX, bulletY, enemyX[i], enemyY[i])):
                
                bullet_sound = mixer.Sound('res/explosion.wav')
                bullet_sound.play()            
                bullet_state = "ready"
                bulletY = 480
                score += 1

                enemyX[i] = random.randint(0,800)
                enemyY[i] = random.randint(50,150)
            
            enemy(enemyX[i], enemyY[i], i)

        if (bulletY <= 0):
            bullet_state = "ready"
            
        player(playerX, playerY)

        showScore(scoreX, scoreY)
        
        pygame.display.update()

if __name__ == '__main__':
        while(restart):
            running = True
            main()

    # TODO : Add exit button
    # TODO : Add up arrow as shoot
    # TODO : Store high score
    # TODO : make .exe file