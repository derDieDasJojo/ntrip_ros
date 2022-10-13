#!/usr/bin/python3

import rospy

from nmea_msgs.msg import Sentence
from mavros_msgs.msg import RTCM
from rospy import Time
import datetime
from http.client import HTTPConnection
from base64 import b64encode
from threading import Thread


class nmea:
    def run(self):
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            self.publish()
            rate.sleep()

    def publish(self):
        now = datetime.datetime.utcnow()
        nmea_gga = self.nmea_gga
        #nmea_gga = "{}{}{}{}".format(self.ntc.nmea_gga,now.hour, now.minute, now.second)
        print("nmea_gga:") 
        print(nmea_gga) 
        nmea_sentence = Sentence()
        nmea_sentence.sentence = nmea_gga
        nmea_sentence.header.stamp = rospy.Time.now()
        nmea_sentence.header.frame_id = "odom"
        self.pub.publish(nmea_sentence)


    def __init__(self):
        rospy.init_node('nmea', anonymous=True)

        self.nmea_topic = rospy.get_param('~nmea_topic', 'nmea')

        self.nmea_gga = rospy.get_param('~nmea_gga')

        self.pub = rospy.Publisher(self.nmea_topic, Sentence, queue_size=10)

if __name__ == '__main__':
    c = nmea()
    c.run()

