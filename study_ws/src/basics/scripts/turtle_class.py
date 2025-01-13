#! /usr/bin/env python3  
import rospy                                # rostopic list 로 받아야할 항목들 확인
from geometry_msgs.msg import Twist         # rostopic info turtle1/cmd_vel 를 통해 데이터 타입 파악  
from turtlesim.msg import Pose              # rostopic info turtle1/pose 를 통해 데이터 타입 파악 
                                            # 클래스 정의: 노드를 클래스로 정의하여 코드를 구조화
                                            
class Pub_Sub_Turtle:                                               # 1단계: 클래스 이름 정의 
    def __init__(self):                                             # 2단계: 클래스 초기화 및 초기 설정
        rospy.init_node("turtle_pubsub_node")                                      # ROS 1단계 (필수): 노드 이름 정의
        rospy.Subscriber("/turtle1/pose", Pose, self.callback)                     # ROS 2단계 (필수): 그냥 이렇게 써도 됨.
        self.pub = rospy.Publisher('/turtle1/cmd_vel',Twist ,queue_size=1)         # ROS 2단계 (필수)  
        self.rate = rospy.Rate(10)                                                 # ROS 2-1단계 (옵션): 발행 주기 설정
        self.msg = Twist()                 # 메시지 타입 설정 및 초기화

    def callback(self, msg):                                        # 3단계 클래스 내 함수 설정
        print(f"Turtle Pub, Sub: {msg}")                            
        #print(f"msg X:{ msg.x}")       
        #print(f"msg Y: {msg.y}")
    
    def publish_data(self):
        self.pub.publish(self.msg)                                                # ROS 3단계(필수): 퍼블리셔 - 퍼블리시 실행

        self.msg.linear.x += 0.01 
        self.msg.angular.z += 0.50
        # 현재 메시지와 linear.x 값 출력
        # print(f"msg:{self.msg}") # 출력: 메시지
        self.rate.sleep()  #ROS 3-1단계(옵션): 퍼블리셔 - 주기 실행

# 메인 함수 정의: ROS 노드를 실행 하기 위한 메인 함수
    
def main():                                                         # 4단계: 메인 함수 정의
    pub_sub = Pub_Sub_Turtle() # pub_sub 이름의 클래스 인스턴스 생성

    while not rospy.is_shutdown():                              
        pub_sub.publish_data()                        
        

if __name__=="__main__":
    main()
    
