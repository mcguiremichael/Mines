import random
import GridSquare

class MineMap:


    OFFCOLOR = (200, 200, 200)
    ONCOLOR = (100, 100, 100)

    """
    Creates a MineMap, a grid that stores the information in an array of GridSquares.
    
    Parameters
    ----------
    mapWidth : int
        The number of GridSquares that are in each row of grid
    mapHeight : int
        The number of GridSquares that are in each column of grid
    numMines : int
        The number of mines that will be dispersed throughout the grid
    topLeftX : int
        The x-value of the topleft-most coordinate in the grid when it is displayed
    topLeftY : int
        The y-value of the topleft-most coordinate in the grid when it is displayed
    boxWidth : int
        The number of pixels the sides of each GridSquare in grid is composed of
    marginSize : int
        The number of pixels between a GridSquare in grid and the GridSquares surrounding it
    surface : pygame.display
        The window on which the grid will be displayed as the game is played
    squaresClicked : [[int, int]]
        The list of pairs of x and y coordinates that have already been clicked
    """
    def __init__(self, mapWidth, mapHeight, numMines, topLeftX, topLeftY, boxWidth, marginSize, surface, squaresClicked):
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.numMines = numMines
        self.topLeftX = topLeftX
        self.topLeftY = topLeftY
        self.boxWidth = boxWidth
        self.marginSize = marginSize
        self.surface = surface
        self.squaresClicked = squaresClicked
        
        self.grid = []
        self.randomizeGrid()
        
    def reinitialize(self):
        temp = self.numMines
        self.numMines = 0
        self.randomizeGrid()
        self.numMines = temp
        
    def disperseMines(self):
        totalNum = self.mapHeight * self.mapWidth
        dispersedGrid = []
        dispersedPlaces = self.randomizeIndices(totalNum)
        dispersedGrid = [[0 for i in range(self.mapWidth)] for i in range(self.mapHeight)]
        for i in range(len(dispersedPlaces)):
            x = dispersedPlaces[i] / self.mapWidth
            y = dispersedPlaces[i] % self.mapWidth
            dispersedGrid[x][y] = 9
        return dispersedGrid
        
    def initializeGrid(self, adjacentGrid):
        self.grid = [[0 for i in range(self.mapWidth)] for i in range(self.mapHeight)]
        for i in range(self.mapHeight):
            for j in range(self.mapWidth):
                x = self.topLeftX + j * (self.boxWidth + self.marginSize)
                y = self.topLeftY + i * (self.boxWidth + self.marginSize)
                #Change that True to False in release
                self.grid[i][j] = GridSquare.GridSquare(x, y, self.boxWidth, MineMap.OFFCOLOR, MineMap.ONCOLOR, self.surface, adjacentGrid[i][j], False, False, False)
        
    def randomizeGrid(self):
        numSquares = self.mapWidth * self.mapHeight
        if (self.numMines >= numSquares):
            self.numMines = numSquares - 1
        minePlaces = random.sample(range(0, numSquares), self.numMines)
        mineGrid = self.disperseMines()
        adjacentGrid = getAdjacentGrid(mineGrid, 9)
        self.initializeGrid(adjacentGrid)    
        
    def randomizeIndices(self, totalNum):
        values = [i for i in range(totalNum)]
        invalidIndices = []
        for i in self.squaresClicked:
            index = i[0] + i[1] * self.mapHeight
            invalidIndices.append(index)
        for i in sorted(invalidIndices, reverse=True):
            del values[i]
        randomIndices = random.sample(values, self.numMines)
        return randomIndices
        
    def drawMap(self):
        for i in range(self.mapHeight):
            for j in range(self.mapWidth):
                self.grid[i][j].drawSquare()
                
    def getSquareFromCoords(self, pos):
        if (pos[0] <= self.maxXCoord() and pos[0] >= self.topLeftX and pos[1] <= self.maxYCoord() and pos[1] >= self.topLeftY):
            x = (pos[0] - self.topLeftX) / (self.boxWidth + self.marginSize)
            y = (pos[1] - self.topLeftY) / (self.boxWidth + self.marginSize)
            return [x, y]
        else:
            return None
        
    def reveal(self, xcoord, ycoord):
        revealedBox = self.getSquareFromCoords(xcoord, ycoord)
        if revealedBox == None:
            return
        revealedBox.clicked = True
        revealedBox.drawSquare()
        if (revealedBox.value == 9):
            revealedBox.drawWrongChoice()
            self.displayMines()
        
        
    def clearSurroundings(self, coords):
        x = coords[0]
        y = coords[1]
        for i in range(-1, 2):
            newY = y + i
            if (newY < 0 or newY >= self.mapHeight):
                continue
                
            for j in range(-1, 2):
                newX = x + j
                if (newX < 0 or newX >= self.mapWidth):
                    continue
                    
                square = (self.grid)[newY][newX]
                if (square.clicked == True):
                    continue
                square.clicked = True
                if (square.value == 0):
                    self.clearSurroundings([newX, newY])
    
    def maxXCoord(self):
        return self.topLeftX + self.mapWidth * (self.boxWidth + self.marginSize) - 1
        
    def maxYCoord(self):
        return self.topLeftY + self.mapHeight * (self.boxWidth + self.marginSize) - 1
        
    def displayMines(self):
        for i in (len(self.grid)):
            for j in (len(self.grid[0])):
                if (self.grid[i][j].value == 9):
                    self.grid[i][j].drawSquare()
                    
    def setSquareClicked(self, coords, isClicked):
        self.grid[coords[1]][coords[0]].clicked = isClicked
        
    def setSquareFlagged(self, coords, isFlagged):
        self.grid[coords[1]][coords[0]].flagged = isFlagged
        
    def setSquareHovering(self, coords, isHovering):
        self.grid[coords[1]][coords[0]].hovering = isHovering
        
    def __getitem__(self, key):
        return self.grid[key[1]][key[0]]
                
       
                            
#key must be greater than 8
def getAdjacentGrid(mineGrid, key):
    
    height = len(mineGrid)
    width = 0
    #empty list checking
    if (height > 0):
        width = len(mineGrid[0])
    else:
        return []
            
    #Iterates through rows
    for i in range(height):
        #Iterates through columns
        for j in range(width):
            if (mineGrid[i][j] == key):
                continue
            #Check the surroundings of each square
            for a in range(-1, 2):
                y = i + a
                #edge checking
                if (y >= height or y < 0):
                    continue
                        
                for b in range(-1, 2):
                    x = j + b
                    #edge checking
                    if (x >= width or x < 0):
                        continue
                    if (mineGrid[y][x] == key):
                        mineGrid[i][j] += 1
    return mineGrid
