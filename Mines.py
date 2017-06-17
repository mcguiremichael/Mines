import pygame
import Button
import MineMap

def main():

    pygame.init()
    window = pygame.display.set_mode((1400, 800))
    windowclock = pygame.time.Clock()

    #Initializes the map
    Map = initialize(window)    
    currentCoords = None
    down = False
    while True:
        [currentCoords, down] = runGame(window, Map, currentCoords, down)
        pygame.display.update()
        windowclock.tick(60)
        
def initialize(surface):
    mapWidth = 30
    mapHeight = 16
    numMines = 5
    boxWidth = 37
    margin = 1
    topLeftX = 10
    topLeftY = 10
    Map = MineMap.MineMap(mapWidth, mapHeight, numMines, topLeftX, topLeftY, boxWidth, 1, surface, [])
    return Map
    
def runGame(surface, Map, coords, down):
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            raise SystemExit()
            
            
        elif (event.type == pygame.MOUSEMOTION):
            pos = event.pos
            newCoords = Map.getSquareFromCoords(pos)
            
            if down == True:
                print newCoords
                if (coords != newCoords):
                    if (coords != None):
                        Map.setSquareHovering(coords, False)
                    if (newCoords != None):
                        Map.setSquareHovering(newCoords, True)
            coords = newCoords
                        
                        
        elif (event.type == pygame.MOUSEBUTTONDOWN):
            pos = event.pos
            newCoords = Map.getSquareFromCoords(pos)\
            
            if (newCoords != None):
                down = True
                Map.setSquareHovering(newCoords, True)
            coords = newCoords
            
            
        elif (event.type == pygame.MOUSEBUTTONUP):
            pos = event.pos
            newCoords = Map.getSquareFromCoords(pos)
            
            button = event.button
            if (newCoords != None and down == True):
                Map.setSquareClicked(newCoords, True)
                Map.setSquareHovering(newCoords, False)
            coords = newCoords
            down = False
            if Map[coords].value == 0:
                Map.clearSurroundings(coords)
                    
    Map.drawMap()
    return coords, down
            
        
if __name__ == "__main__":
    main()
    

