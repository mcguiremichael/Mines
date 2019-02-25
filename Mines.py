#!/usr/bin/env python


import pygame
import Button
import MineMap


def leftButtonNum():
    return 1
    
def rightButtonNum():
    return 3

def main():

    pygame.init()
    window = pygame.display.set_mode((1400, 800))
    windowclock = pygame.time.Clock()

    #Initializes the map
    Map = initialize(window)    
    currentCoords = None
    frame = 0
    font = pygame.font.Font(None, 20)
    while True:
        currentCoords = runGame(window, Map, currentCoords, frame)
        frame += 1
        pygame.display.update()
        windowclock.tick(60)
        
def initialize(surface):
    mapWidth = 30
    mapHeight = 16
    numMines = 99
    Map = MineMap.MineMap(mapWidth, mapHeight, numMines, surface)
    return Map
    
def runGame(surface, Map, coords, frame):
    surface.fill(MineMap.MineMap.BACKGROUNDCOLOR)
    
    Map.drawMap()

    #Event loop
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            raise SystemExit()
            
       
        if (event.type == pygame.MOUSEBUTTONUP):
            pos = event.pos
            if (Map.resetClicked(pos)):
                Map.resetButton.clicked = False
                Map.startNewGame()
                return None
                
        if (Map.frozen == True):
            return coords
            
        elif (event.type == pygame.MOUSEMOTION):
            pos = event.pos
            newCoords = Map.getSquareFromCoords(pos)
            
            if ((Map.leftDown == True) or (Map.rightDown == True)):
                if (coords != newCoords):
                    if (coords != None):
                        Map.setSquareHovering(coords, False)
                    if (newCoords != None):
                        Map.setSquareHovering(newCoords, True)
            coords = newCoords
                        
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            pos = event.pos
            newCoords = Map.getSquareFromCoords(pos)
            buttonNum = event.button
            if (Map.resetClicked(pos)):
                Map.resetButton.clicked = True
            if (newCoords == None):
                continue
            if (buttonNum == leftButtonNum()):
                Map.leftDown = True
            if (buttonNum == rightButtonNum()):
                Map.rightDown = True
            Map.logs.append([newCoords, buttonNum, True, frame])
            Map.setSquareHovering(newCoords, True)
            coords = newCoords
            
        elif (event.type == pygame.MOUSEBUTTONUP):
            buttonNum = event.button
            pos = event.pos
            newCoords = Map.getSquareFromCoords(pos)
            if (newCoords == None):
                Map.leftDown = False
                Map.rightDown = False
                Map.logs.append([newCoords, 0, False, frame])
                continue
            Map.logs.append([newCoords, buttonNum, False, frame])
            if (Map.doubleClickEvent(leftButtonNum(), rightButtonNum()) == True and (Map.canClearSurroundings(newCoords) == True)):
                Map.clearSurroundings(newCoords)
                Map.leftDown = False
                Map.rightDown = False
                continue
            
            if (Map.leftDown == True and Map.rightDown == True):
                if (buttonNum == leftButtonNum()):
                    Map.leftDown = False
                else:
                    Map.rightDown = False
                continue
            
            if (buttonNum == leftButtonNum()):
                Map.setSquareHovering(newCoords, False)
                Map.leftDown = False
                if (Map[newCoords].flagged == True):
                    continue
                Map.setSquareClicked(newCoords, True)
                if Map[newCoords].value == 0:
                    Map.clearSurroundings(newCoords)
                
            if (buttonNum == rightButtonNum()):
                Map.rightDown = False
                if (Map[newCoords].clicked == False):
                    Map.setSquareFlagged(newCoords, not Map[newCoords].flagged)
                    Map.setSquareHovering(newCoords, False)
                    
            coords = newCoords
            
            
    return coords
          
if __name__ == "__main__":
    main()
    


















