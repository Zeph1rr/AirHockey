import pygame

pygame.init()

wind_width=800
wind_height=480
run = True
rad = 10
red = (255,0,0)
blue = (0,0,255)
white = (255, 255, 255)
black = (0,0,0)
green = (0, 255, 0)
yellow = (255, 255, 0)
x_circ=400
y_circ=240
x_rect1=0
y_rect1=220
x_rect2=wind_width-20
y_rect2=220
pause=False
a=True
b=False
FPS=50
c=20
redscore = 0
bluescore = 0
bg=pygame.image.load('bg1.jpg')
RedCar=pygame.image.load('RedCar.jpg')
BlueCar=pygame.image.load('BlueCar.jpg')

time=pygame.time.Clock()
wind=pygame.display.set_mode((wind_width,wind_height))
pygame.display.set_caption("Airhockey")


menuFontObj = pygame.font.SysFont('arial', 24)



while run:

    time.tick(FPS)
    wind.blit(bg, (0, 0))
    wind.blit(RedCar, (x_rect1, y_rect1))
    wind.blit(BlueCar, (x_rect2, y_rect2))
    score = str(redscore) + ':' + str(bluescore)

    menuText = menuFontObj.render(score, True, white)
    menuRectObj = menuText.get_rect()
    menuRectObj.center = (wind_width/2-10, 100)
    wind.blit(menuText, menuRectObj)
    #pygame.draw.rect(wind, (red), (x_rect1,y_rect1, 20, 40))
    #pygame.draw.rect(wind, (blue), (x_rect2,y_rect2, 20, 40))
    pygame.draw.circle(wind,(yellow), (x_circ,y_circ), rad)
    if x_circ == 0:
        x_circ=400
        y_circ=240
        bluescore=bluescore+1
        pause = False
    if x_circ == wind_width:
        x_circ=400
        y_circ=240
        redscore=redscore+1
        pause = False
    if pause and b:
        x_circ+=5
    elif pause and not b:
        x_circ-=5
    if pause and a:
        y_circ+=5
    elif pause and not a:
        y_circ-=5
    if y_circ==wind_height-rad:
        a=False
    elif y_circ==rad:
        a=True
    if redscore == 6 or bluescore == 6:
        run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not pause:
                    pause = True
                elif pause:
                    pause = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y_rect1-10 >= 0 and pause:
        y_rect1-=10
    elif keys[pygame.K_s] and y_rect1+50 <= wind_height and pause:
        y_rect1+=10
    elif keys[pygame.K_i] and y_rect2-10 >= 0 and pause:
        y_rect2-=10
    elif keys[pygame.K_k] and y_rect2+50 <= wind_height and pause:
        y_rect2+=10
    rect1_xr = range(x_rect1,x_rect1+20)
    rect2_xr = range(x_rect2,x_rect2+20)
    rect1_yr = range(y_rect1, y_rect1+40)
    rect2_yr = range(y_rect2, y_rect2+40)
    if x_circ in rect1_xr and y_circ in rect1_yr:
        b=True
    if x_circ in rect2_xr and y_circ in rect2_yr:
        b=False
    pygame.display.update()
