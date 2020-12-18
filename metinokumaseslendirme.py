import pytesseract
import cv2
from gtts import gTTS
import os


def getText(img_yolu):
    img = cv2.imread(img_yolu)
    ims = cv2.resize(img, (960, 600))
    cv2.imshow("Seslendirilecek Resim", ims)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    file = open("okunanmetin.txt", "w+", encoding="utf-8")
    file.write("Dönüştürülen Metniniz: \n")
    file.close()
    file = open("okunanmetin.txt", "a", encoding="utf-8")
    text = pytesseract.image_to_string(img, lang="tur")
    print(text)
    file.write(text)
    file.write("\n")
    file.close()
    return text

tts = gTTS(getText("mrv.png"), lang="tr")
tts.save("seslendirme.mp3")
os.system("seslendirme.mp3")

