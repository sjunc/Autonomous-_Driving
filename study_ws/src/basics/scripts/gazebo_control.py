#! /usr/bin/env python3  
import rospy                                # rostopic list 로 받아야할 항목들 확인
from geometry_msgs.msg import Twist         # rostopic info turtle1/cmd_vel 를 통해 데이터 타입 파악  
from gazebo_msgs.msg import ModelState              # rostopic info turtle1/pose 를 통해 데이터 타입 파악 
                                            # 클래스 정의: 노드를 클래스로 정의하여 코드를 구조화
                                            
class Control_Turtle:                                               # 1단계: 클래스 이름 정의 
    def __init__(self):                                             # 2단계: 클래스 초기화 및 초기 설정
        rospy.init_node("turtle_control_node")                                     # ROS 1단계 (필수): 노드 이름 정의
        self.sub = rospy.Subscriber("/turtle1/pose", ModelState, self.callback)          # ROS 2단계 (필수)
        self.pub = rospy.Publisher("/turtle1/cmd_vel",Twist ,queue_size=1)         # ROS 2단계 (필수)  
        self.rate = rospy.Rate(10)                                                 # ROS 2-1단계 (옵션): 발행 주기 설정
        self.msg = Twist()                 # 메시지 타입 설정 및 초기화
        self.state= ModelState()                 # 메시지 타입 설정 및 초기화, 오른쪽의 데이터 형식으로(같은 데이터 모양) pose에 저장 
        ## self.x = 0
        ## self.y = 0           같은 형식으로 초기화 해줄 필요가 있기 때문에 위에 self.pose = Pose()가 맞음

    def callback(self, data):                                        # 3단계 클래스 내 함수 설정
        self.state.pose.position = data
        ## self.x = data.x                          내가 작성한 분분
        ## self.y = data.y
        #print(f"Turtle Pub, Sub: {data}")                            
        print(f"msg X: {data.x}")       
        print(f"msg Y: {data.y}")
       
    def publish_data(self):
        
        if(2.0< self.state.pose.position.x <9.0 and 2.0< self.state.pose.position.z <9.1):
            self.state.pose.position.x = 1.0
            self.state.pose.position.z = 6.0        #데이터가 실수형이므로 0.0으로 표현함
        else:
            self.state.pose.position.x = 10.0
            self.state.pose.position.x = 11.0
        # 현재 메시지와 linear.x 값 출력
        # print(f"msg:{self.msg}") # 출력: 메시지
        self.pub.publish(self.msg)                                                # ROS 3단계(필수): 퍼블리셔 - 퍼블리시 실행
        self.rate.sleep()                                                         # ROS 3-1단계(옵션): 퍼블리셔 - 주기 실행

# 메인 함수 정의: ROS 노드를 실행 하기 위한 메인 함수
    
def main():                                                         # 4단계: 메인 함수 정의
    control_turtle = Control_Turtle() # pub_sub 이름의 클래스 인스턴스 생성

    while not rospy.is_shutdown():                              
        control_turtle.publish_data()                        
        

if __name__=="__main__":
    main()
    
