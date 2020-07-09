#! /usr/bin/env python3

from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
import cv2

window_name = "QR Code Scanner"
data_file = "codedata.txt"

# Initialize the video stream
print("[INFO] Starting stream")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

csv = open(data_file, "w")

found = set()
found.clear()

while len(found) == 0:
    # Grab frame from threaded video and resize to 400px
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    # get all the barcodes from frame
    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        # If we already got the barcode at least once successfully, quit the program

        if len(found) > 0:
            break

        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # make border green

        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        print("barcode data: " + barcodeData)
        print("barcode type: " + barcodeType)

        text = "{}".format(barcodeData)
        cv2.putText(frame, '', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        if barcodeData not in found:
            csv.write("{}\n".format(barcodeData))
            csv.flush()

            found.add(barcodeData)
            break

    cv2.imshow(window_name, frame)
    key = cv2.waitKey(1) & 0xFF

    # If user press "Q" then quit the program
    if key == ord("q"):
        cv2.destroyWindow(window_name)
        break

print("[INFO] Cleaning up")
csv.close()
