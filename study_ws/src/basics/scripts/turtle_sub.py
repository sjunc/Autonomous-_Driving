#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
                                       #ROS 노드 초기화, 노드이름 "sub_node"로 지정
rospy.init_node("turtle_node")                              # ROS 1단계(필수): 노드 이름 정의 

def callback(msg):                     #콜백함수(callback)정의 : 이 함수는 메시지를 수신할 때 호출됩니다. 
    #print(f"msg: {msg}")                                   # Ros 3단계(필수): subscriber - 콜백 함수 설정 # 출력: 메세지
    print(f"원하는 데이터 X:{msg.x}")     # 출력: 메세지 항목(데이터)
    print(f"원하는 데이터: {msg.linear_velocity}")

#ROS Subscriber 설정
#"/counter" 토픽에서 Int32 메시지를 수신하고, 콜백함수 호출
sub = rospy.Subscriber("/turtle1/pose", Pose, callback)     # ROS 2단계(필수): subscriber 설정

#rospy.spin() 함수를 호출하여 노드를 실행하고 메시지 수신을 계속 대기합니다. 
rospy.spin()    # subscriber: 수신대기  