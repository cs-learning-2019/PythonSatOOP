# Image Processing
# This project replicates the software required to work with green screen photos
# Author: Kavan Lam
# Date: June 6,2020


"""
Helpful Functions and notes
1) createImage(200,200,RGB) -- Create blank color image
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

done = False

def setup():
    global img_fg
    global img_bg
    size(1000, 667)
    
    # Load in the fg and bg images (they are they same dimensions)
    img_fg = loadImage("fg.jpg")
    img_bg = loadImage("bg.jpg")

# Green Screen
def draw():
    global img_fg
    global img_bg
    global done
    
    if done == False:
        # Create a new picture to contain the result
        img_new = createImage(img_fg.width, img_fg.height, RGB)
        
        # We are going to look at both image's pixels
        img_fg.loadPixels()
        img_bg.loadPixels()
        img_new.loadPixels()
    
        for x in range(img_fg.width):
            for y in range(img_fg.height):
                # Pixel location and color
                loc = x + y*img_fg.width
                pix_fg = img_fg.pixels[loc]
                pix_bg = img_bg.pixels[loc]
                
                # Take the bg pixel and put it into the new image
                img_new.pixels[loc] = color(red(pix_bg), green(pix_bg), blue(pix_bg))

                # Take the fg pixel and put in into the new image only if not green
                r = abs(red(pix_fg) - 47)
                g = abs(green(pix_fg) - 255)
                b = abs(blue(pix_fg) - 22)
                    
                if not (r < 40 and g < 40 and b < 40):
                    img_new.pixels[loc] = color(red(pix_fg), green(pix_fg), blue(pix_fg))
        
        # We changed the pixels in destination
        img_new.updatePixels()
        # Display the destination
        image(img_new,0,0)
                
        done = True       
                
                
