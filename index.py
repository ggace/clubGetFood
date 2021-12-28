import pygame
import random

def myimg(img, x,y):
    screen.blit(img, (x,y))

pygame.init()

pygame.display.set_caption("음식 받기") #<title>

#스크린 구성
size  = [800,600]
screen= pygame.display.set_mode(size)

finish = False

fallingObjectsize = (100, 100)

cakeImg = pygame.transform.scale(pygame.image.load('resources\cake.png'), fallingObjectsize)
cookieImg = pygame.transform.scale(pygame.image.load('resources\cookie.webp'), fallingObjectsize)
shitImg = pygame.transform.scale(pygame.image.load('resources\shit.png'), fallingObjectsize)

class Image:
    def __init__(self, img, score):
        self.image = img
        self.score = score

cake = Image(cakeImg, 3) 
cookie = Image(cookieImg,1)
shit = Image(shitImg, -1)

cakeLocate = [0,0]
cookieLocate = [0,0]
shitLocate = [0,0]

while not(finish):
    screen.fill((255,255,255))

    locate = cakeLocate
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
    
    myimg(cake.image, cakeLocate[0], cakeLocate[1])
    myimg(cookie.image,cookieLocate[0],cookieLocate[1])
    myimg(shit.image,shitLocate[0],shitLocate[1])

    if(locate[1] < size[1]-fallingObjectsize[1]):
        locate[1] += 1
    else:
        locate[1] = 0
        locate[0] = random.randint(0, size[0]-fallingObjectsize[0])
    pygame.display.flip()