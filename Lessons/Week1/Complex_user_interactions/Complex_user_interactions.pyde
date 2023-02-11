x = 100
y = 100
speed = 3
speed_fast = 6
color_r = 0

w = 0
a = 0
s = 0
d = 0
shift = 0

def setup():
    size(900, 900)

def draw():
    global x, y, w, a, s, d, shift, color_r
    
    # 1. Clear the previous frame
    background(0, 0, 0)
    
    # 2. Move the objects and do calculations
    use_speed = speed
    if shift == 1:
        use_speed = speed_fast
    
    change_in_x = (a * use_speed * -1) + (d * use_speed)
    change_in_y = (w * use_speed * -1) + (s * use_speed)
    x = x + change_in_x
    y = y + change_in_y
    
    # 3. Draw the objects
    fill(color_r, 50, 150)
    ellipse(x, y, 50, 50)

def keyPressed():
    global w, a, s, d, shift
    
    if keyCode == 16:
        shift = 1
        return
    
    if type(key) == type(1):
        return
    
    if key.lower() == "w":
        w = 1
    elif key.lower() == "s":
        s = 1
    elif key.lower() == "a":
        a = 1
    elif key.lower() == "d":
        d = 1
        
def keyReleased():
    global w, a, s, d, shift
    
    if keyCode == 16:
        shift = 0
        return
    
    if type(key) == type(1):
        return
    
    if key.lower() == "w":
        w = 0
    elif key.lower() == "s":
        s = 0
    elif key.lower() == "a":
        a = 0
    elif key.lower() == "d":
        d = 0
        
def mouseWheel(event):
    global color_r
    if event.getCount() > 0:
        color_r = 255
    else:
        color_r = 0
        
def mousePressed():
    if mouseButton == LEFT:
        print("You left clicked")
    elif mouseButton == RIGHT:
        print("You right clicked")
        
        
        
        
        
        
        
