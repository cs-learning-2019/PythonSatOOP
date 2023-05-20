# Focus Learning
# Image Processing
# Author: Kavan Lam
# Date: May 13, 2023

"""
Helpful Functions and notes
1) createImage(width,height,RGB) -- Create blank color image (can also use ALPHA or ARGB)
2) loadImage("file.jpg")
3) image(img, locx, locy, sizex, sizey)
4) tint(brightness, alpha) or tint(R, G, B, alpha)
5) loadPixels() -- loads the pixels from the object to the pixels array
6) updatePixels() -- update the object with the pixels inside the pixels array
7) The pixels array in 1D (so 2D projected onto 1D)
8) Because of 7, location = x + (y * width). Width is left to right
9) color(greyscale value 0-255) or color(R, G, B)
10) use red(), green(), blue() to extract components from color
11) constrain(x,0,255) -- make x between 0 and 255
12) brightness(img.pixels[loc]) -- gives a num from 0 to 255 that represents the brightness of a pixel
"""
def setup():
    global img
    frameRate(144);
    img = loadImage("girl.JPG")
    print("The image has a width of :" + str(img.width))
    print("The image has a height of:" + str(img.height))
    size(472, 314)

do_once = False
done = False
def draw():
    global do_once, done
    if not done or not do_once:
        draw5()
        done = True
    
#--------------------------------------------------------------------------------------
# Flips image from left to right
def draw1():
    global img
    img_new = createImage(img.width,img.height,RGB)
    img.loadPixels()
    
    for y in range(img.height):  # y = row_num
        for x in range(img.width): # x = col_num
            loc = (x + (y * img.width))

            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
      
            # Set the display pixel to the image pixel
            loc = ((img.width-(x+1)) + (y * img.width))
            img_new.pixels[loc] = color(r,g,b)  

    img_new.updatePixels()   
    #tint(255,255, 255, 255)
    #tint(100, 255)
    image(img_new, 0, 0)

#--------------------------------------------------------------------------------------
# Reverse image
def draw2():
    global img
    img_new = createImage(img.width,img.height,RGB)
    img_new.loadPixels()
    img.loadPixels()
    for y in range(img.height):  # y = row_num
        for x in range(img.width): # x = col_num
            loc = (x + (y * img.width))
    
            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
    
            # Set the display pixel to the image pixel
            img_new.pixels[loc] =  color(r,g,b)  
    img_new.pixels = img_new.pixels[::-1]       
    img_new.updatePixels()   
    background(img_new) 

#--------------------------------------------------------------------------------------
# Flash light on picture
def draw3():
    global img
    img.loadPixels()
    img_new = createImage(img.width,img.height,RGB)
    for x in range(img.width):
        for y in range(img.height):
            # Calculate the 1D pixel location
            loc = x + y*img.width
            # Get the R,G,B values from image
            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
            
            # Calculate an amount to change brightness 
            # based on proximity to the mouse
            distance = dist(x,y,mouseX,mouseY)
            adjustBrightness = (200 - distance)/200
            r *= adjustBrightness
            g *= adjustBrightness
            b *= adjustBrightness
        
            # Constrain RGB to between 0-255
            r = constrain(r,0,255)
            g = constrain(g,0,255)
            b = constrain(b,0,255)
            
            img_new.pixels[loc] = color(r,g,b)
            
    img_new.updatePixels()
    background(img_new)
    
#--------------------------------------------------------------------------------------
# Converts image to black and white
def draw4(): 
    # We are going to look at both image's pixels
    img.loadPixels()
    img_new = createImage(img.width,img.height,ALPHA)
  
    for x in range(img.width):
        for y in range(img.height): 
            loc = x + y*img.width
            img_new.pixels[loc]  = color(brightness(img.pixels[loc]))

    img_new.updatePixels()
    image(img_new, 0, 0)

#--------------------------------------------------------------------------------------
# Point art
def draw5(): 
    global img
    x = int(random(img.width))
    y = int(random(img.height))
    loc = x + y*img.width
    r = red(img.pixels[loc])
    g = green(img.pixels[loc])
    b = blue(img.pixels[loc])
    
    fill(r, g, b, 50)
    noStroke()
    ellipse(x, y, 20, 20)
    
