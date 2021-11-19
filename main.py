import pygame
pygame.init()
win=pygame.display.set_mode((1200,400))
track=pygame.image.load('track2.png')
car=pygame.image.load('tesla.png')
car=pygame.transform.scale(car,(30,60))
carx=151
cary=300
focal=25
clock=pygame.time.Clock()
start=True
direct='up'
camx_offset=0
camy_offset=0
while start:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            start=False
    clock.tick(60)
    camx=carx+camx_offset+16
    camy=cary+camy_offset+15
    pygame.draw.circle(win, (0, 255, 0), (camx, camy), 5, 5)
    up=win.get_at((camx,camy-focal))[0]
    down=win.get_at((camx,camy-+focal))[0]
    right=win.get_at((camx+focal,camy))[0]
    #print(up,right)
    if direct=='up' and up!=255 and right==255:
        direct='right'
        camx_offset=30
        car=pygame.transform.rotate(car,-90)
    elif direct=='right' and right!=255 and down==255:
        direct='downward'
        car=pygame.transform.rotate(car,-90)
        carx=carx+30
        camx_offset=0
        camy_offset=30
    #print(up)
    if direct=='up' and up==255:
        cary = cary - 3
    elif direct=='right' and right==255:
        camx=camx+3
    elif direct=='downward' and down==255:
        cary=cary+3
    win.blit(track,(0,0))
    win.blit(car,(carx,cary))


    pygame.display.update()
