import numpy as np
import argparse
import cv2

#variables

appara = argparse.ArgumentParser()
appara.add_argument("-i", "--image", help = "path to the image")
args = vars(appara.parse_args())

# load the image
image = cv2.imread(args["image"])

boundaries = [
        ([229, 180, 68],[247, 231, 204]),
	([102, 102, 102],[130,158,189]),
	([0,0,0], [255,255,0]),
	([253,0,255],[255,0,255])
    ]


for (lower, upper) in boundaries:
	
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
