
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import tkinter
import csv

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
	help="path to output CSV file containing barcodes")
args = vars(ap.parse_args())

print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

csv = open(args["output"], "w")
found = set()

while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
	
	barcodes = pyzbar.decode(frame)

	for barcode in barcodes:
		(x, y, w, h) = barcode.rect
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type

		text = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

		if barcodeData not in found:
			csv.write("{},{}\n".format(datetime.date.today(),
				barcodeData))
			print("student id: "+barcodeData+" "+str(datetime.date.today()))
			output = barcodeData
			csv.flush()
			found.add(barcodeData)
 	
	cv2.imshow("Barcode Scanner", frame)
	quit = cv2.waitKey(1) & 0xFF

	if quit == ord("q"):
		break

"""overallarr = []
with open('barcodes.csv') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
    	overallarr.append([row[1], row[0]])
top = Tk()
class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Attendence Register")        
        text = Text(master, width = 53, fg = 'black')
        for counter in overallarr:
            text.insert(END, counter[0])
            text.insert(END, "\n")
            text.insert(END, counter[1])
            text.insert(END, "\n")
        text.pack()
        
gui = GUI(top)
top.mainloop()
"""
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()