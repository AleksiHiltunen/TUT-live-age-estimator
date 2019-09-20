import sys
sys.path.append("/home/aleksi/pynaoqi-python2.7-2.8.5.10-linux64-20181203_200915/lib/python2.7/site-packages")
import naoqi
import random

lines =	{
	"Happy":["I like your smile!", "You look happy", "He hee", "Being happy is the best!"],
	"Sad":["Don't be sad", "Are you alright?", "What's up?"],
	"Anger":["Why are you angry?", "Did I say something wrong?"],
	"Surprise":["Surprise!"],
	"Fear":["Don't be afraid", "Nothing to worry about"],
	"Disgust":["Is it me that is disgusting?", "Why are you looking so disgusted?"],
	"Neutral":[" "]
	}

def main(ip, reaction):
	tts = naoqi.ALProxy("ALTextToSpeech", ip, 9559)
	tts.say(random.choice(lines[reaction]))

if __name__ == "__main__":
	ip = sys.argv[1]
	reaction = sys.argv[2]
	main(ip, reaction)
