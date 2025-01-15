#! usr/bin/env python3
import rospy 
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class Webcam:
    def __init__(self):
        rospy.init_node("webcam_node", anonymous=False)
        self.image_pub = rospy.Publisher("webcam_img", Image, queue_size= 10)
        self.capture = cv2.VideoCapture(0)                                      #ls /dev/video (숫자 확인)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.capture.set(cv2.CAP_PROP_FPS, 30)
        self.bridge = CvBridge()

    def main(self):
        _, img = self.capture.read()                                    # _ : 성공여부 true, false는 건너뛰고 img에 데이터를 넣어라
        cv2.namedWindow("video", cv2.WINDOW_NORMAL)
        cv2.imshow("video", img)
        cv2.waitKey(1)
        webcam_img_msg = self.bridge.cv2_to_imgmsg(img, "bgr8")

        self.image_pub.publish(webcam_img_msg)

    
if __name__ == "__main__":
    webcam = Webcam()
    try:
        while not rospy.is_shutdown():
            webcam.main()
    except rospy.ROSInterruptException:
        pass