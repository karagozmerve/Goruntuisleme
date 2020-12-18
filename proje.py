from tkinter import *
import pytesseract
import cv2
from gtts import gTTS
from PIL import ImageTk, Image
from tkinter import filedialog
import pyttsx3
import os
import numpy as np
import requests
from tkinter.ttk import *


url ="http://192.168.1.103:8080//shot.jpg"

root = Tk()
root.geometry('700x500')
root.title('Görüntüden Metin Okuma')
yazi = Label(root,text = "Merhaba Seslerin Görüntüsüne Hoşgeldiniz :)").place(x = 250, y = 0)

def oku():
    filename = filedialog.askopenfilename()
    img = Image.open(filename)
    image=img.copy()
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    file = open("donusturuldu.txt", "w+", encoding="utf-8")
    file.write("Dönüştürülen Metniniz: \n")
    file.close()
    file = open("donusturuldu.txt", "a", encoding="utf-8")
    text = pytesseract.image_to_string(image, lang="tur")
    file.write(text)
    file.write("\n")
    file.close()
    tts = gTTS(text=text, lang="tr")
    tts.save("seslendirme.mp3")
    os.system("seslendirme.mp3")



def cikis():
    import sys; sys.exit()

def canlikamera():
    img = requests.get(url)
    img = np.array(bytearray(img.content), dtype=np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (640, 480))
    cv2.imshow("Kamera", img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = pytesseract.image_to_string(img, lang="tur")
    print(result)
    engine = pyttsx3.init()
    engine.say(result)
    engine.runAndWait()
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()


sto = Style()

#configure style
sto.configure('W.TButton', font= ('Arial', 10),width=20,foreground='Black')

button1 = Button(root, text="Resimden Metni Oku", style='W.TButton', command=oku).place(x=300,y = 340)
button2 = Button(root,text="Çıkış",style='W.TButton',command=cikis).place(x=300,y = 420)
button3=Button(root,text="Kameradan Metni Oku",style='W.TButton',command=canlikamera).place(x=300,y = 380)
root.mainloop()