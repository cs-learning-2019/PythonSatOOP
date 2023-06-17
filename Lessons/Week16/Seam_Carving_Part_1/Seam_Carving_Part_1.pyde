# Image Processing
# Seam Carving PART 1
# Author: Kavan Lam
# Date: June 17, 2023
def setup():
    global img, done
    size(700, 700)
    img = loadImage("Castle.PNG")
    img.loadPixels()
    done = False
    
def draw():
    global img, done
    if not done:
        edges = detectEdges(img)
        
        img_new = createImage(img.width,img.height,RGB)
        for i in range(len(edges)):
            img_new.pixels[i] = color(edges[i])
                
        image(img_new,0,0)
        done = True

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
                
