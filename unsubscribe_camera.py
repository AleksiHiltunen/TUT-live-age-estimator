import sys
sys.path.append("/home/aleksi/pynaoqi-python2.7-2.8.5.10-linux64-20181203_200915/lib/python2.7/site-packages")
import naoqi

def main(ip, id):
	video = naoqi.ALProxy("ALVideoDevice", ip, 9559)
	return video.unsubscribe(id)

if __name__ == "__main__":
	ip = sys.argv[1]
	id = sys.argv[2]
	sys.exit(main(ip, id))
