# Image Processing
# Seam Carving PART 1
# Author: Kavan Lam
# Date: June 17, 2023
def setup():
    global img, done, targetWidth
    size(700, 700)
    img = loadImage("Castle.PNG")
    img.loadPixels()
    done = False
    targetWidth = 400
    
def draw():
    global img, done, targetWidth
    if not done:
        currentWidth = img.width
        edges = detectEdges(img)
        for i in range(img.width - targetWidth):
            loadPixels()
            seam = computeSeam(edges, currentWidth, img.height)
            
            currentWidth -= 1
            newEdges = []
            imgNew = createImage(currentWidth, img.height, RGB)
            for index in seam:
                edges[index] = None
                img.pixels[index] = -1
                    
            nextLoc = 0
            for loc in range(len(edges)):
                if edges[loc] is None:
                    continue
                newEdges.append(edges[loc])
                imgNew.pixels[nextLoc] = img.pixels[loc]
                nextLoc += 1
                
            edges = newEdges
            img = imgNew
            updatePixels() 
                
        image(img,0,0)
        done = True

# Compute the seam according to the algorithm here https://en.wikipedia.org/wiki/Seam_carving
def computeSeam(edges, imgWidth, imgHeight):
    minCost = [None] * len(edges)
    for y in range(imgHeight):
        for x in range(imgWidth):
            loc = x + (y * imgWidth)
            if y == 0:
                minCost[loc] = (edges[loc], None)
            else:
                neighbors = [(x-1) + ((y-1) * imgWidth), (x+1) + ((y-1) * imgWidth)] 
                minNeighbor = (minCost[x + ((y-1) * imgWidth)][0], x + ((y-1) * imgWidth)) # (Min cost, index)
                for neighbor in neighbors:
                    if neighbors >= 0 and neighbors <= len(edges) - 1:
                        if minCost[neighbor][0] < minNeighbor[0]:
                            minNeighbor = (minCost[neighbor][0], neighbor)
                minCost[loc] = (minNeighbor[0] + edges[loc], minNeighbor[1])
    
    y = imgHeight - 1
    seamStartLoc = (0, y)
    minTotalCost = minCost[0 + (y * imgWidth)][0]
    for x in range(imgWidth):
        if minCost[x + (y * imgWidth)][0] < minTotalCost:
            seamStartLoc = (x, y)
            minTotalCost = minCost[x + (y * imgWidth)][0]
    
    seam = [seamStartLoc[0] + (seamStartLoc[1] * imgWidth)]
    seamCurLoc = seamStartLoc[0] + (seamStartLoc[1] * imgWidth)
    while True:
        if minCost[seamCurLoc][1] is None:
            break
        seam.append(minCost[seamCurLoc][1])
        seamCurLoc = minCost[seamCurLoc][1]
        
    return seam

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
    return gradientMagnitude
                
