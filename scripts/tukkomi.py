#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

flag = 0

def cb(message):
    global flag
    if(message.data[:9] == "おかん" and flag == 0):
        print("コーンフレークやないかい")
        flag = 1
    elif(message.data[:9] == "おかん" and flag == 1):
        print("ほなコーフレークと違うかー")
        flag = 0
    elif(message.data[:9] == "おとん"):
        print("絶対ちゃうやろ、もうええわー、ありがとうございました")
    else:
        print("なんでやねん")

if __name__ == '__main__':
    print("特徴教えてよ")
    rospy.init_node('tukkomi')
    sub = rospy.Subscriber('funny_boke', String, cb)
    rospy.spin()
