
import pygame
pygame.init()

win = pygame.display.set_mode((500,430))
screen='game'

pygame.display.set_caption("DBZ 1vs1")


#PLAYER 1 animations

walkRight = [pygame.image.load('right.png'), pygame.image.load('right2.png')]
walkLeft = [pygame.image.load('left.png'), pygame.image.load('left2.png')]
stand = pygame.image.load('right.png')


bg = pygame.image.load('bg.jpg')
p2w=pygame.image.load('FINISH (1).png')
p1w=pygame.image.load('FINISH.png')
kisound=pygame.mixer.Sound('Fireball+1.wav')
kisound2=pygame.mixer.Sound('Fireball+3.wav')


font1 = pygame.font.SysFont('comicsans', 100)
font2 = pygame.font.SysFont('comicsans', 100)


clock = pygame.time.Clock()

#LOADING AND PLAYING THE MUSIC ON LOOP

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)


class player(object):
    def __init__(self,x,y,width,height):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.Jump = False
        self.left = False
        self.right = False
        self.jumpCount = 10
        self.standing = True
        self.hitbox=(self.x,self.y,29,40)
        self.health=10
        self.score=0
        
        
        
        

    def draw(self, win):

        if not(self.standing):    
            
            if self.left:
                win.blit(walkLeft[1], (self.x,self.y))     
            elif self.right:
                win.blit(walkRight[1], (self.x,self.y))          
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
               
            elif self.left:
                win.blit(walkLeft[0], (self.x, self.y))
           
            else:
                win.blit(stand,(self.x,self.y))
        pygame.draw.rect(win, (255,0,0), (self.hitbox[0]-10, self.hitbox[1] - 20, 50, 10))
        pygame.draw.rect(win, (0,128,0), (self.hitbox[0]-10, self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))        
        self.hitbox = (self.x , self.y , 29, 45)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        if self.health>0:
            self.health-=0.5
        else:
            man2.score2+=1
            self.x=50
            man2.x2=400
            man2.health2=10
            self.health=10

        
#PLAYER 2 animations

                
walkR2=[pygame.image.load('VR1.png'),pygame.image.load('VR2.png')]
walkL2=[pygame.image.load('VL1.png'),pygame.image.load('VL2.png')]

class player2(object):
    def __init__(self,x2,y2,width2,height2):
        self.x2 = x2
        self.y2 = y2
        self.width2 = width2
        self.height2 = height2
        self.vel2 = 5
        self.Jump2 = False
        self.left2 = False
        self.right2 = False
        self.jumpCount2 = 10
        self.standing2 = True
        self.hitbox2 = (self.x2 , self.y2 , 29, 42)
        self.health2=10
        self.score2=0
        
               
        
    def draw(self, win):


        if not(self.standing2):    
            
            if self.left2:
                win.blit(walkL2[1], (self.x2,self.y2))
                 
            elif self.right2:
                win.blit(walkR2[1], (self.x2,self.y2))
               
        else:
            if self.right2:
                win.blit(walkR2[0], (self.x2, self.y2))
            else:
                win.blit(walkL2[0], (self.x2, self.y2))
        pygame.draw.rect(win, (255,0,0), (self.hitbox2[0]-10, self.hitbox2[1] - 20,50, 10))
        pygame.draw.rect(win, (0,128,0), (self.hitbox2[0]-10, self.hitbox2[1] - 20, 50 - (5 * (10- self.health2)), 10))
        self.hitbox2 = (self.x2 , self.y2 , 29, 42)
        #pygame.draw.rect(win, (255,0,0), self.hitbox2,2)        
    def hit2(self):
        if self.health2>0:
            self.health2-=0.5
        else:
            man.score+=1
            man.x=50
            self.x2=400
            man.health=10
            self.health2=10


          
    
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x-11
        self.y = y+6
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 10*facing # speed of the bullets

    def draw(self,win):
        
        
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

class projectile2(object):
    def __init__(self,x2,y2,color2,radius2,facing2):
        self.x2 = x2
        self.y2 = y2
        self.radius2 = radius2
        self.color2 = color2
        self.facing2 = facing2
        self.vel2 = 10* facing2 #speed of the bullets

    def draw2(self,win):
        pygame.draw.circle(win,self.color2,(self.x2,self.y2), self.radius2)

    

    
def redrawGameWindow():
    win.blit(bg, (0,0))
    man2.draw(win)
    man.draw(win)
    text = font1.render(str(man.score), 10, (255,0,0))
    win.blit(text, (10, 10))
    text2 = font2.render(str(man2.score2), 10, (255,0,0))
    win.blit(text2, (445, 10))

    for bullet in bullets:
        bullet.draw(win)
        
    for bullet2 in bullets2:
        bullet2.draw2(win)
        
    
    pygame.display.update()


# MAINLOOP
man = player(50, 380, 64,64)
man2 = player2(400,380,64,64)

bullets = []
bullets2=[]
run = True
while run:
    if screen=='game':
        clock.tick(27)
        if man.hitbox[1] < man2.hitbox2[1] + man2.hitbox2[3] and man.hitbox[1] + man.hitbox[3] > man2.hitbox2[1]:
            if man.hitbox[0] + man.hitbox[2] > man2.hitbox2[0] and man.hitbox[0] < man2.hitbox2[0] + man2.hitbox2[2]:
                if man.health>0:
                    man.health-=1
                if man.health>0:
                    man2.health2-=1
                man.x=50
                man2.x2=400
                


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        for bullet in bullets:
            if bullet.y - bullet.radius < man2.hitbox2[1] + man2.hitbox2[3] and bullet.y + bullet.radius > man2.hitbox2[1]:
                if bullet.x + bullet.radius > man2.hitbox2[0] and bullet.x - bullet.radius < man2.hitbox2[0] + man2.hitbox2[2]:
                    bullets.pop(bullets.index(bullet))
                    man2.hit2()
            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
            
        elif keys[pygame.K_d] and man.x < 530 - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
            
        else:
            man.standing = True
            
        if not(man.Jump):
            if keys[pygame.K_w]:
                man.Jump = True
                man.right = False
                man.left = False
              
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount < 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.60 * neg
                man.jumpCount -= 1
            else:
                man.Jump = False
                man.jumpCount = 10
        
        if keys[pygame.K_q]:
            kisound.play()
            
            if man.left:
                facing = -1
            else:
                facing = 1
                
            if len(bullets) < 5:
                bullets.append(projectile(round(man.x + man.width //3), round(man.y + man.height//3), 6, (0,250,250), facing))    
            
                
                
    #PLAYER 2////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

                
        for bullet2 in bullets2:
            if bullet2.y2 - bullet2.radius2 < man.hitbox[1] + man.hitbox[3] and bullet2.y2 + bullet2.radius2 > man.hitbox[1]:
                if bullet2.x2+ bullet2.radius2 > man.hitbox[0] and bullet2.x2 - bullet2.radius2 < man.hitbox[0] + man.hitbox[2]:
                    bullets2.pop(bullets2.index(bullet2))
                    man.hit()
            
            if bullet2.x2 < 500 and bullet2.x2 > 0:
                bullet2.x2 += bullet2.vel2
            else:
                bullets2.pop(bullets2.index(bullet2))
                
        if keys[pygame.K_DOWN]:
                kisound2.play()
                if man2.left2:
                    facing2 = -1
                else:
                    facing2 = 1
                    
                if len(bullets2) < 5:
                    bullets2.append(projectile2(round(man2.x2 + man2.width2 //3), round(man2.y2 + man2.height2//3),(154,50,205), 6, facing2))
                    


                    
        if keys[pygame.K_LEFT] and man2.x2 > man2.vel2:
            man2.x2 -= man2.vel2
            man2.left2 = True
            man2.right2 = False
            man2.standing2 = False
            
            

        elif keys[pygame.K_RIGHT] and man2.x2 < 530 - man2.width2 - man2.vel2:
            man2.x2 += man2.vel2
            man2.right2 = True
            man2.left2 = False
            man2.standing2 = False
            
        else:
            man2.standing2 = True
            
            
            
        if not(man2.Jump2):
            
            if keys[pygame.K_UP]:
                man2.Jump2 = True
                man2.right2 = False
                man2.left2 = False
               
        else:
            if man2.jumpCount2 >= -10:
                neg2 = 1
                if man2.jumpCount2 < 0:
                    neg2 = -1
                man2.y2 -= (man2.jumpCount2 ** 2) * 0.60 * neg2
                man2.jumpCount2 -= 1
                
            else:
                man2.Jump2 = False
                man2.jumpCount2 = 10

            
        if man.score==3 or man2.score2==3:
            screen='end'
        redrawGameWindow()

    elif screen=='end':
        if man.score==3:
            win.blit(p1w,(0,0))
        else:
            win.blit(p2w,(0,0))

        pygame.display.update()
        
pygame.quit()

