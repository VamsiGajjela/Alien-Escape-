import pygame
import time
import random
#Imports different modules specifically pygame,time,random

pygame.init()#intializes/starts up pygame

def menu(): 
    display_width = 800 
    display_height = 600

    
    black = (0,0,0)
    white = (255,255,255)
    red = (200,0,0)
    

    display = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("Alien Escape")
    clock = pygame.time.Clock()
    

    backgroundimg = pygame.image.load('loading.png').convert() 

    def text_objects(text, font):
        textSurface = font.render(text, True, white)
        return textSurface, textSurface.get_rect()
        
    def display_message(message): 
        Largetext = pygame.font.SysFont("comicsansbold", 60)
        TextSurf, TextRect = text_objects(message, Largetext)
        TextRect.center = ((display_width/2), (display_height*0.2))
        display.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(0.1)

    def background_display(x,y): 
        display.blit(backgroundimg, (x,y))

    def game_file():
        game()


    def button(msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(display, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                time.sleep(1)
                if action == "play":
                    game_file()
                    pygame.quit()
                    quit()

                if action == "quit":
                    pygame.quit()
                    quit()
                   
        else:
            pygame.draw.rect(display, ic, (x, y, w, h))

        Smalltext = pygame.font.Font("freesansbold.ttf",15)
        textSurf, textRect = text_objects(msg, Smalltext)
        textRect.center = ((x + (w/2)), (y + (h/2)))
        display.blit(textSurf, textRect)


    def small_text_display(msg, x, y):
        Smalltext = pygame.font.Font("freesansbold.ttf",15)
        textSurf, textRect = text_objects(msg, Smalltext)
        textRect.center = ((x), (y))
        display.blit(textSurf, textRect)

    def high_score_display(msg, highscore, x , y):
        scoretext = pygame.font.SysFont("comicsansms", 25)
        textSurf, textRect = text_objects(msg + highscore, scoretext)
        textRect.center = ((x), (y))
        display.blit(textSurf, textRect)

    def display_message(message,x,y):
        Largetext = pygame.font.SysFont("comicsansbold", 60)
        TextSurf, TextRect = text_objects(message, Largetext)
        TextRect.center = (x, y)
        display.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(0.1)
        
    def game_intro():
        start = True
        while start == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            f=open('highscore.txt','r+')
            highscore=f.read()
            f.close()
            
            background_display(0,0)
            small_text_display("This game was made by Vamsi Gajjela", 400, 560)
            small_text_display("Copyright © VG 2019", 400, 580)
            button('Play',150, 300, 150, 90, black, red,'play')
            button('Quit',500, 300, 150, 90, black, red,'quit')
            high_score_display('Highscore: ',highscore ,375 , 425)
            display_message('Alien Escape', 395, 200 )
            pygame.display.update()
            clock.tick(60)
    game_intro()



def game():
    height=700
    width=500
    display=pygame.display.set_mode((height,width))
    timer=pygame.time.Clock()

    white=(255,255,255)
    blue=(0,0,0)
    grey=(207,207,207)

    playerx = (-110)
    playery = (200)

    floor=0

    player_change_y=0
    player_height=1


    tracker=0

    charcterimg = pygame.image.load('charcter.png')
    background = pygame.image.load('background.png').convert()
    cometimg = pygame.image.load('comet.png')
    cometimg2 = pygame.image.load('comet.png')

    rocketimg = pygame.image.load('rocket.png')
    satimg = pygame.image.load('sat.png')
    pygame.display.set_caption("Alien Escape")


    background_x=0

    cometx=800
    comety=(random.randint(0,410))
    comet_speed=-7
    comet_height1=80

    comet2x=800
    comet2y=(random.randint(0,410))
    comet_speed2=0
    comet_height2=80

    rocketx=800
    rockety=(random.randint(0,410))
    rocket_speed=0
    rocket_height=50

    satx=800
    saty=(random.randint(0,410))
    sat_speed=0
    sat_height=80

    def charcter(x,y):
        display.blit(charcterimg, (x,y))

    def comet(x,y):
        display.blit(cometimg, (x,y))

    def comet2(x,y):
        display.blit(cometimg2, (x,y))
        
    def rocket(x,y):
        display.blit(rocketimg, (x,y))

    def sat(x,y):
        display.blit(satimg, (x,y))

    def scorekeeper(score):
        font = pygame.font.SysFont("comicsansms", 25)
        text=font.render('Score '+str(score),True,white)
        display.blit(text,(550,20))

    def Large_text_display(msg, x, y):

        font = pygame.font.SysFont("comicsansms", 25)
        text=font.render(msg,True,white)
        display.blit(text,(x,y))


    def loadingscreen():
        start = True
        while start == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            display.blit(loading,[0,0])
            f=open('highscore.txt','r')
            highscore1=f.read()
            f.close()
            Large_text_display(('All time highscore: '+str(highscore)),200,500)

            Large_text_display("ALIEN INVASION", 350, 150)
            button("Exit",430, 260, 200, 100, grey, white,"exit")
            button("Play",90, 260, 200, 100, grey, white,"play")
            
            pygame.display.update()
            clock.tick(5)

    def button(msg,x,y,w,h,ic,ac,action=None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                if action == "exit":
                    pygame.quit()
                    quit()
                elif action == 'play':
                    game()

        else:
            pygame.draw.rect(screen, ic, (x, y, w, h))
        
        Smalltext = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, Smalltext)
        textRect.center = ((x + (w/2)), (y + (h/2)))
        screen.blit(textSurf, textRect)

    def crash():
        ending()
            
    start = True
    display.fill(white)
    score=0
    score=0

    f = open("highscore.txt", "r+")
    highscore=f.read()
    f.close()

    while start == True:
        tracker+=1
        
        for incident in pygame.event.get():
            if incident.type==pygame.QUIT:
                start=False

            if incident.type == pygame.KEYDOWN:

                if incident.key == pygame.K_UP:
                    player_change_y = -5

                elif incident.key == pygame.K_DOWN:
                    player_change_y = 5
                  
            if incident.type == pygame.KEYUP:
                if incident.key == pygame.K_UP or incident.key == pygame.K_DOWN:
                    player_change_y = 0
                
        if playery>350:
            playery=350

        playery+=player_change_y 
        
        if playerx<-50:
            playerx=-49

        if playerx>360:
            playerx=359

        if playery<-78:
            playery=-77
     

        replay = background_x % background.get_rect().height
        display.blit(background, (replay-background.get_rect().height,0))
        if replay<height:
            display.blit(background, (replay,0))

        if 1000 < tracker < 2500:
            Large_text_display("Stage: 2", 275, 10)
            background_x-=5
            comet_speed=-3.5
            comet_speed2=-4
        
        elif 2500 < tracker < 5000:
            Large_text_display("Stage: 3", 275, 10)
            comet_speed=-4
            background_x-=6
            rocket_speed=-5
            sat_speed=0
            comet_speed2=-4.5

        elif 5000 < tracker < 7000:
            Large_text_display("Stage: 4", 275, 10)
            background_x-=10
            comet_speed=-1
            rocket_speed=-5
            sat_speed=-1
            comet_speed2=-3

        
        elif 7000 < tracker < 7250:
            Large_text_display(("You got away"), 100, 10)
            background_x-=10
            comet_speed=-1
            rocket_speed=-3
            sat_speed=-4
            comet_speed2=-2


        elif 7250 < tracker < 8000 :          
            Large_text_display(("Beat your highscore"), 100, 10)    
            background_x-=11
            comet_speed=-1
            rocket_speed=-3
            sat_speed=-4
            comet_speed2=-2

        elif tracker > 8000:
            Large_text_display("INSANE MODE!", 275, 10)
            background_x-=14
            comet_speed=-7
            rocket_speed=-9
            sat_speed=-6.5
            comet_speed2=-8


            
        charcter(playerx,playery)
         
        comet(cometx,comety)
        cometx+=comet_speed

        comet2(comet2x,comet2y)
        comet2x+=comet_speed2

        rocket(rocketx,rockety)
        rocketx+=rocket_speed

        sat(satx,saty)
        satx+=sat_speed
        
        if cometx<-75:
            score+=1
            cometx=800
            comety=(random.randint(0,410))
            comet(cometx,comety)

        if comet2x<-75:
            score+=1
            comet2x=800
            comet2y=(random.randint(0,410))
            comet2(comet2x,comet2y)


        if rocketx<-75:
            score+=2
            rocketx=800
            rockety=(random.randint(0,410))
            rocket(rocketx,rockety)

        if satx<-80:
            score+=3
            satx=800
            saty=(random.randint(0,410))
            sat(satx,saty)
            
        if playerx+110>cometx+15:
            if (playery<(comety-95) and playery>(comety-95)+comet_height1) or (playery+player_height>(comety-95) and playery+player_height<(comety-95)+comet_height1):
                if score>int(highscore):
                    f=open('highscore.txt','w')
                    f.write(str(score))
                    f.close()
                crash()
                start=False

        if playerx+110>comet2x+15:
            if (playery<(comet2y-95) and playery>(comet2y-95)+comet_height2) or (playery+player_height>(comet2y-95) and playery+player_height<(comet2y-95)+comet_height2):
                if score>int(highscore):
                    f=open('highscore.txt','w')
                    f.write(str(score))
                    f.close()
                crash()
                start=False
                
        if playerx+110>rocketx-30:
            if (playery<(rockety-50) and playery>(rockety-50)+rocket_height) or (playery+player_height>(rockety-50) and playery+player_height<(rockety-50)+rocket_height):
                if score>int(highscore):
                    f=open('highscore.txt','w')
                    f.write(str(score))
                    f.close()
                crash()
                start=False

        if playerx+110>satx+50:
            if (playery<(saty-50) and playery>(saty-60)+sat_height) or (playery+player_height>(saty-60) and playery+player_height<(saty-60)+sat_height):
                if score>int(highscore):
                    f=open('highscore.txt','w')
                    f.write(str(score))
                    f.close()
                crash()
                start=False

        scorekeeper(score)
        pygame.display.update() 
        timer.tick(120)

    pygame.quit()






def ending():
    display_width = 800
    display_height = 600

    black = (0,0,0)
    white = (255,255,255)
    red = (200,0,0)



    display = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("Alien Escape")
    clock = pygame.time.Clock()


    backgroundimg = pygame.image.load('loading.png').convert()

    def text_objects(text, font):
        textSurface = font.render(text, True, white)
        return textSurface, textSurface.get_rect()
        
    def display_message(message):
        Largetext = pygame.font.SysFont("comicsansbold", 60)
        TextSurf, TextRect = text_objects(message, Largetext)
        TextRect.center = ((display_width/2), (display_height*0.2))
        display.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(0.1)

    def background_display(x,y):
        display.blit(backgroundimg, (x,y))

    def game_file():
        game()

    def button(msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(display, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                time.sleep(1)
                if action == "play":
                    game_file()
                    pygame.quit()
                    quit()

                if action == "quit":
                    pygame.quit()
                    quit()
                if action == "menu":
                    main_menu()
                    pygame.quit()
                    quit()                   
                   
        else:
            pygame.draw.rect(display, ic, (x, y, w, h))

        Smalltext = pygame.font.Font("freesansbold.ttf",15)
        textSurf, textRect = text_objects(msg, Smalltext)
        textRect.center = ((x + (w/2)), (y + (h/2)))
        display.blit(textSurf, textRect)


    def background_display(x,y):
       display.blit(backgroundimg, (x,y))

    def button(msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(display, ac, (x, y, w, h))
            if click[0] == 1 and action != None:
                time.sleep(1)
                if action == "play":
                    game_file()
                    pygame.quit()
                    quit()

                if action == "quit":
                    pygame.quit()
                    quit()
                if action == "menu":
                    main_menu()
                    pygame.quit()
                    quit()
                   
                   
        else:
            pygame.draw.rect(display, ic, (x, y, w, h))

        Smalltext = pygame.font.Font("freesansbold.ttf",15)
        textSurf, textRect = text_objects(msg, Smalltext)
        textRect.center = ((x + (w/2)), (y + (h/2)))
        display.blit(textSurf, textRect)


    def small_text_display(msg, x, y):
        Smalltext = pygame.font.Font("freesansbold.ttf",15)
        textSurf, textRect = text_objects(msg, Smalltext)
        textRect.center = ((x), (y))
        display.blit(textSurf, textRect)

    def high_score_display(msg, highscore, x , y):
        scoretext = pygame.font.SysFont("comicsansms", 25)
        textSurf, textRect = text_objects(msg + highscore, scoretext)
        textRect.center = ((x), (y))
        display.blit(textSurf, textRect)

    def display_message(message,x,y):
        Largetext = pygame.font.SysFont("comicsansbold", 60)
        TextSurf, TextRect = text_objects(message, Largetext)
        TextRect.center = (x, y)
        display.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(0.1)
        
    def game_intro():
        start = True
        while start == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            f=open('highscore.txt','r+')
            highscore=f.read()
            f.close()   
            background_display(0,0)
            small_text_display("This game was made by Vamsi Gajjela", 400, 560)
            small_text_display("Copyright © VG 2019", 400, 580)
            button('Try again',150, 200, 150, 90, black, red,'play')
            button('Quit',500, 200, 150, 90, black, red,'quit')
            button('Menu',320, 335, 150, 90, black, red,'menu')

            
            high_score_display('Highscore: ',highscore ,390 , 470)
            display_message('Alien Escape', 435, 100 )
            pygame.display.update()
            clock.tick(60)
    def main_menu():
        menu()
    game_intro()

while True:
    menu()
    
