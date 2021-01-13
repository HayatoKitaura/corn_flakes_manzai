#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy
import sys
from std_msgs.msg import String

rospy.init_node('boke')                                # ノード名「count」に設定
pub = rospy.Publisher('funny_boke', String, queue_size=10)  # パブリッシャ「count_up」を作成
rate = rospy.Rate(10)                                   # 10Hzで実行

input_line = ""

print("うちのおかんがな、好きな朝ごはんあるらしいねん")
print("でも名前忘れたらしくてね")

while "ありがとうございました" not in input_line:
    print("ボケてください↓")

    input_line = sys.stdin.readline()

    pub.publish(input_line)
    rate.sleep()
