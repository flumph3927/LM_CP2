import pygame, random

pygame.init()

scrn=pygame.display.set_mode((2000,1000))

clock=pygame.time.Clock()

plat=[]
for i in range(50):
    plat.append(pygame.Rect(random.randint(0,1970),random.randint(0,970),30,30))

vic=pygame.Rect(random.randint(0,1970),random.randint(0,970),30,30)

x,y=480,450

score=0

font = pygame.font.SysFont(None, 32)

run=True
xmove=0
ymove=0
while run:
    text = font.render(f'Score: {score}',True,(0,0,0))
    char=pygame.Rect(x,y,20,50)
    scrn.fill((255, 255, 255))

    for i in plat:
        pygame.draw.rect(scrn,(255,0,0),i)
        if i.colliderect(char):
            vic=pygame.Rect(random.randint(0,1970),random.randint(0,970),30,30)
            score=0
            plat=[]
            for i in range(50):
                pble=pygame.Rect(random.randint(0,1970),random.randint(0,970),30,30)
                if not pble.colliderect(char):
                    plat.append(pygame.Rect(random.randint(0,1970),random.randint(0,970),30,30))

    pygame.draw.rect(scrn,(0,255,0),vic)

    if vic.colliderect(char):
        vic=pygame.Rect(random.randint(0,1970),random.randint(0,970),30,30)
        score+=1
        plat=[]
        for i in range(50):
            pble=pygame.Rect(random.randint(0,1970),random.randint(0,970),30,30)
            if not pble.colliderect(char):
                plat.append(pygame.Rect(random.randint(0,1970),random.randint(0,970),30,30))

    pygame.draw.rect(scrn,(0,0,255),char)

    scrn.blit(text,(10,10))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ymove-=0.1
    if keys[pygame.K_s]:
        ymove+=0.1
    if keys[pygame.K_a]:
        xmove-=0.1
    if keys[pygame.K_d]:
        xmove+=0.1
    x+=xmove
    y+=ymove
    if x<0: x=0
    if y<0: y=0
    if x>1980: x=1980
    if y>950: y=950

    clock.tick(60)

    pygame.display.flip()