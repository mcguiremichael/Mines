import random
import printerHelper

def disperse(width, height, default, key, number):
    output = [[default for i in range(width)] for i in range(height)]
    gridSize = width * height
    values = random.sample(range(0, gridSize), number)
    for i in range(len(values)):
        x = values[i] / width
        y = values[i] % width
        output[x][y] = key
    return output

def main():
    width = 10
    height = 10
    default = 0
    key = 1
    number = 10
    averages = [[0 for i in range(width)] for i in range(height)]
    numRuns = 100000
    for i in range(numRuns):
        grid = disperse(width, height, default, key, number)
        for j in range(len(averages)):
            for k in range(len(averages[j])):
                averages[j][k] += (1.0 * grid[j][k])
    printerHelper.printList(averages)
                
    for i in range(len(averages)):
        for j in range(len(averages[i])):
            print averages[i][j], numRuns
            averages[i][j] = averages[i][j] / numRuns
    printerHelper.printList(averages)
    expectedAverage = (number / (1.0 * width * height)) * key
    print "these values compare to the value of " + str(expectedAverage)            
    
if __name__ == "__main__":
    main()    
