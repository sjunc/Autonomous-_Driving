# Publisher & Subscriber
### Node
Ros 어플리케이션의 독립적인 실행 단위
### Publisher
메세지(데이터)를 발행하는 노드  
특정 주제(Topic)에 대한 메세지를 생성하여 해당 주제를 구독하는 다른 노드에 전송  
메세지 타입(int32), 주제 이름, 발행 빈도(quesize) 등을 정의  
### Subscriber
메세지를 구독하는 노드  
PUBLISHER 가 발행한 메세지를 해당 주제(Topic)를 구독하여 받아들이는 역할  
받은 메세지를 처리하고, 필요한 경우 다른 노드로 메세지를 전송하여 로봇 제어, 상태 모니터링, 데이터 분석등을 수행   
  
Publisher  
0.shebang & import  
1. init_node 설정 (node 이름 설정)  
2. rospy.Publisher(이름, 타입, 발행 빈도)  
3. rospy.Rate 설정 - 빈도  
  
#! /usr/bin/env python3  
rospy.init("이름")  
pub = rospy.Publisher('counter', Int32, queue_size =1)  
rate = rospy.Rate(3)  
  
Subscriber  
0.shebang & import  
1. init_node 설정 (node 이름 설정)  
2. rospy.Subscriber(이름, 타입, 이걸 전달할 함수)  
3. callback 함수 사용  
  
#! /usr/bin/env python3  
rospy.init("이름")  
pub = rospy.Subscriber('counter', Int32, callback)  
def callback(msg)  

------------------------------  
  
### python을 사용해서 script 형태로 읽지않고 바로 ros로 실행하는 법

#### 사전 작업
~/study_ws    $ catkin_make        C++로 빌드를 진행  
~/study_ws    $ source /opt/ros/noetic/setup.bash  
~/study_ws    $ source devel/setup.bash           source 적용시켜 주겠다.   첫번째 이유 내가 사용할 워크 스페이스 안에 있는 패키지를 사용하기 위한 적용 단계  

#### 실행 시 에러 발생  
  
~/study_ws$ rosrun basics topic_subscriber.py
[rosrun] Couldn't find executable named topic_subscriber.py below /home/user/study_ws/src/basics
[rosrun] Found the following, but they're either not files,
[rosrun] or not executable:
[rosrun]   /home/user/study_ws/src/basics/scripts/topic_subscriber.py

#### 권한 부여
ls -al 을 실행하면 권한이 없음을 알 수 있음 rw권리만 존재, x가 없고 초록색이 아님.  
권한이 없음. chmod를 통해 x 즉 실행 권한을 부여주어야함.                      # 두번째 이유  
~/study_ws/src/basics/scripts   $ chmod 777 topic_publisher.py    해결방안: 실행가능한 최고 권한을 부여하였음  
sudo chmod 777 topic_publisher.py  

#### 터미널 실행
roscore 터미널에서 실행  
source devel/setup.bash  
rosrun basics topic_Subscriber.py  
source devel/setup.bash  
rosrun basics topic_publisher.py  

#### rostopic의 pub으로 publish하는 방식
~/study_ws$ rostopic pub /counter std_msgs/Int32 "data: 0" #/counter 뒤엔 Tab키로 자동완성 가능, "data: 0" 부분 수정시 데이터가 그렇게 전달됨  


### turtlesim 활용 
roscore 
rosrun turtlesim turtlesim_node  
기존 subscriber 수정(파일을 복사하면 권한도 복사됨)  
rostopic info /turtle1/Pose 정보 확인    
데이터 turtlesim의 msg 중 pose 데이터 형태를 import from turtlesim.msg import Pose    
callback 함수 수정 msg에 속한 것들 중   
Subscriber 설정 sub = rospy.Subscriber("/turtle1/pose", Pose, callback)  
 1. 경로 변경, 2. 데이터 방식 변경, 3. callback 함수 호출

Class화 시키기  



##### 여담
.bashrc 에는 단축어나 사전 설정할 내용들을 넣는다.  
축약어는  
alias 축약 = '명령어'  
class로 사용하기  



