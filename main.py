import pygame
import math
import random

#Initializing the pygame, for every game
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load("background.jpg")


#Title and logo
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("gameboy.png")
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load("chips.png")
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load("sauna.png"))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = playerX
bulletY = 480
bulletY_change = 0

def bullet(x,y):
    screen.blit(bulletImg,(x+16,y+10))


def player(x,y):
    screen.blit(playerImg,(x, y))

def enemy(x,y):
    for i in range(num_of_enemy):
        screen.blit(enemyImg[i],(x, y))

def isCollision(enX, enY, bulX,bulY):
    distance1 = math.sqrt( math.pow(enX-bulX,2) + math.pow(enY-bulY,2) )
    distance2 = math.sqrt( math.pow(playerX+16-bulX,2) + math.pow(playerY+10-bulY,2) )
    if distance1 < 27 and distance2 <27:
        return 1
    elif distance1 < 27:
        return 2
    elif distance2 < 27:
        return 3
    else:
        return 4


f=0
score =0

#Game loop
running= True
while running:

    if f == 0:
        bulletX = playerX

    screen.fill((0, 0, 0))

    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                playerX_change = -6
            if event.key == pygame.K_RIGHT :
                playerX_change = 6
            if event.key == pygame.K_SPACE:
                bulletY_change = -8
                f += 1
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0



    playerX += playerX_change
    bulletY += bulletY_change

    if bulletY<=0:
        bulletY = 480
        bulletY_change = 0
        f = 0

    bullet(bulletX, bulletY)

    if playerX<=0:
        playerX = 0
    elif playerX>=736:
        playerX = 736
    #this should come after screen.fill()
    player(playerX, playerY)

    for i in range(num_of_enemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i]>=736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        enemy(enemyX[i], enemyY[i])

        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY) == 2:
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)
            score += 1
            #print(score)
            bulletY = 480
            bulletY_change = 0
            f = 0
        elif isCollision(enemyX[i], enemyY[i], bulletX, bulletY) == 1 or isCollision(enemyX[i], enemyY[i], bulletX, bulletY) == 3:
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)
    #for every game
    pygame.display.update()
