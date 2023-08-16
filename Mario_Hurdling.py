import pygame
pygame.init()

#Set up screen
screen=pygame.display.set_mode((1200,600))

#Set up Mariothat moves
Q=12
mario=[0]*Q
for i in range(12):
    mario[i]=pygame.sprite.Sprite()
    mario[i].image=pygame.image.load(str(i)+'.png')
    mario[i].image=pygame.transform.scale(mario[i].image,(100,100))
    
#Main Mario
Mario=pygame.sprite.Sprite()
Mario.image=pygame.image.load('0.png')
Mario.image=pygame.transform.scale(Mario.image,(100,100))
x=50
y=550
Mario.rect=mario[0].image.get_rect(center=(x,y))

#Set pipes
pipes=pygame.sprite.Sprite()
pipes.image=pygame.image.load('bg5.png')
pipes.rect=pipes.image.get_rect()

#Set background
bground=pygame.sprite.Sprite()
bground.image=pygame.image.load('bg8.png')

#Set Start Button
button=pygame.image.load('start1.png')
button_rect=button.get_rect(center=(500,250))
screen.blit(button,button_rect)

#Set collision
collision,collision1=0,0
x,y=350,500
dx,dy=2,-24
clock=pygame.time.Clock()
jump=False
count=-1
width=1700
i=0
Sum=0
font = pygame.font.SysFont(None, 30)

#set game start
game_started=False

#Set time
elapsed_time=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    #Game Starts
    if game_started:
        count+=1 #(count=count+1)
        count1=count//3
        count2=count1%Q
        i=i-10
        screen.blit(bground.image,(0,0))
        count+=1 #(count=count+1)
        count1=count//4
        count2=count1%Q
        pipes.rect=pipes.image.get_rect(center=(900+2*i,300))
        screen.blit(pipes.image,pipes.rect)
        if i<-width:
            i=0
        keys=pygame.key.get_pressed()
        Mario.rect=mario[count2].image.get_rect(center=(x,y))
        screen.blit(mario[count2].image,Mario.rect)
        if keys[pygame.K_UP]:
                jump=True
        if jump:
            y=y+dy
            dy+=2
            if y>500:
                jump=False
                dy=-24
        collision=pygame.sprite.collide_mask(pipes,Mario)
        if collision==None:
            collision=0
        if collision!=0:
            collision=1
        delta=collision-collision1
        if delta==1:
            Sum=Sum+1
            print('Sum=',Sum)
            
        # Calculate the elapsed time
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000

        # Display the elapsed time on the screen
        font = pygame.font.SysFont(None, 30)
        time_text = font.render("Time: " + str(elapsed_time) + " seconds", True, 'white')
        screen.blit(time_text, (10, 10))
            
        penalty_text = font.render("penalty number= " + str(Sum), True, 'white')
        screen.blit(penalty_text, (10, 40))
        collision1=collision
    else:
        screen.blit(bground.image,(0,0))
        screen.blit(button,button_rect)
        screen.blit(pipes.image,pipes.rect)
        count2=0
        screen.blit(mario[count2].image,Mario.rect)
        if event.type == pygame.MOUSEBUTTONDOWN:# and event.button == 1:
            if button_rect.collidepoint(event.pos):
                game_started = True
                start_time = pygame.time.get_ticks()  # Record the start time when the game starts
                
    if elapsed_time >= 60:
       
        game_started = False  # Stop the game
            
        screen.fill('blue')
        button_rect = pygame.Rect(500, 250, 250, 50)
        pygame.draw.rect(screen, 'red', button_rect)
        button_font = pygame.font.SysFont(None, 50)
        button_text = button_font.render("GameOver", True, 'white')
        screen.blit(button_text, (530,260))
        
        time_text = font.render("Time: " + str(elapsed_time) + " seconds", True, 'white')
        screen.blit(time_text, (10, 10))
        
        penalty_text = font.render("penalty number= " + str(Sum), True, 'white')
        screen.blit(penalty_text, (10, 40))
        
        
    clock.tick(100)
    pygame.display.update() 