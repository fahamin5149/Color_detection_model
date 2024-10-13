import cv2
from get_color_limit import get_limits
from PIL import Image

cap= cv2.VideoCapture(0)

yellow= [0,255,255] #Yellow in BGR
black = [0, 0, 1]
white = [255, 255, 255]


while True:
    ret, frame= cap.read()

    hsvimage= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower, upper= get_limits(white)

    # the function we are going to use in order to get a mask of all the features we need
    mask= cv2.inRange(hsvimage,lower,upper)

    # we are just converting our numpy array into pillow
    mask_= Image.fromarray(mask)
    
    # if we want the bounding box of <color> eg yellow pixels
    bbox= mask_.getbbox()

    if bbox is not None:
        x1,y1, x2,y2= bbox
        frame= cv2.rectangle(frame, (x1, y1),(x2,y2),4)

    cv2.imshow('frame', frame)

    # when q is pressed the frame will break
    if cv2.waitKey(33) & 0xFF ==ord('q'):
        break

cap.release()

cv2.destroyAllWindows()