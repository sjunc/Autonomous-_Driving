#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from time import *

class Limo_Stop:
    def __init__(self):
        rospy.init_node("Laidar_scan_node")
        self.sub = rospy.Subscriber("/scan", LaserScan, self.laser_callback) # 1.토픽 명, 2. 토픽 타입, 3. 섭스크라이브한 데이터를 처리하는 함수공간)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.rate = rospy.Rate(30)
        self.lidar_flag = False
        self.deg = 10
        self.cmd_vel_msg = Twist()
    
    def publish(self):
        self.cmd_vel_msg.linear.x = 0.5
        self.pub.publish(self.cmd_vel_msg)
        self.rate.sleep()


    def laser_callback(self, msg):
        num = 0                                                     # 함수가 실행 될 때마다 초기화 
        if (self.lidar_flag == False):
            self.degrees = [                    #radient 값으로 되어있어서 알기 힘드니 degree 값으로 바꾸는 과정
                (msg.angle_min + (i * msg.angle_increment))* 180/ 3.141592     # rostopic 에서 확인한 angle min -1.74
                for i, data in enumerate(msg.ranges)                          # enumerate 인덱스와 값을 포함하여 리턴 enumerate는 기본적으로 (index, value) 형식의 튜플을 반환하기 때문에 센서같은 정확해야하는 데이터 처리에 적합
            ]
            self.liar_flag = True

        for i, data in enumerate(msg.ranges):                                                  # 각도가 -10 이상 10 이하 이면서 거리값이 0이상 0.5m 이하일때 num + 1
            if (-self.deg < self.degrees[i] < self.deg and 0 < msg.ranges[i] < 0.5):           
                num += 1                                                                       

        if num < 20:
            self.cmd_vel_msg.linear.x = 0.3                                                   # 센서에서 garbage값이 들어올 수 있으므로 또 하나의 제어문으로 10 이하일 때만 전진
        else:
            self.cmd_vel_msg.linear.x = 0

        self.pub.publish(self.cmd_vel_msg)
        self.rate.sleep()
        # print(self.degrees)
        print(num)
        # print(self.lidar_flag)

if __name__ == "__main__":
    limo_stop = Limo_Stop()
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
