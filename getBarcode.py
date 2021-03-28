import cv2
import numpy as np
from pyzbar.pyzbar import decode
import requests
import sys


def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        
        # cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        # print("Barcode: "+barcodeData +" | Type: "+barcodeType)
        return barcodeData

# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     decoder(frame)
#     cv2.imshow('Image', frame)
#     code = cv2.waitKey(10)
#     if code == ord('q'):
#         break



img = cv2.imread('./out.jpg', 0) 
img = cv2.flip(img, 1)
# cv2.imwrite('asfd.jpg', img)
barcode = decoder(img)

print("this is barcode: ", barcode)

response = requests.get("https://api.barcodelookup.com/v2/products?barcode={}&key=u7l14tt2dk5y13yjqp9vpfbvsxuqof".format(barcode))
if response.status_code == 200:
    print(response.json())
else:
    print("error")

sys.stdout.flush()
