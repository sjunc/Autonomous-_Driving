#! usr/bin/env python3
import rospy 
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
import numpy as np

class Gray_scale:
    def __init__(self):
        rospy.init_node("image_node")
        self.image_pub = rospy.Publisher("gray_img", Image, queue_size= 10)
        self.rate = rospy.Rate(10)
    def image(self):
        gray = np.array(
            [
            [0, 225, 127,255, 0, 255, 127, 255, 127, 255,0, 225, 127,255, 0, 255, 127, 255, 127, 255],
            [255, 127, 255, 127, 255, 255, 127, 255, 127, 255,0, 225, 127,255, 0, 255, 127, 255, 127, 255],
            [127, 255, 0, 255, 127, 255, 127, 255, 127, 255,0, 225, 127,255, 0, 255, 127, 255, 127, 255],
            [255, 127, 255, 127, 255, 255, 127, 255, 127, 255,0, 225, 127,255, 0, 255, 127, 255, 127, 255],
            [0, 225, 127,255, 0, 255, 127, 255, 127, 255,0, 225, 127,255, 0, 255, 127, 255, 127, 255],
        ], np.uint8,
        )

        bridge = CvBridge()
        ros_image = bridge.cv2_to_imgmsg(gray)
        gray_image = bridge.imgmsg_to_cv2(ros_image)
        cv2.imshow("Image", gray_image)
        cv2.waitKey(1)

        self.image_pub.publish(ros_image)
        self.rate.sleep()

def main():
    gray_scale = Gray_scale()
    while not rospy.is_shutdown():
        gray_scale.image()

if __name__ == "__main__":
    main()