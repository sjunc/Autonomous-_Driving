#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import CompressedImage

class Camera:
    def __init__(self):
        rospy.init_node("image_node")
        sub = rospy.Subscriber("/camera/color/image_raw/compressed", CompressedImage, self.camera_callback) # 1.토픽 명, 2. 토픽 타입, 3. 섭스크라이브한 데이터를 처리하는 함수공간)
        
    def camera_callback(self, data):
        print(f"camera data = {data}")
        

def main():
    camera = Camera()
    rospy.spin()

if __name__ == "__main__":
    main()


