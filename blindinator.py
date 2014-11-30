from SimpleCV import *
#import usb, sys
#sys.path.append("..")
#from arduino.usbdevice import ArduinoUsbDevice

#try:
#        theDevice = ArduinoUsbDevice(idVendor=0x16c0, idProduct=0x05df)
#except:
        #sys.exit("Blindinator Not Found")

def point():
        if lit:
                s="*"
        else:
                s="."
        s = s+(chr(ord('0')+(180-x)))+(chr(ord('0')+(180-y)))
        #print s
        #for c in s:
        #        try:
        #                theDevice.write(ord(c))
        #        except:
        #                print "warning: device write error"

def up():
        global y
        if(y>0):
                y=y-1
        point()
def down():
        global y
        if(y<180):
                y=y+1
        point()
def left():
        global x
        if(x>0):
                x=x-1
        point()
def right():
        global x
        if(x<180):
                x=x+1
        point()
def center():
        global x,y
        x=90
        y=90
        point()
def laser(isOn):
        global lit
        lit=isOn
        point()

def Look():
        quitting = False
        frame = 0
        cam = Camera()
        disp = Display()
        print cam.getImage().listHaarFeatures()
        #segment = HaarCascade("nose.xml") eh. slow
        #segment = HaarCascade("eye.xml") pretty good
        #segment = HaarCascade("lefteye.xml") frequently gets right eye
        #segment = HaarCascade("left_eye2.xml") slow/inaccurate
        #segment = HaarCascade("right_eye.xml")
        segment = HaarCascade("eye.xml")
        while not quitting:
                #print frame
                frame = frame+1
                
                img = cam.getImage()#.colorDistance(Color.ORANGE)

                #promising for laser finding
        #        blobs = img.findBlobs(minsize=10,maxsize=250) # get the largest blob on the screen
        #        if blobs:
        #                for b in blobs:
        #                       if b.isCircle(tolerance=0.5):
        #                               b.draw()                      
                                        #avgcolor = np.mean(blobs[-1].meanColor()) #get the average color of the blob

                #sucks
        #        circs = img.findCircle(canny=200,thresh=350,distance=10)
        #        if circs:
        #                for c in circs:
        #                        c.draw()
                                
                autoface = img.findHaarFeatures(segment)
                if ( autoface is not None ):
                    autoface.draw()
                
                img.save(disp)

                disp.checkEvents()
                #if disp.pressed[ord('q')]:
                #        quitting=True
                #elif disp.pressed[ord('w')]:
                #        up()
                #elif disp.pressed[ord('a')]:
                ##        left()
                #elif disp.pressed[ord('s')]:
                #        right()
                #elif disp.pressed[ord('z')]:
                #        down()
                #elif disp.pressed[ord('c')]:
                #        center()
                #elif disp.pressed[ord('0')]:
                #        laser(False)
                #elif disp.pressed[ord('1')]:
                #        laser(True)
                #elif disp.pressed[ord('p')]:
                #        print "x="+str(x)+", y="+str(y)
                
                #for x in range(ord('a'),ord('z')):
                #        if disp.pressed[x]==1:
                #                print "K="+chr(x)

                #k = ord(msvcrt.getch()) if msvcrt.kbhit() else 0
                #if k>0:
                #        print "key hit "+k
                #if k=='q':
                #        quitting=True

lit=False
center()
point()
Look()
exit()
