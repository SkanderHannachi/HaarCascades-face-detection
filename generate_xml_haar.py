"""Programme qui génère des images negatives capturée par la logitech.Il génère également le fichier text et effectue un traitement de base sur les fichiers.
Les étapes pour générer un .xml pour le haar cascades : 

1/ Générer les 5000 (400X400) négatives.

2/ génerer le fichier bg.txt

3/ Creer un dossier data et un dossier info 

4/ capturer une image positive

5/  on génère 90% du nombre d'images positives.
>opencv_createsamples -img positive.png -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 maxzangle 0.5 -num 5000 

6/Creer le vecteur de données avec la commande : 
>opencv_createsamples -info info/info.lst -num 4000 -w 20 -h 20 -vec positives.vec 

8/Lancer la commande : 
>opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 3600 -numNeg 4000 -numStages 10 -w 20 -h 20


"""

import numpy as np
import random as rdm 
import time
import cv2
import os


DIRR = "/home/skndr-ros/Desktop/recon"
NOMBRE_TRAIN = 100
DIM = (400,400)
cap = cv2.VideoCapture(1)


def tri(ls) :
    rr = []
    for elem in ls : 
        if elem[:3] == 'neg' :
            rr.append(elem)
    return rr         

def process() :
    ls = os.listdir(DIRR) 
    L  = tri(ls)
    fichier = open('bg.txt','w')
    for f in L : 
        ch = 'neg'+'/'+f+'\n'
        fichier.write(ch)
    fichier.close()

def resiz() : 
    cyln = cv2.imread('cylind.png')
    resized = cv2.resize(cyln,(100,100),interpolation = cv2.INTER_AREA)
    cv2.imwrite("cylinre.png", resized)
    
    
def capture() : 
    i=0
    while(i<=NOMBRE_TRAIN):
        i+=1
    # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray,DIM,interpolation = cv2.INTER_AREA)
        cv2.imshow('frame',resized)
        print(i)
        cv2.imwrite("neg"+str(i)+".png", resized)
        time.sleep(0.01)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            des()
            break
    cap.release()
    cv2.destroyAllWindows()
def main() : 
    #capture()
    process()
if __name__ == "__main__" : 
    main()

