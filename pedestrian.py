import cv2
object_cascade = cv2.CascadeClassifier("C:/Users/donny/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_fullbody.xml")

video = cv2.VideoCapture(0)

while{True}:
    ret,frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = object_cascade.detectMultiScale(gray, 1.2,3)

    for (x,y,w,h) in eyes:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0,255,0), 2)
    cv2.imshow("frame",frame)
    if(cv2.waitKey(25) == 32):
        break

video.release()
cv2.destroyAllWindows()