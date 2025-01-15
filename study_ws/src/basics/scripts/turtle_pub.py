#! /usr/bin/env python3  
import rospy
from geometry_msgs.msg import Twist         # rostopic info turtle1/cmd_vel 를 통해 데이터 타입 파악  

#ROS노드 초기화 
rospy.init_node("turtle_pub_node")                              # ROS 1단계(필수) : 노드 이름 설정

pub = rospy.Publisher('turtle1/cmd_vel',Twist ,queue_size=1)    # ROS 2단계 (필수) : 퍼블리셔 설정

rate = rospy.Rate(10)                                           # ROS 2-1단계(옵션): 발행 주기 설정  
# Twist 메시지 타입의 메시지 객체를 생성하고 초기화  
msg = Twist()      #메시지 타입 설정 및 초기화, 숏컷  

while not rospy.is_shutdown():                              
    pub.publish(msg)                                            # ROS 3단계  퍼블리셔 - 퍼블리시 실행                          
    msg.linear.x += 0.01 # 메시지 항목(linear.x) - 데이터 값변경
    #msg.linear.y += 0.01
    msg.angular.z += 0.01
    # 현재 메시지와 linear.x 값 출력
    # print(f"msg:{msg}")
    print(f"msg:{msg.linear.x}") # 출력: 메시지

    # 지정한 발행 주기에 따라 슬립
    rate.sleep()  #ROS 3-1단계(옵션): 퍼블리셔 - 주기 실행