#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
                                       #클래스 정의: 노드를 클래스로 정의하여 코드를 구조화
class Class_Name:                                            #1단계: 클래스 이름 정의 
    def __init__(self):                                     # 2단계: 클래스 초기화 및 초기 설정
        rospy.init_node("turtle_node")                                      # ROS 1단계(필수): 노드 이름 정의

        self.sub = rospy.Subscriber("/turtle1/pose", Pose, self.callback)   # ROS 2단계(필수): subscriber 설정

    def callback(self, msg):                                # 3단계 클래스 내 함수 설정
        print(f"msg: {msg}")                
        print(f"msg X:{ msg.x}")       
        print(f"msg Y: {msg.y}")
# 메인 함수 정의: ROS 노드를 실행 하기 위한 메인 함수
def main(): # 4단계: 메인 함수 정의
    class_name = Class_Name()   # Class_Name 클래스의 인스턴스 생성

    #rospy.spin() 함수를 호출하여 노드를 실행하고 메시지 수신을 계속 대기합니다. 
    rospy.spin()    # subscriber: 수신대기  
# 직접 실행 코드: 스크립트가 직접 실행될 때 main() 함수를 호출합니다. 

if __name__ =="__main__":   #5단계: 직접 실행 구문 정의
    main()