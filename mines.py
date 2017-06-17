#This is mines
import sys
import pygame

from random import *
from pygame.locals import *

FPS = 30

width = 30
height = 16
mines = 99

num_squares = width * height #width x height

if mines > num_squares - 5:
    mines = num_squares - 5

window_width = 1230
window_height = 800
#1230, 800
box_size = 20

gray0 = (240, 240, 240)
gray1 = (215, 215, 215)
gray2 = (180, 180, 180)
white = (255,255,255)
over = (180, 180, 180)
clicked_color = (100,100,100)
green = (0, 200, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
dark_blue = (0, 0, 100)
maroon = (128,0,0)
teal = (0, 128, 128)
black = (0, 0, 0)
light_gray = (180, 180, 180)
yellow = (255, 255, 0)


color_list = [gray1, blue, green, red, dark_blue, maroon, teal, yellow, light_gray, gray2, black, red, red]
def negative():
    thing = [[255-i[a] for a in range(len(i))] for i in color_list] 
    for i in range(len(color_list)):
        color_list[i] = (thing[i][0], thing[i][1], thing[i][2])
        



def set_mines(mines, num_squares):
    squares = []
    for item in range(num_squares):
        squares.append(False)
    while mines > 0:
        index = randint(0, num_squares-1)
        if squares[index] == False:
            squares[index] = True
            mines -= 1
    return squares
    
squares = set_mines(mines, num_squares)

def set_rows_cols(squares, width, height):
    new_list = []
    for item in range(width):
        new_list.append([])
        for a in range(height):
            index = item * height
            index += a
            new_list[item].append(squares[index])
    return new_list
    

        
def print_list(thing):
    for item in range(len(thing)):
        print thing[item]
        
box_size = 40
xMargin = (window_width - (box_size * width)) / 2
yMargin = 60
        
def draw_board(width, height, window_width, window_height, revealed, thing):
    
    pygame.draw.rect(DISPLAYSURF, black , (xMargin-1, yMargin-1, window_width - 2 * xMargin + 1, box_size * height + 1))
    totalx = xMargin
    for item in range(width):
        if item != 0:
            totalx += box_size
        totaly = yMargin
        for a in range(height):
            if a != 0:
                totaly += box_size
            check = revealed[item][a][1]
            #pygame.draw.rect(DISPLAYSURF, color_list[check], (totalx, totaly, box_size-1, box_size-1))
            #pygame.draw.polygon(DISPLAYSURF, color0, ((totalx - 2, totaly -2), (totalx, totaly), (totalx + box_width - 2, totaly), (totalx + box_width, totaly - 2)))
            width4 = box_size / 4
            width2 = box_size / 2
            height8 = box_size / 8
            height83 = 3 * height8
            height85 = 5 * height8
            height87 = 7 * height8
            width43 = 3 * width4
            color = color_list[check]
            if check == 0:
                pygame.draw.rect(DISPLAYSURF, color, (totalx, totaly, box_size-1, box_size-1))
            elif check == 10:
                pygame.draw.rect(DISPLAYSURF, color_list[9], (totalx, totaly, box_size-1, box_size-1))
                pygame.draw.circle(DISPLAYSURF, black, (totalx+20, totaly+20), 10, 0)
                pygame.draw.polygon(DISPLAYSURF, black, ((totalx+5, totaly+9), (totalx+9, totaly+5), (totalx+35, totaly+31), (totalx+31, totaly+35)))
                pygame.draw.polygon(DISPLAYSURF, black, ((totalx+5, totaly+31), (totalx+9, totaly+35), (totalx+35, totaly+9), (totalx+31, totaly+5)))
                pygame.draw.rect(DISPLAYSURF, black, (totalx+2, totaly+17, 36, 6))
                pygame.draw.rect(DISPLAYSURF, black, (totalx+17, totaly+2, 6, 36))
                
            elif check == 11:
                pygame.draw.rect(DISPLAYSURF, color_list[0], (totalx, totaly, box_size-1, box_size-1))
                
                pygame.draw.rect(DISPLAYSURF, black, (totalx+18, totaly+6, 4, 21))
                pygame.draw.polygon(DISPLAYSURF, color, ((totalx+21, totaly+4), (totalx+9, totaly+10), (totalx+21, totaly+16)))
                pygame.draw.rect(DISPLAYSURF, black, (totalx+10, totaly+27, 20, 3))
            
            elif check == 9:
            	pygame.draw.rect(DISPLAYSURF, color, (totalx, totaly, box_size-1, box_size-1))
            	
            elif check == 1:
                pygame.draw.rect(DISPLAYSURF, color_list[9], (totalx, totaly, box_size-1, box_size-1))
                pygame.draw.polygon(DISPLAYSURF, color, ((totalx + width4+1, totaly + height83), (totalx+1 + width2 , totaly + height8), (totalx+1 + width2, totaly + height83)))
                pygame.draw.rect(DISPLAYSURF, color, (totalx + 3 * width4 / 2 + 1, totaly + height83, width4 / 2 + 1, height83))
                pygame.draw.rect(DISPLAYSURF, color, (totalx + width4 + 1, totaly + height85+1, height83+2, height8))
                
            elif check == 2:
                pygame.draw.rect(DISPLAYSURF, color_list[9], (totalx, totaly, box_size-1, box_size-1))
                pygame.draw.polygon(DISPLAYSURF, color, ((totalx + width4, totaly + width4), (totalx + height83, totaly + height8), (totalx + height83, totaly + width4)))
                pygame.draw.rect(DISPLAYSURF, color, (totalx + height83, totaly + height8, width4, height8 - 1))
                pygame.draw.polygon(DISPLAYSURF, color, ((totalx + height85-1, totaly + height8), (totalx + height85-1, totaly + width4), (totalx + width43-1, totaly + width4)))
                pygame.draw.rect(DISPLAYSURF, color, (totalx + height85-1, totaly + width4, height8+1, height8))
                pygame.draw.polygon(DISPLAYSURF, color, ((totalx + height85-1, totaly + height83), (totalx + width43-1, totaly + height83), (totalx + height83, totaly + width43), (totalx + width4, totaly + width43)))
                pygame.draw.rect(DISPLAYSURF, color, (totalx + height83, totaly + height85+1, height83, height8))
                
            elif check == 3:
                pygame.draw.rect(DISPLAYSURF, color_list[9], (totalx, totaly, box_size-1, box_size-1))
                pygame.draw.rect(DISPLAYSURF, color, (totalx + width4, totaly + height8, height83, height8))
                pygame.draw.polygon(DISPLAYSURF, color, ((totalx + height85, totaly + height8), (totalx + height85, totaly + width4), (totalx + width43, totaly + width4)))
                pygame.draw.rect(DISPLAYSURF, color, (totalx + height85, totaly + width4, height8+1, height85 - 10))
                pygame.draw.rect(DISPLAYSURF, color, (totalx + width4, totaly + width2 - 5, width2, height8))
                pygame.draw.polygon(DISPLAYSURF, color, ((totalx + height85, totaly + height87 - 10), (totalx + height85, totaly + height87 - 5), (totalx + width43, totaly + height87 - 10)))
                pygame.draw.rect(DISPLAYSURF, color, (totalx + width4, totaly + height87 - 10, height83, height8+1))
            elif check == 4:
                pygame.draw.rect(DISPLAYSURF, color_list[9], (totalx, totaly, box_size-1, box_size-1))
                pygame.draw.rect(DISPLAYSURF, color, (totalx + width4, totaly + height8, height8, height83))
                pygame.draw.rect(DISPLAYSURF, color, (totalx + width4, totaly + height83, height85, height8))
                pygame.draw.rect(DISPLAYSURF, color, (totalx + height85, totaly + height8, height8, height85))
                
            elif check == 5:
                pygame.draw.rect(DISPLAYSURF, color_list[9], (totalx, totaly, box_size-1, box_size-1))
            	pygame.draw.rect(DISPLAYSURF, color, (totalx + width4, totaly + height8, width2, height8))
            	pygame.draw.rect(DISPLAYSURF, color, (totalx + width4, totaly + width4, height8, width4))
            	pygame.draw.rect(DISPLAYSURF, color, (totalx + width4, totaly + height83, height83, height8))
            	pygame.draw.polygon(DISPLAYSURF, color, ((totalx + height85, totaly + height83 + 1), (totalx + height85, totaly + width2), (totalx + width43 - 1, totaly + width2)))
            	pygame.draw.rect(DISPLAYSURF, color, (totalx + height85, totaly + width2, height8, height8))
            	pygame.draw.polygon(DISPLAYSURF, color, ((totalx + height85, totaly + height85), (totalx + height85, totaly + width43), (totalx + width43 - 1, totaly + height85)))
            	pygame.draw.rect(DISPLAYSURF, color, (totalx + width4, totaly + height85 + 1, height83, height8))
            	
            	"""elif check == 6:
                pygame.draw.rect(DISPLAYSURF, color_list[9], (totalx, totaly, box_size-1, box_size-1))
                pygame.draw.rect(DISPLAYSURF, color_list[9], (totalx + width4, totaly + height8, width2, height8))
                pygame.draw.rect(DISPLAYSURF, """
            	
           	
           		
           		
            elif check == 12:
                pygame.draw.rect(DISPLAYSURF, color_list[9], (totalx, totaly, box_size-1, box_size-1))
                pygame.draw.polygon(DISPLAYSURF, color, ((totalx, totaly+8), (totalx+8, totaly), (totalx+39, totaly+31), (totalx+31, totaly+39)))
                pygame.draw.polygon(DISPLAYSURF, color, ((totalx, totaly+31), (totalx+8, totaly+39), (totalx+39, totaly+8), (totalx+31, totaly)))
           		
            
               
"""def draw_nums(width, height, window_width, window_height, revealed, check):
    if check == 0:"""
            
def draw_mined_board(width, height, window_width, window_height, board, thing):

    totalx = 15
    for item in range(width):
        if item != 0:
            totalx += box_size
        totaly = yMargin
        for a in range(height):
            
            if a != 0:
                totaly += box_size
            index = board[item][a]
            pygame.draw.rect(DISPLAYSURF, color_list[index], (totalx, totaly, box_size-1, box_size-1))
            
    
            
def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, over, (left, top, box_size-1, box_size-1))
    
    
    
    
    
def generateRevealedBoxesData(val):
    new = []
    revealedBoxes = []
    new = [False for i in range(height)]
    for i in range(width):
        revealedBoxes.append(new)
    #print revealedBoxes
    return revealedBoxes


    
def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (box_size) + xMargin
    top = boxy * (box_size) + yMargin
    return (left, top)


def getBoxAtPixel(x, y):
    for boxx in range(width):
        for boxy in range(height):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, box_size, box_size)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)
       
       

  

def board_numbers(board):
    x = len(board)-1
    y = len(board[0])-1
    new_list = []
    for item in range(len(board)):
        new_list.append([])
        for i in range(height):
            new_list[item].append([])
    for i in range(len(board)):
        for a in range(len(board[0])):
            total = 0
            if board[i][a] == True:
                new_list[i][a] = 10
            else:
                #if (i != 0 and i != x) and (a != 0 and a != y):
                for b in range(-1, 2):
                    for c in range(-1, 2):
                        if (not (b == 0 and c == 0)) and ((-1 < i+b < x+1) and (-1 < a+c < y+1)):
                            if board[i+b][a+c] == True:
                                total += 1      
                if total == 0:
                    new_list[i][a] = 9
                else:
                    new_list[i][a] = total            
    total = 0            
    return new_list
    
def mine_board(board):
    new_list = []
    for item in range(len(board)):
        new_list.append([])
        for i in range(height):
            new_list[item].append([])
            
    for i in range(len(board)):
        for a in range(len(board[0])):
            if board[i][a] == True:
                new_list[i][a] = 10
            else:
                new_list[i][a] = 0
    return new_list
               
    
def nine_spread(revealedBoxes, squares, boxx, boxy):
    x = len(squares)-1
    y = len(squares[0])-1
    i = boxx
    a = boxy
    d = squares[boxx][boxy]
    revealedBoxes[boxx][boxy] = [True, d]
    #if (i != 0 and i != x) and (a != 0 and a != y):
    for b in range(-1, 2):
        for c in range(-1, 2):
            if (not (b == 0 and c == 0)) and ((-1 < i+b < x+1) and (-1 < a+c < y+1)):
                d = squares[i+b][a+c]
                e = revealedBoxes[i+b][a+c][1]
                #e checks if any squares are marked as mines in revealedBoxes.
                #check for whether or not any surrounding squares are actually mines when right and left clicking.
                #if it is true, the game ends.
                if d != 9 and e != 11:
                    revealedBoxes[i+b][a+c] = [True, d]
                if d == 9 and revealedBoxes[i+b][a+c][0] == False:
                    nine_spread(revealedBoxes, squares, i+b, a+c)        
    return revealedBoxes
    

def check_surroundings(boxx, boxy, revealed, squares):
    x = len(squares)
    y = len(squares[0])
    total = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            if (not (a == 0 and b == 0)) and ((-1 < a + boxx < x) and (-1 < b + boxy < y)):
                if revealed[boxx+a][boxy+b][1] == 11:
                    total += 1
    if total != squares[boxx][boxy]:
        return False
    else:
        return True
        
def mine_coordinates(board, boxx, boxy):
    coords = []
    x = len(board)
    y = len(board[0])
    for a in range(-1, 2):
        for b in range(-1, 2):
            if (not (a == 0 and b == 0)) and ((-1 < boxx+a < x) and (-1 < boxy+b < y)):
                if type(board[boxx+a][boxy+b]) == type(1):
                    if board[boxx+a][boxy+b] == 10:
                        coords.append([boxx+a, boxy+b])
                elif type(board[boxx+a][boxy+b]) == type([]):
                    if board[boxx+a][boxy+b][1] == 11:
                        coords.append([boxx+a, boxy+b])
    return coords
    
    
        
        
def nine_spread_match(boxx, boxy, revealed, squares):
    user_coords = mine_coordinates(revealed, boxx, boxy)
    real_coords = mine_coordinates(squares, boxx, boxy)
    if user_coords == real_coords:
        return True
    else:
        return False
    
def wrong_coordinates(revealed, squares):
    wrong_coords = []
    x = len(revealed)
    y = len(revealed[0])
    for i in range(x):
        for a in range(y):
            for b in range(-1, 2):
                for c in range(-1, 2):
                    if (not (b == 0 and c == 0)) and ((-1 < i+b < x) and (-1 < a+c < y)):
                        test1 = revealed[i+b][a+c][1]
                        test2 = squares[i+b][a+c]
                        if test1 == 11 and test2 != 10:
                            revealed[i+b][a+c][1] = 12
    return revealed
    
                
def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((window_width, window_height))
    revealed = [[[False, 0]] * height for i in range(width)]
    mousex = 0
    mousey = 0
    pygame.display.set_caption("Mines")
    squares = set_mines(mines, num_squares)
    
    
    squares = set_rows_cols(squares, width, height)
    minedboard = mine_board(squares)
    squares = board_numbers(squares)
    
    #print_list(squares)
    #print_list(revealed)
    hover = False
    clicked = False
    boxx, boxy = None, None
    left_down = 0
    right_down = 0
    game_over = False
    won = False
    over = False
    first_click = True
    
    while True:
    
    
        clicked = False
        DISPLAYSURF.fill((255,255,255))
        pygame.draw.rect(DISPLAYSURF, black, (594, 9, 42, 42))
        pygame.draw.rect(DISPLAYSURF, color_list[0], (window_width/2 - 20, 10, 40, 40))
        pygame.draw.rect(DISPLAYSURF, black, (999, 9, 42, 42))
        pygame.draw.rect(DISPLAYSURF, color_list[0], (1000, 10, 40, 40))
        draw_board(width, height, window_width, window_height, revealed, hover)
        left = False
        right = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
            
                pygame.quit()
                sys.exit()
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                boxx, boxy = getBoxAtPixel(mousex, mousey)
                #clicked = False
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                boxx, boxy = getBoxAtPixel(mousex, mousey)
                hover = True
                clicked = False
            if event.type == MOUSEBUTTONUP and event.button == 1:
                left_down = 8
                #if event.button == 1, it means a left click
                mousex, mousey = event.pos
                boxx, boxy = getBoxAtPixel(mousex, mousey)
                hover = False
                clicked = True
                left = True
            if event.type == MOUSEBUTTONUP and event.button == 3:
                right_down = 8
                #if event.button == 3, it means a right click
                mousex, mousey = event.pos
                boxx, boxy = getBoxAtPixel(mousex, mousey)
                hover = False
                clicked = True
                right = True
            if event.type == MOUSEBUTTONUP and event.button == 2:
                right_down = 8
                left_down = 8
                mousex, mousey = event.pos
                boxx, boxy = getBoxAtPixel(mousex, mousey)
                hover = False
                clicked = True
                right = True
                left = True
                
                
        #print left_down, right_down
        if left_down > 0:
            left_down -= 1
        if right_down > 0:
            right_down -= 1
        if ((595 < mousex < 635) and (10 < mousey < 50)):
            if hover:
                pygame.draw.rect(DISPLAYSURF, color_list[9], (595, 10, 40, 40))
            if clicked:
                main()
        if ((1000 < mousex < 1040) and (10 < mousey < 50)):
            if hover:
                pygame.draw.rect(DISPLAYSURF, color_list[9], (1000, 10, 40, 40))
            if clicked:
                negative()
        
        
        if (boxx != None and boxy != None):
            if clicked == True and (not game_over):
                if first_click:
                    squares = set_mines(mines, num_squares)
                    squares = set_rows_cols(squares, width, height)
                    minedboard = mine_board(squares)
                    squares = board_numbers(squares)
                    while squares[boxx][boxy] != 9:
                        squares = set_mines(mines, num_squares)
                        squares = set_rows_cols(squares, width, height)
                        minedboard = mine_board(squares)
                        squares = board_numbers(squares)
                    first_click = False
                    
            
            
            
            
            
                if (left_down > 0 and right_down > 0) and (check_surroundings(boxx, boxy, revealed, squares) == True):
                    #check_surroundings(width, height, revealed)
                    nine_spread(revealed, squares, boxx, boxy)
                    #print nine_spread_match(boxx, boxy, revealed, squares)
                    if not nine_spread_match(boxx, boxy, revealed, squares):
                        revealed = wrong_coordinates(revealed, squares)
                        for a in range(len(revealed)):
                            for b in range(len(revealed[a])):
                                if minedboard[a][b] == 10 and revealed[a][b][1] != 11:
                                    revealed[a][b] = [True, 10]
                                    game_over = True
                
                                    
                        
                #print boxx, boxy
                if left_down>0 and revealed[boxx][boxy][0] == False:
                    #print revealed[boxx][boxy]
                    if revealed[boxx][boxy][1] != 11:
                        d = squares[boxx][boxy]
                        #sets revealed[boxx][boxy] to a list saying the square has been clicked, and giving it the number of mines
                        #adjacent to it. If the number is zero, it is given 9, and if it is a mine, it is given 10.
                        if d == 9:
                            nine_spread(revealed, squares, boxx, boxy)
                            #this is to open up more squares if there is an area of empty squares.
                        
                        if d == 10:
                            revealed = wrong_coordinates(revealed, squares)
                            revealed[boxx][boxy] = [True, 11]
                            for a in range(len(revealed)):
                                for b in range(len(revealed[a])):
                                    if minedboard[a][b] == 10 and revealed[a][b][1] != 11:  
                                        revealed[a][b] = [True, 10]
                                        game_over = True
                        revealed[boxx][boxy] = [True, d]
                if right and not won:
                    if revealed[boxx][boxy] == [False, 0]:
                        #revealed[boxx][boxy] = 0
                        revealed[boxx][boxy] = [True, 11]
                        count = 0
                        for a in range(len(revealed)):
                            for b in range(len(revealed[0])):
                                if revealed[a][b][1] == 11 and minedboard[a][b] == 10:
                                    count += 1
                        if count == mines:
                            won = True 
                                
                    elif revealed[boxx][boxy] == [True, 11]:
                        #revealed[boxx][boxy] = 0
                        revealed[boxx][boxy] = [False, 0]
            elif hover == True and not game_over:
                test = revealed[boxx][boxy][0]
                if (not test):
                    drawHighlightBox(boxx, boxy)
                
        pygame.display.update()
        FPSCLOCK.tick(FPS)
"""def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)"""
    
    
if __name__ == "__main__":
    main()















