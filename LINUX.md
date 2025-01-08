# OS

Window: 유저 친화적, 데이터에 대한 보호(강제 종료)  
Linux: 방대한 데이터를 수용 가능. 개발자에게 적합   
오픈소스 OS  
서버-페도라  
일반-우분투  
  
하드웨어  
커널(Kernel)  
쉘(Shell)  
Terminal  
유저  

## Linux FileSystem
/ (root) 최상위 폴더   
슈퍼 유저의 홈디렉토리  
/boot 리눅스 커널을 보관하고 있는 폴더  
/etc 시스템 설정 파일들이 모여있는 폴더  
/home 일반적으로 사용하는 위치, User가 사용할 수 있는 공간 제공(유일하게 수정할 수 있음)  
/mnt usb 저장 장치 및 외장하드 등이 마운팅 되는 위치  
/proc 커널을 통해 관리되는 폴더, 커널을 통해 볼 수 있는 가상의 파일들이 존재  
/sys 커널을 통해 확인할 수 있는 하드웨어등의 폴더  
/dev 연결된 장치를 확인할 수 있는 폴더, 카메라, 센서 등 리눅스에선 장치들도 파일로서 관리되고 있음  
/bin 실행할 수 있는 파일들이 위치한 폴더 실행하는 명령어들의 binary 파일 존재  
/sbin System Binary 파일들이 존재  
/lib 시스템에서 사용하는 라이브러리 파일들이 존재. .so, .a 파일들이 존재 (리눅스에서 프로그램 설치를 위해선 사전 설치가 필요한 라이브러리들이 많음)   
/usr 사용자에 대한 폴더
/tmp 임시 파일들이 존재하는 폴더  
/opt 필수적인 파일들이 아닌 optional한 파일들이 위치한 폴더, 필수적이지 않은 소프트웨어를 설치하면 여기 설치되는 경우가 존재    
/var  
/lost+found 잠금 및 복구를 위한 폴더  

## ubuntu
일반 리눅스 배포판 중 가장 많이 사용되는 Debian 계열  
짝수 해 4월에 LTS (Long Term Support) 버전이 출시  
정규 버전 6개월 마다 배포되며, 배포일 기준으로 9개월 간 업데이트 및 지원  
LTS 버전은 2년 마다 배포, 배포일 기준 최대 5년까지 업데이트 및 지원  

## Linux 설치 및 Linux Command
권장 50GB ~ 100GB 정도 필요  
Bash(Bourne-Again Shell)  
현재 리눅스의 표준 쉘  
Alias : 명령어 및 단축 기능  
연산, History, 자동 이름 완성, 프롬프트 제어 기능 등이 존재  
  
다양한 터미널이 존재함. 수업에선 터미네이터를 사용  
termianl 실행 단축키 Ctrl + Alt + T 

$sudo apt install termianter

sudo -> 관리자 권한으로 이후의 명령어 실행
apt install -> apt 패캐지 네임으로 설치하겠다.
terminater -> 설치할 프로그램 명

sudo - 특정 명령어를 관리자 권한으로 실행하는 명령어
sudo <<사용할 명령어>>

특정 명령어를 관리자 권한(root 권한) 으로 실행  
비밀번호를 입력하게 나오는데 짧은 비밀번호는 처음 설치할 때만 가능(이후 8자 이상)  

apt(advanced package installer) - 패캐지 설치 관리자  
sudo apt install <<PACKAGE_name>>  
필요한 패캐지를 설치할 수 있도록 해주는 관리자  

pwd(Print Working Directory) - 현재 작업 중인 폴더 출력  
현재 작업 중인 폴더의 절대 경로 출력  

cd (Change Directory) 현재 작업 중인 폴더를 변경  
절대 경로 및 상대경로 모두 들어갈 수 있음  
이동 경로 생략 ~  
뒤로 가기 ../  

Tab 자동 완성 , 설명  
cd ca (Tab)  
ca 로 시작하는 폴더 나열  
  
ls(list contents)***  
$ ls <경로> 
폴더 내부의 파일 및 폴더 리스트 출력    
폴더 파란색, 파일 흰색, 실행 파일 초록색  
-l 상세 표기(권한, 크기, 수정시간 등)  
-a 숨김 파일 출력  
  
명령어 --help  
명령어에 대한 상세 설명 확인 가능  

mkdir (MAKE directory)  
폴더를 만드는 명령어  
-p 폴더 옵션  
mkdir -p 폴더1/폴더2  

touch 파일의 최종 수정 시간 변경 , 새 파일 생성  
code (vscode 확장 명령어) touch와 같은 기능, vscode에서 실행시킴.  
  
echo *  
파일 또는 터미널에 특정 내용 출력  
cat  
파일 내부의 내용을 출력해주는 명령어  
  
cp  *  
파일 또는 폴더를 복사하는 명령어  
-r 옵션을 사용하면 디렉터리와 그 안의 모든 내용(하위 디렉터리, 파일 등)을 복사할 수 있음
$cp -r [복사할 디렉토리][목적지 디렉토리]  

mv(move)  *  
파일 및 폴더 이동 명령어  
이름 바꿀 때 사용  
  
rm (remove file)  ***  
파일 및 폴더 삭제 명령어  
-r 폴더 삭제 시 필요 옵션
-f 폴더 없어도 무시하고 진행 옵션  
$ rm -rf <> 문제가 생길 수 있으므로 확인하고 진행  
  
find  
특정 폴더에서 파일 검색하는 명령어  

grep  
특정 내용을 검색하는 명령어  
grep <<검색할 내용>> <<검색할 파일>> 

find <<경로>> | grep <<검색내용>>  
  
df  
파일 시스템의 디스크 사용량을 확인할 수 있는 명령어  

du  
폴더 크기를 확인하는 명령어  
du -b 폴더명  

head  
공백포함 맨 위 기본 10줄  
head -n 5 ~/.bashrc  
-n 5  
number 5  
앞부분 5줄 출력, tail 뒷부분  

chown    
파일의 소유 권한을 변경  

chmod **중요**  
파일 또는 폴더의 권한을 변경하는 명령어  
chmod {a, u, g, o}{+, -}{r, w, x} <<파일명>>
chmod {000~777} <<파일명>>
a, u, g, o = all, user, group, others 사용자들
r, w, x 읽기, 쓰기, 실행 권한
000, 777 8진법에 따른 권한  
777(최고권한) - 실행가능 파일 초록색  
권한을 부여하는 것도 관리자로 해야하므로  
sudo chmod 777 << >> 세트  

ps  
현재 실행 중인 프로세스 확인    
ps ux | grep <<..>>  

kill  
프로세스 종료  
kill 옵션 프로세스_번호(번호로 종료해야하기 때문에 ps로 먼저 프로세스 확인하고 kill)  
-15 프로그램 종료 요청 명령 전달  
-9 강제 종료(주로)  
kill -9 242525  

ping  
인터넷 접속 여부 확인  
ping google.com -c 5
ping 8.8.8.8 
ping <확인할 IP><url><-c><횟수>
127.0.0.1 자기 자신  

wget  
온라인 파일을 다운로드하는 명령어  
wget <<온라인 주소>>  

uname  
unix name의 준말, 리눅스 시스템 관련 정보 확인 명령어  
-a 전부  
-r 리눅스에 대해  

top  
cpu 사용량 출력  

history  
입력했던 명령어 기록 출력  
history | grep ros  
ros로 검색, 관련해서 썼던 명령어만 검색  

man  
manual의 약자 특정 명령어에 대한 메뉴얼 제공  
man ls  
man mv  
man mkdir  

hostname  
호스트 및 네트워크 정보를 확인하는 명령어(네트워크 확인할 때 많이 씀)  
$ hostname i  
ip주소(ros 환경에서 중요하게 사용함)  

SSH  
IP 일때 UI 없이 터미널로만 원격 제어  
vscode의 경우 모니터없이 불가능 = VI나 nano 편집기를 사용해야함.   
모니터가 없는 경우 = 냉장고나 세탁기 같은 임베디드 시스템들, 실습에 사용할 자동차 플랫폼  
  
sudo apt install ssh  









