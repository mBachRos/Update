#!/usr/bin/env python

import sys
from swarm.msg import Detection
import Classes.receiver
import Classes.Json


while(True):
    Classes.receiver.background_controller(detection_data)
    Classes.Json.detInput2Detection(detection_data)
