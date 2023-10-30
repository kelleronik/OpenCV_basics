import cv2                                                                              #импорт библиотеки OpenCV

faceCascade= cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")     #выбор классификатора Хаара для лиц в анфас
img = cv2.imread('Resources/lena.png')                                                  #создание объекта img с использованием команды чтения
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                                          #перевод изображения в оттенки серого

faces = faceCascade.detectMultiScale(imgGray,1.1,4)                                     #создание объекта, содержащего лица

for (x,y,w,h) in faces:                                                                 #рисование обводящих прямоугольников для лиц
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Result", img)                                                               #вывод результата
cv2.waitKey(0)                                                                          #команда для того, чтобы изображение не закрывалось