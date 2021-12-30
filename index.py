import pygame
import random
import values

class Image:
    def __init__(self, img, score, locate):
        self.image = img
        self.score = score
        self.locate = locate
def showImg(img, x,y):
    screen.blit(img, (x,y))
def showImgs(imgs):
    for img in imgs:
        showImg(img.image, img.locate[0], img.locate[1])
def loadImage(path, size):
    return pygame.transform.scale(pygame.image.load(path), size)

def getTextByTop(text, fontsize, textColor, bgcolor, x, y):
    font = pygame.font.Font('freesansbold.ttf', fontsize) 
    text = font.render(text, True, textColor, bgcolor)
    textRect = text.get_rect()
    textRect.x = x
    textRect.y = y
    return text, textRect
def getTextByCenter(text, fontsize, textColor, bgcolor, x, y):
    font = pygame.font.Font('freesansbold.ttf', fontsize) 
    text = font.render(text, True, textColor, bgcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    return text, textRect


def movePocket():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]: pocket.locate[0] -= values.pocketSpeed*speed
    elif pressed[pygame.K_d]: pocket.locate[0] += values.pocketSpeed*speed
    elif pressed[pygame.K_RIGHT]: pocket.locate[0] += values.pocketSpeed*speed
    elif pressed[pygame.K_LEFT]: pocket.locate[0] -= values.pocketSpeed*speed
    
def resetFallObject():
    global turn
    global locate
    global speed
    global fallSpeed
    global objects
    global objectIndex
    
    turn += 1
    
    locate[1] = 0-values.fallingObjectsize[1]
    objectIndex = random.choice(percentages)
    locate = objects[objectIndex].locate
    locate[0] = random.randint(0, values.size[0]-values.fallingObjectsize[0])
    
    fallSpeed = values.fallSpeed * speed
    speed += values.addingSpeed
    
#시작
pygame.init()

#title
pygame.display.set_caption("음식 받기")

#스크린
screen= pygame.display.set_mode(values.size)

#트리거
finish = False
isSetUp = True
isGameIn = True
gameStartTrigger = False

#이미지 불러오기
backgroundImg = loadImage(r'resources\background.jpg', (values.size[0], values.size[1]))
cakeImg = loadImage(r'resources\cake.png', values.fallingObjectsize)
cookieImg = loadImage(r'resources\cookie.png', values.fallingObjectsize)
shitImg = loadImage(r'resources\shit.png', values.fallingObjectsize)
pocketImg = loadImage(r'resources\pocket.png', values.pocketObjectsize)

#이미지 클래스화(이미지 파일, 점수, 위치)
cake = Image(cakeImg, values.cakeScore, [random.randint(0, values.size[0]-values.fallingObjectsize[0]),0]) 
cookie = Image(cookieImg,values.cookieScore, [random.randint(0, values.size[0]-values.fallingObjectsize[0]),0])
shit = Image(shitImg, values.shitScore, [random.randint(0, values.size[0]-values.fallingObjectsize[0]),0])
pocket = Image(pocketImg, None, [values.size[0]/2-values.pocketObjectsize[0]/2,values.size[1] - values.pocketObjectsize[1] - 10])

#기본 세팅
score = 0
maxScore = score
turn = 0
objects = [cake, cookie, shit]
speed = values.speed
fallSpeed = values.fallSpeed

#문자 세팅
scoreText, scoreTextRect = getTextByTop(f'SCORE : {score}', 20, values.textColor,values.bgcolor, values.smallNotice[0], values.smallNotice[1])
maxscoreText, maxscoreTextRect = getTextByTop(f'MAX SCORE : {maxScore}', 20, values.textColor,values.bgcolor, values.smallNotice[0], values.smallNotice[1]+20)
turnText, turnTextRect = getTextByTop(f'TURN : {turn}', 20, values.textColor,values.bgcolor, values.smallNotice[0], values.smallNotice[1]+40)
maxscoreLargeText, maxscoreLargeTextRect = getTextByCenter(f'MAX SCORE : {maxScore}', 50, values.textColor,values.bgcolor, values.bigNotice[0], values.bigNotice[1]-25)
turnLargeText, turnLargeTextRect = getTextByCenter(f'TURN : {turn}', 50, values.textColor,values.bgcolor, values.bigNotice[0], values.bigNotice[1]+25)
restartLargeText, restartLargeTextRect = getTextByCenter(f'PRESS SPACE BAR TO RESTART', 20, values.textColor,values.bgcolor, values.bigNotice[0], values.bigNotice[1]+60)

#확률 작업
percentages = []

for i in range(values.cakePercentage):
    percentages.append(0)
for i in range(values.cookiePercentage):
    percentages.append(1)
for i in range(values.shitPercentage):
    percentages.append(2)

#object 선택
objectIndex = random.choice(percentages)
locate = objects[objectIndex].locate

#게임 시작
while not(finish):
    #배경화면
    showImg(backgroundImg, 0,0)

    #이벤트 처리
    for event in pygame.event.get():
        #종료처리
        if event.type == pygame.QUIT:
            finish = True
        
            
    #게임 중
    if(isGameIn):
        #시작시 초기화
        if(isSetUp):
            score = 0
            maxScore = score
            turn = 0
            speed = values.speed
            fallSpeed = values.fallSpeed
            
            objectIndex = random.choice(percentages)
            locate = objects[objectIndex].locate
            
            cake = Image(cakeImg, values.cakeScore, [random.randint(0, values.size[0]-values.fallingObjectsize[0]),0]) 
            cookie = Image(cookieImg,values.cookieScore, [random.randint(0, values.size[0]-values.fallingObjectsize[0]),0])
            shit = Image(shitImg, values.shitScore, [random.randint(0, values.size[0]-values.fallingObjectsize[0]),0])
            pocket = Image(pocketImg, None, [values.size[0]/2-values.pocketObjectsize[0]/2,values.size[1] - values.pocketObjectsize[1] - 10])  
        #트리거 처리 
        isSetUp = False 
        
        #pocket 움직임 처리
        movePocket()
        
        #포켓 위치 제한
        if(pocket.locate[0] < 0): pocket.locate[0] = 0
        elif(pocket.locate[0] > values.size[0]-values.pocketObjectsize[0]): pocket.locate[0] = values.size[0]-values.pocketObjectsize[0]
            
        
        
        #받음 처리
        if(locate[1] >= values.size[1]-values.fallingObjectsize[1]):
            #받았을때
            if(locate[0]+values.fallingObjectsize[0] > pocket.locate[0] and locate[0]-values.fallingObjectsize[0] < pocket.locate[0] + values.pocketObjectsize[0] and locate[1] >= values.size[1]-values.fallingObjectsize[1] and locate[1] <= values.size[1]):
                score += objects[objectIndex].score
                
                if(maxScore < score):
                    maxScore = score
                resetFallObject()
                
                
            #못받고 끝에 도달하지 않았을 때
            elif(locate[1] < 1000):
                locate[1] += fallSpeed*speed
                fallSpeed += values.addingFallSpeed * speed
                
                
            #못받고 끝에 도달했을 때
            else:
                resetFallObject()
                
        else:
            locate[1] += fallSpeed*speed
            fallSpeed += values.addingFallSpeed * speed
            
        #text처리
        scoreText, scoreTextRect = getTextByTop(f'SCORE : {score}', 20, values.textColor,values.bgcolor, values.smallNotice[0], values.smallNotice[1])
        maxscoreText, maxscoreTextRect = getTextByTop(f'MAX SCORE : {maxScore}', 20, values.textColor,values.bgcolor, values.smallNotice[0], values.smallNotice[1]+20)
        turnText, turnTextRect = getTextByTop(f'TURN : {turn}', 20, values.textColor,values.bgcolor, values.smallNotice[0], values.smallNotice[1]+40)
        screen.blit(scoreText, scoreTextRect) 
        screen.blit(maxscoreText, maxscoreTextRect) 
        screen.blit(turnText, turnTextRect) 
        #이미지 보여주기
        showImgs([objects[objectIndex], pocket])
        #점수가 0이하일 때
        if(score < 0):  
            isGameIn = False
            gameStartTrigger = False
    #게임 오버
    else:
        #text처리
        maxscoreLargeText, maxscoreLargeTextRect = getTextByCenter(f'MAX SCORE : {maxScore}', 50,values.textColor,values.bgcolor, values.bigNotice[0], values.bigNotice[1]-25)
        turnLargeText, turnLargeTextRect = getTextByCenter(f'TURN : {turn}', 50, values.textColor,values.bgcolor, values.bigNotice[0], values.bigNotice[1]+25)
        screen.blit(maxscoreLargeText, maxscoreLargeTextRect) 
        screen.blit(turnLargeText, turnLargeTextRect) 
        screen.blit(restartLargeText, restartLargeTextRect) 
        #restart
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] and not gameStartTrigger: isGameIn = True; isSetUp = True; gameStartTrigger = True;
        
        
    
        
    pygame.display.flip()