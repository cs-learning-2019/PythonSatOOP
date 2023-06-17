# Image Processing
# This projects takes a photo and detects the edges
# Author: Kavan Lam
# Date: June 10, 2023
from Queue import *

def setup():
    global img, done
    size(700, 700)
    img = loadImage("Cells.png")
    img.loadPixels()
    done = False
    
def draw():
    global img, done
    if not done:
        img_new = createImage(img.width,img.height,RGB)
        edges = detectEdges(img)
        print("There are " + str(countConnectedComponents(edges, img.width,img.height)) + " cells")
        for y in range(img.height):
            for x in range(img.width):
                loc = x + (y * img.width)
                img_new.pixels[loc] = color(edges[loc])
        image(img_new,0,0)
        done = True

def countConnectedComponents(edges, imgWidth, imgHeight):
    q = Queue()
    curLabel = 0
    pixelLabel = [None] * len(edges)
    
    for y in range(imgHeight):
        for x in range(imgWidth):
            loc = x + (y * imgWidth)
            # Skip this pixel if it already has a label
            if not(pixelLabel[loc] is None):
                continue
            
            if (edges[loc] == 0):
                pixelLabel[loc] = -1
                continue
            
            curLabel += 1
            pixelLabel[loc] = curLabel
            q.enqueue((x, y))
            # We will loop until there are no more pieces of the cell to look at
            while not q.isEmpty():
                curPosition = q.dequeue()
                a = curPosition[0]
                b = curPosition[1]
                adjacentPositions = [(a-1, b-1), (a, b-1), (a+1, b-1), (a-1, b), (a+1, b), (a-1, b+1), (a, b+1), (a+1, b+1)]
                for adjPos in adjacentPositions:
                    newLoc = adjPos[0] + (adjPos[1] * imgWidth)
                    if newLoc >= 0 and newLoc <= ((imgWidth * imgHeight) - 1):
                        if (edges[newLoc] == 255 and pixelLabel[newLoc] is None):
                            pixelLabel[newLoc] = curLabel
                            # We add the adjacent position to the queue since we want to process the neighbours of that pixel as well
                            q.enqueue(adjPos)         
    return curLabel

# Slightly blurs an image using a 3x3 Gaussian filter
def imageBlur(imgArray, imgWidth, imgHeight):
    newImgArray = []
    for y in range(imgHeight):
        for x in range(imgWidth):
            loc = x + (y * imgWidth)
            adjacentPixels = [(x-1, y-1, 1), (x, y-1, 2), (x+1, y-1, 1), (x-1, y, 2), (x+1, y, 2), (x-1, y+1, 1), (x, y+1, 2), (x+1, y+1, 1)]
            totalValue = 4.0 * imgArray[loc]
            totalWeight = 4
            for adjacentPixel in adjacentPixels:
                newLoc = adjacentPixel[0] + (adjacentPixel[1] * imgWidth)
                if newLoc >= 0 and newLoc <= ((imgWidth * imgHeight) - 1):
                    totalValue += imgArray[newLoc] * adjacentPixel[2]
                    totalWeight += adjacentPixel[2]
            newImgArray.append(totalValue / totalWeight)
    return newImgArray

# Computes the image gradient magnitude using the Sobel filters
def imageGradientMagnitude(imgArray, imgWidth, imgHeight):
    newImgArray = []
    for y in range(imgHeight):
        for x in range(imgWidth):
            loc = x + (y * imgWidth)
            sobelX = [(x-1, y-1, 1), (x+1, y-1, -1), (x-1, y, 2), (x+1, y, -2), (x-1, y+1, 1), (x+1, y+1, -1)]
            sobelY = [(x-1, y-1, 1), (x, y-1, 2), (x+1, y-1, 1), (x-1, y+1, -1), (x, y+1, -2), (x+1, y+1, -1)]
            mx = 0.0
            my = 0.0
            for pixel in sobelX:
                newLoc = pixel[0] + (pixel[1] * imgWidth)
                if newLoc >= 0 and newLoc <= ((imgWidth * imgHeight) - 1):
                    mx += imgArray[newLoc] * pixel[2]
            for pixel in sobelY:
                newLoc = pixel[0] + (pixel[1] * imgWidth)
                if newLoc >= 0 and newLoc <= ((imgWidth * imgHeight) - 1):
                    my += imgArray[newLoc] * pixel[2]
            newImgArray.append(sqrt(mx ** 2 + my ** 2))
    return newImgArray

# Detect edges in an image using the first 2 steps here https://en.wikipedia.org/wiki/Canny_edge_detector with simple thresholding
def detectEdges(img):
    imageIntensity = []
    for i in range(len(img.pixels)):
        imageIntensity.append(brightness(img.pixels[i]))
    
    imgWidth = img.width
    imgHeight = img.height
    blurredImage = imageBlur(imageIntensity, imgWidth, imgHeight)
    gradientMagnitude = imageGradientMagnitude(blurredImage, imgWidth, imgHeight)
    gradientThreshold = 50
    for i in range(len(gradientMagnitude)):
        if gradientMagnitude[i] > gradientThreshold:
            gradientMagnitude[i] = 255
        else:
            gradientMagnitude[i] = 0
                    
    return gradientMagnitude
                
