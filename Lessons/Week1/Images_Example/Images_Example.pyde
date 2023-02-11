def setup():
    global img1
    
    size(900, 900)
    img1 = loadImage("background.jpg")
    
def draw():
    global img1
    rect(100, 100, 50, 50)
    image(img1, 100, 100, 50, 50)
    
    
