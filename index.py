import pygame
import random

def showImg(img, x,y):
    screen.blit(img, (x,y))

pygame.init()

pygame.display.set_caption("음식 받기") #<title>

#스크린 구성
size  = [800,1000]
screen= pygame.display.set_mode(size)

finish = False

score = 0
maxScore = score

font = pygame.font.Font('freesansbold.ttf', 20) 
scoreText = font.render(f'SCORE : {score}', True, (0,0,0), (255,255,255)) 
scoreTextRect = scoreText.get_rect()  
scoreTextRect.x = 0
scoreTextRect.y = 0
maxscoreText = font.render(f'MAX SCORE : {maxScore}', True, (0,0,0), (255,255,255)) 
maxscoreTextRect = maxscoreText.get_rect()  
maxscoreTextRect.x = 0
maxscoreTextRect.y = 20



fallingObjectsize = (100, 100)
pocketObjectsize = (150, 100)

cakeImg = pygame.transform.scale(pygame.image.load('resources\cake.png'), fallingObjectsize)
cookieImg = pygame.transform.scale(pygame.image.load('resources\cookie.webp'), fallingObjectsize)
shitImg = pygame.transform.scale(pygame.image.load('resources\shit.png'), fallingObjectsize)
pocketImg = pygame.transform.scale(pygame.image.load('resources\pocket.png'), pocketObjectsize)

class Image:
    def __init__(self, img, score, locate):
        self.image = img
        self.score = score
        self.locate = locate

cake = Image(cakeImg, 3, [0,0]) 
cookie = Image(cookieImg,1, [0,0])
shit = Image(shitImg, -4, [0,0])
pocket = Image(pocketImg, 0, [0,size[1] - pocketObjectsize[1]])

objects = [cake, cookie, shit]

cakePercentage = 10
cookiePercentage = 45
shitPercentage = 45

percentages = []

for i in range(cakePercentage):
    percentages.append(0)
for i in range(cookiePercentage):
    percentages.append(1)
for i in range(shitPercentage):
    percentages.append(2)

objectIndex = random.choice(percentages)
locate = objects[objectIndex].locate
speed = 1

fallSpeed = 0.2

resultPercentage = [0,0,0]


isGameIn = True
while not(finish):
    screen.fill((80,100,255))
    

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True
    
    if(isGameIn):
    
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_a]: pocket.locate[0] -= 1*speed
        elif pressed[pygame.K_d]: pocket.locate[0] += 1*speed
        elif pressed[pygame.K_RIGHT]: pocket.locate[0] += 1*speed
        elif pressed[pygame.K_LEFT]: pocket.locate[0] -= 1*speed
        
        if(pocket.locate[0] < 0): pocket.locate[0] = 0
        elif(pocket.locate[0] > size[0]-pocketObjectsize[0]): pocket.locate[0] = size[0]-pocketObjectsize[0]
            
        
        showImg(objects[objectIndex].image, objects[objectIndex].locate[0], objects[objectIndex].locate[1])
        showImg(pocket.image, pocket.locate[0], pocket.locate[1])
        
        
        
        if(locate[1] >= size[1]-fallingObjectsize[1]):
            if(locate[0]+fallingObjectsize[0] > pocket.locate[0] and locate[0]-fallingObjectsize[0] < pocket.locate[0] + pocketObjectsize[0] and locate[1] >= size[1]-fallingObjectsize[1] and locate[1] <= size[1]):
                score += objects[objectIndex].score
                
                if(maxScore < score):
                    maxScore = score
                
                locate[1] = 0-fallingObjectsize[1]
                objectIndex = random.choice(percentages)
                resultPercentage[objectIndex] += 1
                locate = objects[objectIndex].locate
                locate[0] = random.randint(0, size[0]-fallingObjectsize[0])
                fallSpeed = 0.2 * speed
                
                speed += 0.001
                
                print(score)
                
            elif(locate[1] < 1200):
                locate[1] += speed
                fallSpeed += 0.002 * speed
            else:
                
                locate[1] = 0-fallingObjectsize[1]
                objectIndex = random.choice(percentages)
                resultPercentage[objectIndex] += 1
                locate = objects[objectIndex].locate
                locate[0] = random.randint(0, size[0]-fallingObjectsize[0])
                fallSpeed = 0.2 * speed
                speed += 0.001
        
        else:
            locate[1] += speed
            fallSpeed += 0.002 * speed
        scoreText = font.render(f'SCORE : {score}', True, (0,0,0), (255,255,255)) 
        maxscoreText = font.render(f'MAX SCORE : {maxScore}', True, (0,0,0), (255,255,255)) 
        screen.blit(scoreText, scoreTextRect) 
        screen.blit(maxscoreText, maxscoreTextRect) 
        if(score < 0): 
            isGameIn = False
    
    
        
    pygame.display.flip()