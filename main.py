import time
import ai
import pygame
import sys
import evalute
import numpy as np
from pygame.locals import *


pygame.init()
board = np.zeros((3,3))
chance = 0
size =  400, 400
screen = pygame.display.set_mode(size)

pygame.display.set_caption("TicTacToe")
Game_Sprite ={}
o1 = pygame.image.load('img/o.png').convert_alpha()
x1 = pygame.image.load("img/x.png").convert_alpha()
Game_Sprite['o'] =  pygame.transform.scale(o1, (100,123))
Game_Sprite['x'] =  pygame.transform.scale(x1, (100,123))

bd = pygame.image.load('img/board.png').convert_alpha()
bd = pygame.transform.scale(bd,(400,400))
screen.blit(bd,(0, 0))
pygame.display.update()
def position():
    x, y =  pygame.mouse.get_pos()
    if (x < 133) and (y < 133 ):                                
        position = 17,0 
    elif (x > 133 and x < 266) and (y < 133 ):                  
        position = 150,0 
    elif (x > 266 and x < 399) and (y < 133 ):                  
        position = 285,0 
    elif (x < 133) and (y > 133 and y < 266):                    
        position = 17,140
    elif (x > 133 and x < 266) and (y > 133 and y < 266):       
        position = 150,140
    elif (x > 266 and x < 400) and (y > 133 and y < 266):        
        position = 285,140
    elif (x < 133) and (y > 266 and y < 400):                   
        position = 17,280
    elif (x > 133 and x < 266) and (y > 266 and y < 400):       
        position = 150,280
    elif (x > 266 and x < 400) and (y > 266 and y < 400):       
        position =  285,280  
    return position 


def mark_sqr(pos):
    if pos == (17,0):
        rows = 0
        col = 0
    elif pos == (150,0):
        rows = 0
        col = 1
    elif pos == (285,0):
        rows = 0
        col = 2
    elif pos == (17,140):
        rows = 1
        col = 0
    elif pos == (150,140):
        rows = 1
        col = 1
    elif pos == (285,140):
        rows = 1
        col = 2
    elif pos == (17,280):
        rows = 2
        col = 0
    elif pos == (150,280):
        rows = 2
        col = 1
    elif pos == (285,280):
        rows = 2
        col = 2
    return rows,col

def opp_mark_sqr(data):
    if data == (0,0):
        pos= (17,0)
    elif data == (0,1):
        pos = (150,0)
    elif data == (0,2) :
        pos = (285,0)
    elif data == (1,0):
        pos =(17,140)
    elif data == (1,1):
       pos =(150,140)
    elif data == (1,2):
        pos = (285,140)
    elif data == (2,0):
        pos =(17,280)
    elif data == (2,1):
        pos = (150,280)
    elif data == (2,2):
        pos =(285,280)
    return pos



    
def main():
    global chance
    player_1 = Game_Sprite['x']   
    player_2 = Game_Sprite['o'] 
    with open("moves.txt", "w")as f:
        f.write("")
        while(chance < 9):
            play = evalute.whosChance(player_1 ,player_2,chance)
            if play == player_1:
                play3 = 1
            elif play == player_2:
                play3 = 2
            AI = ai.AI_Module(board,1,2)
            if play == player_1:
                pass
            elif play == player_2:
                with open("moves.txt","r") as f:
                    move =AI.eval()
                    pos2 = opp_mark_sqr(move)
                    a = f.readlines()
                    d = a.count(f"{pos2}\n")
                    if d > 0:break
                    else:
                        with open("moves.txt", "a")as f:
                            f.write(f"{pos2}\n")
                        rows,col=mark_sqr(pos2)
                        screen.blit(play , pos2)
                        board[rows][col] = play3
                        pygame.display.update()
                        chance += 1
                        won2 =evalute.checkWin(board)
                if won2 == 1:
                    print(f"x is the winner") 
                    time.sleep(2)
                    sys.exit()
                elif won2 == 2:
                        print(f"o is the winner") 
                        time.sleep(2)
                        sys.exit()
                elif won2 == 0:
                    print(f"Next chance : o ")    

            for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        while(True):
                            pos = position()
                            if play == player_1:
                                play5 = 1
                            elif play == player_2:
                                play5 = 2
                            with open("moves.txt","r") as f:
                                a = f.readlines()
                                d = a.count(f"{pos}\n")
                                if d > 0:break
                                else:
                                    with open("moves.txt", "a")as f:
                                        f.write(f"{pos}\n")
                                    rows,col=mark_sqr(pos)
                                    screen.blit(play , pos)
                                    board[rows][col] = play5
                                    pygame.display.update()
                                    chance += 1
                                    won =evalute.checkWin(board)
                                    
                                    if won == 1:
                                        print(f"x is the winner") 
                                        time.sleep(2)
                                        sys.exit()
                                    elif won == 2:
                                         print(f"o is the winner") 
                                         time.sleep(2)
                                         sys.exit()
                                    elif won == 0:
                                        print(f"Next chance : x ")    
                                        time.sleep(0.5)

                                        break

                                        
                        
                    
                    elif event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        sys.exit()

if __name__ == "__main__":
    main()
