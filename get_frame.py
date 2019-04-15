import sys
sys.path.append("/home/aleksi/pynaoqi-python2.7-2.8.5.10-linux64-20181203_200915/lib/python2.7/site-packages")
import naoqi
import numpy as np
import os
import json

DIR = os.path.dirname(os.path.realpath(__file__))

def main(ip, id):
	video = naoqi.ALProxy("ALVideoDevice", ip, 9559)

	w = 320
	h = 240
	result = video.getImageRemote(id)
	'''return result[6]'''
	image = np.zeros((h, w, 3), np.uint8)
	values = map(ord, list(result[6]))
	i = 0
	for y in range(0, h):
		for x in range(0, w):
			image.itemset((y, x, 0), values[i+0])
			image.itemset((y, x, 1), values[i+1])
			image.itemset((y, x, 2), values[i+2])
			i += 3

	'''Image is written into a json file so that it can be retrieved in python3'''
	image = image.tolist()
	data = {}
	with open(os.path.join(DIR, "temp_img", "current_frame.json"), 'w') as file:
		file.truncate()
		data["data"] = image
		json.dump(data, file)

	return

if __name__ == "__main__":
	ip = sys.argv[1]
	id = sys.argv[2]
	sys.exit(main(ip, id))
