#importing modules
import cv2
import pytesseract

#you need to install pytesseract app on your device , windowsInstaller.exe for same is given in this project
#install pytesseract and note down where its installed
#in my case its installed in C:\Program Files\Tesseract-OCR\tesseract.exe


#adding tesseract.exe file
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img=cv2.imread("test2.png")
img=cv2.cvtColor(img,cv2
                 .COLOR_BGR2RGB)
#shows text recognised in terminal
print(pytesseract.image_to_string(img))

hImg,wImg=img.shape[:2]

#putting rectangles and text on image
boxes=(pytesseract.image_to_boxes(img))
for b in boxes.splitlines():
    #print(b)
    b=b.split(" ")
    print(b)
    x,y,w,h =int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(255,255,0),2)
    cv2.putText(img,b[0],(x,hImg-y-30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))
cv2.imshow("Result",img)
cv2.waitKey(0)