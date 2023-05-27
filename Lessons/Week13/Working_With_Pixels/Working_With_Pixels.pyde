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

do_once = True
done = False
def draw():
    global do_once, done
    if not done or not do_once:
        draw6()
        done = True

def draw6():
    global img
    img_new = createImage(img.width,img.height,RGB)
    for x in range(img.width):
        for y in range(img.height):
            rs = []
            bs = []
            gs = []
            totalWeight = 0
            
            loc = x + y*img.width
            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
            rs.append(r)
            gs.append(g)
            bs.append(b)
            totalWeight += 1
            
            # Bottom Pixel
            if (x + (y+1)*img.width) <= 148207:
                loc1 = (x + (y+1)*img.width)
                rs.append(red(img.pixels[loc1]) * 5)
                gs.append(green(img.pixels[loc1]) * 5)
                bs.append(blue(img.pixels[loc1]) * 5)
                totalWeight += 5
            
            # Right Pixel
            if  ((x+1) + y*img.width) <= 148207:
                loc3 = ((x+1) + y*img.width)
                r3 = red(img.pixels[loc3]) * 5
                g3 = green(img.pixels[loc3]) * 5
                b3 = blue(img.pixels[loc3]) * 5
                rs.append(r3)
                gs.append(g3)
                bs.append(b3)
                totalWeight += 5
            
            # Top pixel
            if (x + (y-1)*img.width) >= 0:
                loc4 = (x + (y-1)*img.width)
                r4 = red(img.pixels[loc4]) * 5
                g4 = green(img.pixels[loc4]) * 5
                b4 = blue(img.pixels[loc4]) * 5
                rs.append(r4)
                gs.append(g4)
                bs.append(b4)
                totalWeight += 5
            
            # Left pixel
            if ((x-1) + y*img.width) >= 0:
                loc2 = ((x-1) + y*img.width)
                r2 = red(img.pixels[loc2]) * 5
                g2 = green(img.pixels[loc2]) * 5
                b2 = blue(img.pixels[loc2]) * 5
                rs.append(r2)
                gs.append(g2)
                bs.append(b2)
                totalWeight += 5
            
            newR = (sum(rs)/totalWeight)
            newG = (sum(gs)/totalWeight)
            newB = (sum(bs)/totalWeight)
            img_new.pixels[loc] = color(newR,newG,newB)
    img_new.updatePixels()
    image(img_new, 0, 0)
    
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
    
