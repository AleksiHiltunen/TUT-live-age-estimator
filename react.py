import sys
sys.path.append("/home/aleksi/pynaoqi-python2.7-2.8.5.10-linux64-20181203_200915/lib/python2.7/site-packages")
import naoqi

animations = {
		"Happy":"joy",
		"Sad":"user",
		"Neutral":"group",
		"Disgust":"confirmation",
		"Anger":"hesitation",
		"Surprise":"anterior",
		"Fear":"self"
}

def main(ip, reaction):
	posture = naoqi.ALProxy("ALRobotPosture", ip, 9559)
	posture.goToPosture("Stand", 0.6)
	tts = naoqi.ALProxy("ALAnimationPlayer", ip, 9559)
	tts.runTag(animations[str(reaction)])
	posture.goToPosture("Stand", 0.6)

if __name__ == "__main__":
	ip = sys.argv[1]
	reaction = sys.argv[2]
	main(ip, reaction)
