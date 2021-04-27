from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import time
import eel

eel.init('WD')

@eel.expose
def detectEmotion():
    iterCount = 0
    emotionCounts={
        "Happy":0,
        "Sad":0,
        "Angry":0,
        "Neutral":0,
        "Surprise":0
    }
  
    iterLabel = ''
    face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    classifier =load_model('./Emotion_Detection.h5')

    class_labels = ['Angry','Happy','Neutral','Sad','Surprise']

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    print('called detect function in py:')
    while True:
       
        ret, frame = cap.read()
        labels = []
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h,x:x+w]
            roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)


            if np.sum([roi_gray])!=0:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi,axis=0)

   

                preds = classifier.predict(roi)[0]
                print("\nprediction = ",preds)
                label=class_labels[preds.argmax()]
                print("\nprediction max = ",preds.argmax())
                print("\nlabel = ",label)
                label_position = (x,y)
                cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
                if iterCount < 20:
                    if label == 'Angry':
                        emotionCounts["Angry"]+=1
                    elif label == 'Sad':
                        emotionCounts["Sad"]+=1
                    elif label == 'Happy':
                        emotionCounts["Happy"]+=1
                    elif label == 'Neutral':
                        emotionCounts["Neutral"]+=1
                    elif label == 'Surprise':
                        emotionCounts["Surprise"]+=1
                    iterCount+=1
              
            else:
                cv2.putText(frame,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
            print("\n\n")
            print('count:', iterCount)
            print('emotionCounts:', emotionCounts)
        cv2.imshow('Emotion Detector',frame)
        if iterCount >=20:
            break
            

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
   
    maxLabel =max(emotionCounts  , key=emotionCounts.get) 
    print('maxLabel:', maxLabel)
    return  maxLabel

eel.start('main.html')