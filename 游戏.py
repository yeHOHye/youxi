# -*- coding: utf8 -*-
background_image_filename = 'tupian2.jpg'
BEGIN_image_filename='jinzi.jpg'
choice='beijing.png'
An_a='a.jpg'
An_b='b.jpg'
An_c='c.jpg'
An_d='d.jpg'
An_e='e.jpg'
An_f='f.jpg'
An_g='g.jpg'
import pygame
from pygame.locals import *
from sys import exit
import random

def winner(player_point):
    if player_point is not None:
        if 1 in player_point and  2 in player_point and  3 in player_point :

            return True
        elif  1 in player_point and  4 in player_point and  5 in player_point :

            return True
        elif  3 in player_point and  8 in player_point and  9 in player_point :

            return True
        elif  5 in player_point and  7 in player_point and  8 in player_point :

            return True

        elif  2 in player_point and  6 in player_point and  7 in player_point :

            return True
        elif  4 in player_point and  6 in player_point and  9 in player_point :

            return True
        elif  1 in player_point and  6 in player_point and  8 in player_point :

            return True
        elif  3 in player_point and  6 in player_point and  5 in player_point :

            return True
        else:
            return False
def AI_move(step,chess_piece_lock,encode,encode_2,winner_way):
    surplus=set(step).difference(encode)
    AI = []
    AI_lock=0
    ai_walk_2_1=[]
    if chess_piece_lock%2==0:
        if len(surplus)>0:
            for i in range(8):
                AI_winner_way = list(set(winner_way[i]).difference(encode_2))
                AI.append(AI_winner_way)
            for j in range(len(AI)):
                if len(AI[j])==1 :
                    a=len(list(set(AI[j]).difference(encode)))
                    if  not a<1:
                        ai_walk_2_1 = (AI[j])
                        AI_lock=1
                        break

            if AI_lock==1:
                ai_walk_2=ai_walk_2_1
                return ai_walk_2
            else:
                ai_walk_1 = random.sample(surplus, 1)
                return ai_walk_1
    return False

pygame.init()
screen = pygame.display.set_mode((600, 600), 0, 32)
pygame.font.init()
background_choice=pygame.image.load(choice)
my_font = pygame.font.SysFont('arial',48)
text = my_font.render("Tic-tac-toe",True,(0,0,0),(255,255,255))
Begin = my_font.render("Begin",True,(0,0,0),(255,255,255))
Tryagain = my_font.render("Try again",True,(0,0,0),(255,255,255))
draw = my_font.render("draw",True,(0,0,0),(255,255,255))

w_2,h_2=Tryagain.get_size()
An_a_image=pygame.image.load(An_a).convert
An_b_image=pygame.image.load(An_b).convert
An_c_image=pygame.image.load(An_c).convert
An_d_image=pygame.image.load(An_d).convert
An_e_image=pygame.image.load(An_e).convert
An_f_image=pygame.image.load(An_f).convert
An_g_image=pygame.image.load(An_g).convert
jinzi = pygame.image.load(BEGIN_image_filename).convert()
background = pygame.image.load(background_image_filename).convert()
Fullscreen = False
w,h=background.get_size()
x_1=-100
y_1=-100
x_2=-100
y_2=-100
chess_piece_lock=1
x=-100
y=-100
encode_1=[]
encode_2=[]
lock=0
process=1
encode=[]
lu=0
AI_step=[1,2,3,4,5,6,7,8,9]
delay=1
winner_way=[[1,2,3],[1,4,5],[3,8,9],[5,7,8],[2,6,7],[4,6,9],[1,6,8],[3,6,5]]
chess_picture = []
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if process==2:
            AI_WALK=AI_move(AI_step,chess_piece_lock,encode,encode_2,winner_way)
            if event.type == MOUSEBUTTONDOWN or chess_piece_lock%2==0:
                    point_x,point_y=pygame.mouse.get_pos()
                    if(((0<point_x<200) and (0<point_y<200) ) or AI_WALK==[1]) and 1 not in encode :
                            x=50
                            y=50
                            lu=1
                            chess_piece_lock=chess_piece_lock+1
                    elif (((200<point_x<400) and (0<point_y<200))  or AI_WALK==[2]) and 2 not in encode:
                            x=250
                            y=50
                            lu=2
                            chess_piece_lock=chess_piece_lock+1
                    elif (((400<point_x<600) and (0<point_y<200))  or AI_WALK==[3]) and 3 not in encode:
                            x=450
                            y=50
                            lu=3
                            chess_piece_lock=chess_piece_lock+1
                    elif( ((0<point_x<200) and (200<point_y<400) ) or AI_WALK==[4]) and 4 not in encode:
                            x=50
                            y=250
                            lu=4
                            chess_piece_lock=chess_piece_lock+1
                    elif (((0<point_x<200) and (400<point_y<600)) or AI_WALK==[5]) and 5 not in encode:
                            x=50
                            y=450
                            lu=5
                            chess_piece_lock=chess_piece_lock+1
                    elif (((200<point_x<400) and (200<point_y<400))  or AI_WALK==[6]) and 6 not in encode:
                            x=250
                            y=250
                            lu=6
                            chess_piece_lock=chess_piece_lock+1
                    elif (((200<point_x<400) and (400<point_y<600)) or AI_WALK==[7]) and 7 not in encode:
                            x=250
                            y=450
                            lu=7
                            chess_piece_lock=chess_piece_lock+1
                    elif (((400<point_x<600) and (400<point_y<600)) or AI_WALK==[8]) and 8 not in encode:
                            x=450
                            y=450
                            lu=8
                            chess_piece_lock=chess_piece_lock+1
                    elif (((400<point_x<600) and (200<point_y<400)) or AI_WALK==[9]) and 9 not in encode:
                            x=450
                            y=250
                            lu=9
                            chess_piece_lock=chess_piece_lock+1


            if chess_piece_lock%2 == 1:
                x_1=x
                y_1=y
                encode_1.append(lu)
            else:
                x_2=x
                y_2=y
                encode_2.append(lu)
            encode=encode_1+encode_2
    if process==1:
        screen.blit(jinzi,(0,0))
        screen.blit(text,(220,100))
        screen.blit(Begin,(250,350))
        encode=[]
        x_1=-100
        y_1=-100
        x_2=-100
        y_2=-100
        chess_piece_lock=1
        x=-100
        y=-100
        encode_1=[]
        encode_2=[]
        delay=1
        lu=0
        lock=0
        AI_step=[1,2,3,4,5,6,7,8,9]
        w_1,h_1=Begin.get_size()
        chess_picture = ['a.jpg', 'b.jpg', 'd.jpg', 'e.jpg', 'f.jpg', 'g.jpg']
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                point_x,point_y=pygame.mouse.get_pos()
                chess_piece_image_filename = chess_picture[(random.randrange(len(chess_picture)))]
                chess_picture.remove(chess_piece_image_filename)
                black_chess_piece_image_filename = chess_picture[(random.randrange(len(chess_picture)))]
                chess_piece = pygame.image.load(chess_piece_image_filename).convert()
                black_chess_piece = pygame.image.load(black_chess_piece_image_filename).convert()
                if (250<point_x<250+w_1) and (350<point_y<350+h_1) :
                    screen.blit(background, (0, 0))
                    process=2
    if process==2:
        screen.blit(chess_piece,(x_1,y_1))
        screen.blit(black_chess_piece,(x_2,y_2))

        pygame.display.update()
    if winner(encode_1):
            if(delay==1):
                pygame.time.delay(800)
                delay=2
            process=3

            screen.blit(jinzi,(0,0))
            screen.blit(Tryagain,(180,300))
            winner_1 = my_font.render("AI IS WINNER",True,(0,0,0),(255,255,255))
            screen.blit(winner_1,(100,100))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    point_x,point_y=pygame.mouse.get_pos()
                    if (180<point_x<180+w_2) and (300<point_y<300+h_2) :
                        process=1
    elif winner(encode_2):
                if(delay==1):
                    pygame.time.delay(800)
                    delay=2
                process=3

                screen.blit(jinzi,(0,0))
                screen.blit(Tryagain,(180,300))
                winner_2 = my_font.render("player is winner",True,(0,0,0),(255,255,255))
                screen.blit(winner_2,(100,100))
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        point_x,point_y=pygame.mouse.get_pos()
                        if (180<point_x<180+w_2) and (300<point_y<300+h_2) :
                            process=1
    elif len(set(encode))==10:

            if(delay==1):
                    pygame.time.delay(800)
                    delay=2
            process=3
            screen.blit(jinzi,(0,0))
            screen.blit(Tryagain,(180,300))
            screen.blit(draw,(200,100))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    point_x,point_y=pygame.mouse.get_pos()
                    if (180<point_x<180+w_2) and (300<point_y<300+h_2) :
                        process=1
    pygame.display.update()