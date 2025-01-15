#! usr/bin/env python3
import rospy 
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
import numpy as np

class Color:
    def __init__(self):
        rospy.init_node("color_image_node", anonymous=False)
        self.image_pub = rospy.Publisher("color_img", Image, queue_size= 10)
        self.rate = rospy.Rate(10)
        self.bridge = CvBridge()

    def image(self):
        blue = [255, 0, 0]
        green = [0, 255, 0]
        red = [0, 0, 255]
        purple = [255, 0, 255]
        sky = [255, 255, 0]
        yellow = [0, 255, 255]
        random = [244, 234, 216]

        color = blue

        color_img = np.array(
            [
                [color, color, color, color, color, color, color, color, color, color, color, color, ],
                [color, color, color, color, color, color, color, green, color, color, color, color ],
                [color, color, color, red, color, color, color, color, color, color, color, color ],
                [color, yellow, color, color, random, color, color, color, color, color, color, color ],
                [color, color, purple, color, sky, color, color, color, color, color, color, color ],
                [color, color, color, color, color, color, color, color, color, color, color, color ],
                
            ], np.uint8
        )

        bridge = CvBridge()                         #python과 ros 사이의 이미지 출력방식 연결 다리 클래스
        ros_image = self.bridge.cv2_to_imgmsg(color_img, "bgr8")

        self.image_pub.publish(ros_image)
        self.rate.sleep()

def main():
    color = Color()
    while not rospy.is_shutdown():
        color.image()

if __name__ == "__main__":
    main()