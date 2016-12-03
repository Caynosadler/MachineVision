from SimpleCV import Image, Camera, Display, Color

cam = Camera()
scaler = 0.5
previous = cam.getImage().scale(scaler)
disp = Display((680, 480))
sz = previous.width/10

while disp.isNotDone():
    current = cam.getImage().scale(scaler)
    motion = current.findMotion(previous, sz, method='HS')
    motion.draw(color=Color.RED, width=3)
    current.save(disp)
    previous = current
        
