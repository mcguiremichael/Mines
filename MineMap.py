import random
import GridSquare
import EventSquare

class MineMap:


    OFFCOLOR = (210, 210, 210)
    ONCOLOR = (140, 140, 140)
    BACKGROUNDCOLOR = (160, 160, 135)
    #each box in the grid is 37 pixels across
    boxWidth = 39
    margin = 1
    leftButtonNum = 1
    rightButtonNum = 3
    debugMode = False

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
    margin : int
        The number of pixels between a GridSquare in grid and the GridSquares surrounding it
    surface : pygame.display
        The window on which the grid will be displayed as the game is played
    squaresClicked : [[int, int]]
        The list of pairs of x and y coordinates that have already been clicked
    """
    def __init__(self, mapWidth, mapHeight, numMines, surface):
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight
        self.numMines = numMines
        self.surface = surface
        
        
        
        #Maximum number of frames that can pass between the letting up of both buttons in order to call revealSurroundings.
        self.timeThreshold = 30
        self.grid = []
        self.squaresClicked = []
        
         #Each time a user event happens (The left or right mouse buttons are either clicked down or let up), logs will store the location of the event and the frame in which it happened.
        #Each entry into logs will be of the following format:
        #   logs[i] = [position, buttonNumber, up(False) or down(True), frame]
        self.logs = []
        self.leftDown = False
        self.rightDown = False
        self.frozen = False
        
        #Topleft most coords of the game grid, in pixel values
        self.topLeftX = (self.surface.get_width() - ((MineMap.boxWidth + MineMap.margin) * self.mapWidth)) / 2
        self.topLeftY = 100
        
        
        self.resetButton = self.makeResetButton()
        
        self.randomizeGrid()
        
    def makeResetButton(self):
        width = 60
        x = (self.surface.get_width() - width) / 2
        y = 20
        offColor = MineMap.OFFCOLOR
        onColor = MineMap.ONCOLOR
        return EventSquare.EventSquare(x, y, width, offColor, onColor, False, self.surface)
        
    def startNewGame(self):
        self.randomizeGrid()
        self.squaresClicked = []
        self.logs = []
        self.leftDown = False
        self.rightDown = False
        self.frozen = False
        
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
                x = self.topLeftX + j * (MineMap.boxWidth + MineMap.margin)
                y = self.topLeftY + i * (MineMap.boxWidth + MineMap.margin)
                #Change that True to False in release
                self.grid[i][j] = GridSquare.GridSquare(x, y, MineMap.boxWidth, MineMap.OFFCOLOR, MineMap.ONCOLOR, self.surface, adjacentGrid[i][j], MineMap.debugMode, False, False)
        
    def randomizeGrid(self):
        numSquares = self.mapWidth * self.mapHeight
        if (self.numMines >= numSquares):
            self.numMines = numSquares - 1
        mineGrid = self.disperseMines()
        adjacentGrid = getAdjacentGrid(mineGrid, 9)
        self.initializeGrid(adjacentGrid)    
        
    def randomizeIndices(self, totalNum):
        values = [i for i in range(totalNum)]
        invalidIndices = []
        for i in self.squaresClicked:
            index = i[0] + i[1] * self.mapWidth
            invalidIndices.append(index)
        for i in sorted(invalidIndices, reverse=True):
            del values[i]
        randomIndices = random.sample(values, self.numMines)
        return randomIndices
        
    def drawMap(self):
        for i in range(self.mapHeight):
            for j in range(self.mapWidth):
                self.grid[i][j].drawSquare()
        self.resetButton.drawSquare()
                
    def getSquareFromCoords(self, pos):
        if (pos[0] <= self.maxXCoord() and pos[0] >= self.topLeftX and pos[1] <= self.maxYCoord() and pos[1] >= self.topLeftY):
            x = (pos[0] - self.topLeftX) / (MineMap.boxWidth + MineMap.margin)
            y = (pos[1] - self.topLeftY) / (MineMap.boxWidth + MineMap.margin)
            return [x, y]
        else:
            return None
        
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
                if (square.flagged == True and square.isMine()):
                    continue
                self.setSquareClicked([newX, newY], True)
                if (square.value == 0):
                    self.clearSurroundings([newX, newY])
                    
    def canClearSurroundings(self, coords):
        total = 0
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
                
                if self.grid[newY][newX].flagged == True:
                    total += 1
                    
        return total == self.grid[y][x].value
        
    def doubleClickEvent(self, left, right):
        if (self.leftDown == self.rightDown):
            return False
        
        desiredButtonVal = 0
        if (self.leftDown == True):
            desiredButtonVal = right
        else:
            desiredButtonVal = left
            
        last = len(self.logs)-1
        i = last - 1
        while i >= 0:
            log = self.logs[i]
            lastLog = self.logs[last]
            if (log[3] - lastLog[3] > self.timeThreshold):
                return False
            if log[0] == None:
                return False
            if ((log[1] == desiredButtonVal) and (log[2] == False)):
                if (log[0] != lastLog[0]):
                    return False
                return True
            if ((log[1] != desiredButtonVal) and (log[2] == False)):
                return False
            i -= 1
        return False
                    
    def gameOver(self):
        self.frozen = True
        self.displayMines()
    
    def maxXCoord(self):
        return self.topLeftX + self.mapWidth * (MineMap.boxWidth + MineMap.margin) - 1
        
    def maxYCoord(self):
        return self.topLeftY + self.mapHeight * (MineMap.boxWidth + MineMap.margin) - 1
        
    def displayMines(self):
        for i in self.grid:
            for j in i:
                if (j.value == 9 and j.flagged == False):
                    j.clicked = True
                if (j.value != 9 and j.flagged == True):
                    j.value = 10
                    
    def setSquareClicked(self, coords, isClicked):
        if (len(self.squaresClicked) == 0):
            self.squaresClicked.append(coords)
            self.randomizeGrid()
        else:
            self.squaresClicked.append(coords)
        if ((self.grid[coords[1]][coords[0]]).isMine() == True and self.grid[coords[1]][coords[0]].flagged == False):
            self.gameOver()
        self.grid[coords[1]][coords[0]].clicked = isClicked
        
    def setSquareFlagged(self, coords, isFlagged):
        self.grid[coords[1]][coords[0]].flagged = isFlagged
        
    def setSquareHovering(self, coords, isHovering):
        self.grid[coords[1]][coords[0]].hovering = isHovering
        
    def __getitem__(self, key):
        return self.grid[key[1]][key[0]]
        
    def resetClicked(self, pos):
        b = self.resetButton
        if ((pos[0] >= b.x and pos[0] <= b.upperX) and (pos[1] >= b.y and pos[1] <= b.upperY)):
            return True
        return False
                
       
                            
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
    
    
    
