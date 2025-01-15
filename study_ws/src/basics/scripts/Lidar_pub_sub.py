#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class Lidar:
    def __init__(self):
        rospy.init_node("Laidar_scan_node")
        self.sub = rospy.Subscriber("/scan", LaserScan, self.lidar_callback) # 1.토픽 명, 2. 토픽 타입, 3. 섭스크라이브한 데이터를 처리하는 함수공간)
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.rate = rospy.Rate(10)
        self.order = Twist()
    
    def publish(self):
        self.order.linear.x = 0.5
        self.pub.publish(self.order)
        self.rate.sleep()


    def lidar_callback(self, data):
        print(f"angle increasement = {data.angle_increment}")
        print(f"ranges = {data.ranges}")
        

def main():
    lidar = Lidar()
    # rospy.spin()

    while not rospy.is_shutdown():
        lidar.publish()

if __name__ == "__main__":
    main()
