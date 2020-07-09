from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
import cv2

window_name = "QR Code Scanner"
data_file = "qrcodedata.txt"

# Initialize the video stream
print("Starting video stream...")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

csv = open(data_file, "w")
frame = vs.read()
frame = imutils.resize(frame, width=400)

barcodes = pyzbar.decode(frame)
cv2.imshow(window_name, frame)

for barcode in barcodes:
    (x, y, w, h) = barcode.rect
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # make border green

    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type
    print("barcode data: " + barcodeData)
    print("barcode type: " + barcodeType)

    text = "{}".format(barcodeData)
    cv2.putText(frame, '', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    csv.write("{}\n".format(barcodeData))
    csv.flush()

    print("Got the barcode data: " + barcodeData)
    break
print("Stoping video stream...")
cv2.destroyWindow(window_name)
csv.close()
print("Done!")
