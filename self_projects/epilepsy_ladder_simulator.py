import pygame, random

pygame.init()

scrn=pygame.display.set_mode((1000,500))

clock=pygame.time.Clock()

rects=[]
for i in range(2000):
    rects.append(pygame.Rect(random.randint(-50,950),random.randint(-25,475),random.randint(1,200),random.randint(1,100)))

plat=[]
for i in range(50):
    plat.append(pygame.Rect(random.randint(-10,960),random.randint(0,490),50,10))


x,y=480,450

run=True
fall=0
while run:
    jump=False
    rects=[]
    for i in range(random.randint(1250,5000)):
        rects.append(pygame.Rect(random.randint(0,1950),random.randint(0,975),random.randint(1,200),random.randint(1,100)))
    
    scrn.fill((255, 255, 255))
    for i in rects:
        pygame.draw.rect(scrn,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),i)
    pygame.draw.rect(scrn,(0,0,255),(x,y,20,50))

    for i in plat:
        pygame.draw.rect(scrn,(0,0,0),i)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and fall==0:
        fall-=15
        jump=True
    if keys[pygame.K_a]:
        x-=5
    if keys[pygame.K_d]:
        x+=5
    if x<0: x=0
    if y<0: y=0
    if x>980: x=980
    if y>450: y=450
    if y!=450: fall+=0.5
    for i in plat:
        if y<=i.y+10 and y+50>=i.y:
            if x>i.x-20 and x<i.x+50:
                if not jump:
                    fall=0
    y+=fall
    if y>=450: fall=0
    

    clock.tick(60)

    pygame.display.flip()
