# Autonomous_Driving

  linux 환경에서 python과 ROS(Robot Operating System)을 이용하여 개발

  자율 주행
  운전자의 조작 없이 자동차 스스로 운행이 가능한 자동차를 의미
  총 6단계 (0~5)

  ### 자율 주행 시 변화
  1. 교통 사고 감소(전 세계 연간 100만명)  
  2. 자동차 관련 범죄 감소(뺑소니, 음주운전 등)
  3. 긴급 서비스 향상(응급 차량, 교통신호와 통제)
  4. 자동차 소유 구조 변화
  5. 운전 소외 집단의 차량 이용
  6. 차량의 거주성 증가(업무, 취침, 휴식)
  
  ### 자율주행 시스템
  #### 인지
  센서(카메라, GPS, LiDAR, 레이더 Rader[고가])를 통해 차량 주변을 인식  
  #### 판단
  인지쪽의 결과를 바탕으로 현재 차량의 상태에서 최적의 움직임을 판단하는 기술  
  Global path: GPS 현재 위치에서 목적지까지 경로  
  Local path: global path를 따라가기 위한 최적의 경로  
  #### 제어
  센서 데이터 및 설정된 경로 결과를 기반으로 조향 및 가감속을 제어하는 기술  
  다양한 수식에 따라서 제어  
  PID 제어  
  경로 추종 컨트롤러(Pure Pursuit Controller)  
  MPC  

    
  그냥 딥러닝으로 데이터 수집해서 하면 안 되나? 사람은 시각 및 청각으로 운전을 하니까 그걸 데이터를 모아서 그 상황에 어떤 판단을 내리면서 운전을 하는 지 알 수 있게 학습  
  내부 데이터 (운전자의 eye tracking 및 내부에서 들리는 소리)  
  외부 데이터 (정면, 후면, 측면의 영상 데이터)  






  
