# import the opencv library
import cv2
face_cascade = cv2.CascadeClassifier('/Users/bhumisehgal/Documents/whjr/PRO-C106-Student-Boilerplate-main/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/Users/bhumisehgal/Documents/whjr/PRO-C106-Student-Boilerplate-main/haarcascade_eye.xml')

# Define a video capture object
vid = cv2.VideoCapture(0)

while(True):
   
    # Capture the video frame by frame
    ret, frame = vid.read()
    grey= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.1, 5)

    eyes= eye_cascade.detectMultiScale(grey, 1.1, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    for (x,y,w,h) in eyes:
        cv2.rectangle(frame,(x,y), (x+w,y+h),(255,0,0),2)

    # Display the resulting frame
    cv2.imshow("Web cam", frame)
      
    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break
  
# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()