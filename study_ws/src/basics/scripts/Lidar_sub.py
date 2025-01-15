#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

class Lidar:
    def __init__(self):
        rospy.init_node("Laidar_scan_node")
        sub = rospy.Subscriber("/scan", LaserScan, self.lidar_callback) # 1.토픽 명, 2. 토픽 타입, 3. 섭스크라이브한 데이터를 처리하는 함수공간)
        
    def lidar_callback(self, data):
        print(f"angle increasement = {data.angle_increment}")
        print(f"ranges = {data.ranges}")
        

def main():
    laidar_scan = Lidar()
    rospy.spin()

if __name__ == "__main__":
    main()

#                                       #ROS 노드 초기화, 노드이름 "sub_node"로 지정
#rospy.init_node("scan")                              # ROS 1단계(필수): 노드 이름 정의 
#
#def callback(data):                     #콜백함수(callback)정의 : 이 함수는 메시지를 수신할 때 호출됩니다. 
#    #print(f"원하는 데이터: {data.intensities}")
#    print(f"원하는 데이터: {data.ranges}")
##ROS Subscriber 설정
#sub = rospy.Subscriber("/scan", LaserScan, callback)     # ROS 2단계(필수): subscriber 설정
#
##rospy.spin() 함수를 호출하여 노드를 실행하고 메시지 수신을 계속 대기합니다. 
#rospy.spin()    # subscriber: 수신대기
