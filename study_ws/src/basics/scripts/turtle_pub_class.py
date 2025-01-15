#! /usr/bin/env python3  
import rospy
from geometry_msgs.msg import Twist         # rostopic info turtle1/cmd_vel 를 통해 데이터 타입 파악  

#ROS노드 초기화 
class Publish_turtle:
    def __init__(self):   
        rospy.init_node("turtle_pub_node")

        self.pub = rospy.Publisher('turtle1/cmd_vel',Twist ,queue_size=1)    # ROS 2단계 (필수)  
        self.rate = rospy.Rate(10)  
        self.msg = Twist()      

    def publish(self):
        self.pub.publish(self.msg)

        self.msg.linear.x += 0.01 
        self.msg.angular.z += 0.01
        # 현재 메시지와 linear.x 값 출력
        print(f"msg:{self.msg}") # 출력: 메시지
        self.rate.sleep()  #ROS 3-1단계(옵션): 퍼블리셔 - 주기 실행

def main():
    pub_turtle = Publish_turtle()
    while not rospy.is_shutdown():                              
        pub_turtle.publish()                        
        

if __name__=="__main__":
    main()
    
