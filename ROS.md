# ROS  
ROS(Robot Operating System) 로봇용 오픈 소스 메타 운영 체제  
미들웨어 시스템  
센서, 언어, 로봇에 대해 규격화하고 통합시켜 놓음.  
보안 취약의 이유로 기업에서 사용하지 않음. ros 기반으로 성능과 보안을 향상시켜 ros2가 출시되었음.  

### 목적
로봇 연구 개발 시, 모든 사람이 협업하고 공유하기 위함  
프레임워크를 제공하진 않으나 약간의 모듈을 추가하여 편리하게 코드를 재사용 가능  
미들웨어의 기능(언어와 운영체제 상관 X, 여러 프로세스 사이의 통신 부분을 담당)  
독립적인 프로세스로 동작(하나의 노드에서 오류 발생 시에도 시스템 지속 작동)  

### 개발환경 
Ubuntu 운영체제 공식 지원  

Ubuntu 20.04에 ROS noetic 사용 예정  

roscore  
중요(master)

터틀로 실험 가능  

### ROS FileSystem  
Repository  
Meta packages  
packages  
package Manifest, Messages, services, Codes, Misc  

include: 헤더 파일 폴더  
src/package: 소스 파일 폴더  
srv: 서비스 유형이 포함된 폴더    
scripts: 실행가능한 python 스크립트를 포함하는 폴더  

Node: Ros의 최소 단위의 프로세스, 실제 하나의 역할만 하게끔 권장  
Message: Node와 Node 사이의 전달하는 데이터, 그 외 통신(서비스나 파라미터, 메시지를 통해)  
Master: 마스터(ROScore)를 통해, 노드의 이름을 등록하고 검색하여 정보를 얻음.  
  
bags: 시작하는 순간 모든 데이터 녹화 저장 및 불러오기 가능  
  
#### 통신방법
services: 입력이 있을 때만 동작하는 형태의 데어터, 송수신을 의미  
양방향 통신으로 노드간의 통신 요청과 동시에 응답하여 처리가 필요한 경우 사용  
*Topics*: 메세지를 식별하기 위해 이름을 붙여놓은 것. 보내는 것을 Publish, 받는 것 Subscribe  
단방향 통신으로 연속적으로 데이터를 송수신, 한 번 접속 시 지속적으로 데이터 송수신(보내는 노드 publisher와 받는 노드 subsciber 가 존재)  
ex) 카메라나 센서 같은 경우는 대부분 Publisher, cmd_vel 속도명령을 대기하고 있는 subsciber
Action: service와 유사, 장기적으로 수행되는 프로세스에서 피드백을 제공하는 양방향 통신.  
ex) 서울에서 부산까지 5번에 나눠 갈 때, 지점 1까지 가기전엔 계속 하던 거 실행  

### ROS 명령어
roscore: master를 실행하는 명령어  
rosrun: 패캐지의 노드를 실행하는 명령어  
roslaunch: 여러 개의 노드를 한번에 실행할 때 사용하는 명령어(roscore가 기반이 되어서 꺼져있어도 바로 core와 함께 실행)  
rosclean: log 파일을 검사하거나 제거 및 정리하는 명령어   
rostopic: 등록된 topic을 다루는 명령어*****  
rostopic bw  
rostopic delay  
rostopic echo*  
rostopic find  
rostopic hz  
rostopic info*   
rostopic list*   
rostopic pub*   
rostopic type  
  
rostopic list  
현재 실행시킨 항목의 topic 확인  
rostopic info 경로 
publisher 뭐가 subcriber엔 뭐가 있는지
rostopic echo 경로
데이터를 출력 
rostopic pub 경로  
publish 시킬 것을 입력  


info로 확인하면 
echo를 통해선 subsciber가 나 스스로 pub에선 publisher의 내가 나옴  

작동중인 터미널 종료  
Ctrl + C  

roscore로 master를 선언, 로컬 환경에선 본인이 master이자 slave 

$ code ~/.bashrc
$ nano ~/.bashrc
~ 상대경로  . 숨겨진 파일
code 혹은 nano 편집기로 열기

각종 센서를 통해서 데이터를 가져오고 subscribe 하는 부분에 대해 publish를 진행함.  

마스터
export ROS_MASTER_URI=http://192.168.0.5:11311
echo $ROS_MASTER_URI  
슬레이브
export ROS_IP=192.168.0.5
echo $ROS_IP

rostopic list  
를 확인하면 연결된 것을 확인할 수 있다.  
  
rostopic pub /turtle1/cmd_vel geometry_msgs/Twist  
설정을 통해서 거북이를 원격으로 움직이는 걸 확인 가능하다.

우분투는 터미널 마다 초기화가 되므로 .bashrc를 수정하여서 모든 터미널에 적용할 수 있다.  
처음이후는 WIFI 접속을 변경할 때, MASTER를 변경할 때, 혼자서 테스트 진행할 때(MASTER=IP, 혹은 export 한 부분을 주석처리) 주소를 변경해주면 된다.  
















