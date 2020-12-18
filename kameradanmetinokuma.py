import cv2
import numpy as np
import requests
import pytesseract
from PIL import Image
import pyttsx3

url ="http://192.168.1.103:8080//shot.jpg"

while True:
    img=requests.get(url)
    img=np.array(bytearray(img.content),dtype=np.uint8)
    img=cv2.imdecode(img,cv2.IMREAD_COLOR)
    img=cv2.resize(img, (640,480))
    cv2.imshow("Kamera",img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = pytesseract.image_to_string(img, lang="tur")
    print(result)
    engine = pyttsx3.init()
    engine.say(result)
    engine.runAndWait()
    if cv2.waitKey(1)==27:
        break


cv2.destroyAllWindows()
