import sys
sys.path.append("/home/aleksi/pynaoqi-python2.7-2.8.5.10-linux64-20181203_200915/lib/python2.7/site-packages")
import naoqi

def main(ip):
	id = "camera"
	video = naoqi.ALProxy("ALVideoDevice", ip, 9559)
	id = video.subscribeCamera(id, 0, 1, 11, 30)
	sys.stderr.write(id)

if __name__ == "__main__":
	ip = sys.argv[1]
	sys.exit(main(ip))
