import random
from os import system,name
from time import sleep
import keyboard


  ##############********#############
##start=0,0                          ##
##end=width-3,height-1               ##
##eg:if w=65,h=25 then end=62,24     ##
  ##############********#############
def food(width,height):
    foodx=(random.random())*width
    foody=(random.random())*height
    return int(foodx),int(foody)       
def move(snake):
    pass
def board(width,height,snakex,snakey,snakelen,sym):
##    global boardx,boardy
##    boardx,boardy=width,height
    for i in range(width):
        print(0,end='')
    print()
    foodx,foody=food(width,height)
##    foodx,foody=62,24
    for i in range(height):
   ##food placement
        print(0,end='')

        j=0
        while(j<width-2):
            







            
                #######main##########
####            if i==0 and j==width//2:        ##test
####                print('2',end='')
####                j+=1
            
            if (i==foody) and (j==foodx):
                print('*',end='')
                j+=1
##            elif (i==snakey) and (j ==snakex):  ##move horizontal
##                for k in range(snakelen):
##                    print(sym,end='')
##                    j+=1
            elif (i in range(snakey,snakey+snakelen)) \
                 and (j==snakex):      ##move vertical
                
                print(sym,end='')
                j+=1
            else:
            ##########################
                print(" ",end='')
                j+=1
        print(0)
    for i in range(width):
        print(0,end='')
    print()
    print(foodx,foody)
##    print(boardx,boardy)
    ##snakeplacement
def snake(l,inc):
    snake=5
    for i in range(l):
        snake+=inc
##    snake='000000000'
    return snake
   
def game(boardx=65,boardy=25):
    snakex,snakey=boardx//2,boardy//2
##    snakex,snakey=62,0
    snakee=snake(0,2)
    if name=='nt':
        system('cls')
    
    while(True and snakex<boardx-snakee and snakey<boardy-snakee):
        if keyboard.is_pressed('w'):
            while(snakee!=0):
                board(boardx,boardy,snakex,snakey,snakee,'@')
                snakee+=2
                sleep(0.6)
                if name=='nt':
                    system('cls')
        else:
            board(boardx,boardy,snakex,snakey,snakee,'@')
            
    ##        snakex+=4
            snakey+=2
            if snakex>boardx-snakee -4:
                snakex=0
            if snakey>boardy-snakee-1:
                snakey=0
            sleep(0.6)
            if name=='nt':
                system('cls')
##

##    for i in range(start[1]):
##        
##    
##    return 0
game()

def appear(x,y,length,sym):
    snake=''
    for i in range(length):
        snake+=sym


def disappear(length,snake,sym):
    for i in range(length):
        snake-=sym



























