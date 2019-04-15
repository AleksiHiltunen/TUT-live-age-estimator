# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:44:40 2016

@author: agedemo
"""

import threading
import cv2
import GrabUnit
import subprocess
import os
import numpy as np
import json

DIR = os.path.dirname(os.path.realpath(__file__))

class GrabberThread(threading.Thread):

    def __init__(self, parent, params):

        threading.Thread.__init__(self)

        '''camId = params.getint("camera", "Id")

        camResolution = params.get("camera", "resolution")
        camResolution = camResolution.upper().split("X")
        camResolution = [int(x) for x in camResolution]
        print(("Using camera %d at resolution %s" % (camId, camResolution)))

        self.flipHor = params.getint("camera", "flip_horizontal")

        self.video = cv2.VideoCapture(camId)  # 0: Laptop camera, 1: USB-camera
        #self.video.set(3, camResolution[0])  # 1280 #1920 Default: 640
        #self.video.set(4, camResolution[1])  # 720  #1080 Default: 480
'''
        self.flipHor = params.getint("camera", "flip_horizontal")
        self.parent = parent

        #Initializing the video device of the robot
        process = subprocess.Popen("python /home/aleksi/TUT-live-age-estimator/subscribe_camera.py 192.168.43.161".split(), stdout=subprocess.PIPE)
        process.wait()

        print("Grabber Thread initialized...")

    def run(self):
        while not self.parent.isTerminated():

            #stat, frame = self.video.read()
            python2_cmd = "python /home/aleksi/TUT-live-age-estimator/get_frame.py 192.168.43.161 camera_0"
            process = subprocess.Popen(python2_cmd.split(), stdout=subprocess.PIPE)
            process.wait()
            #output, error = process.communicate()
            with open(os.path.join(DIR, "temp_img", "current_frame.json")) as file:
                data = json.load(file)
                d = data["data"]
                frame = np.array(d)
                frame = frame.astype(np.uint8)
                print(frame)
                print(type(frame))
                print(len(frame))
                print(len(frame[0]))
                print(type(frame[0][0][0]))

            if frame is not None and not self.parent.isTerminated():
                if self.flipHor:
                    frame = frame[:, ::-1, ...]

                unit = GrabUnit.GrabUnit(frame)

                self.parent.putUnit(unit)

