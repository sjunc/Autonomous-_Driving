#! /usr/bin/env python3                                     
                                                            # 쉬뱅 shebang 파이썬 언어로 구동되는 걸 컴파일러에게 다시한번 언급
import rospy                                                # rospy 임포트
from std_msgs.msg import Int32                              # censor나 수많은 메세지 중 int32 가져옴

rospy.init_node('topic_publisher')                          # init(초기화) 'topic_publisher'란 이름으로 node를 초기화, 정의 시켰음. 

pub = rospy.Publisher('counter', Int32, queue_size=1)                  # publish 기능을 가진 'counter'는 Int32데이터를 가진 counter란 이름의 데이터를 전달

rate = rospy.Rate(2)                                        # 초당 2번 전달

count = 0                                                   # 변수초기화

while not rospy.is_shutdown():                              # rospy가 꺼지지 않으면 반복
    pub.publish(count)                                      # pub의 publish 기능을 사용. 0부터 시작
    count += 1                                              # 1씩 증가
    rate.sleep()                                            # 코드에 지연 추가 


# ~/study_ws    $ catkin_make        C++로 빌드를 진행
# ~/study_ws    $ source devel/setup.bash           source 적용시켜 주겠다.   첫번째 이유 내가 사용할 워크 스페이스 안에 있는 패키지를 사용하기 위한 적용 단계
#에러발생
'''~/study_ws$ rosrun basics topic_subscriber.py
[rosrun] Couldn't find executable named topic_subscriber.py below /home/user/study_ws/src/basics
[rosrun] Found the following, but they're either not files,
[rosrun] or not executable:
[rosrun]   /home/user/study_ws/src/basics/scripts/topic_subscriber.py
'''
# ls -al 을 실행하면 권한이 없음을 알 수 있음 x가 없고 초록색이 아님. 
# 권한이 없음. chmod를 통해 x 즉 실행 권한을 부여주어야함.                      두번째 이유
#~/study_ws/src/basics/scripts   $ chmod 777 topic_publisher.py    해결방안: 실행가능한 최고 권한을 부여하였음

