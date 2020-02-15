# Home IOT DIY

## 소개

라즈베리 파이 등을 중간 서버로 사용한 아두이노, Nodemcu, 아이폰의 Siri (혹은 빅스비)를 이용한 홈 IOT 입니다.

### 구현된 기능

구현된 기능은 다음과 같습니다.

- Siri를 사용한 컴퓨터 전원 켜기 (WOL 기능 사용) [[파이썬 소스](https://github.com/wookoo/SimpleHomeIOT/blob/master/RestServer/app/views.py#L15)]
- Siri와 Nodemcu 를 사용한 컴퓨터 전원 켜기 , 끄기 (물리적인 릴레이 스위치 사용) [[파이썬 소스](https://github.com/wookoo/SimpleHomeIOT/blob/master/RestServer/app/views.py#L48)][[아두이노 소스]("https://github.com/wookoo/SimpleHomeIOT/blob/master/DeviceSource/ComputerTrigger/ComputerTrigger.ino")]
- Siri와 Nodemcu, 릴레이를 사용한 전등 제어 [[파이썬 소스](https://github.com/wookoo/SimpleHomeIOT/blob/master/RestServer/app/views.py#L67)] [[아두이노 소스](https://github.com/wookoo/SimpleHomeIOT/blob/master/DeviceSource/LightSwitch/LightSwitch.ino)]

~~~
siri 를 사용 할 필요 없이 서버 수정을 조금만 하면 웹으로도 가능합니다.
~~~

<hr>


## 설정

해당 부분에선 사용 전 기능 설정법을 알려드립니다.

### 서버 컴퓨터 사전 설정

사전설치 필요 모듈은 다음과 같습니다.

- django2.0
- request

공유기 설정에서, 라즈베리파이의 django에서 사용할 포트포워딩을 진행하셔야합니다.
~~~
보안을 신경쓰시는분들은 라즈베리 파이를 포트포워딩으로 물리지 마시고, 내부 망에서 사용하십시오!
~~~


### WOL 설정
~~~
구현 기능의 WOL 기능을 사용하여 컴퓨터의 전원을 키기 위해선 WOL 설정을 해야 합니다.
~~~

- WIN + R 키를 동시에 누릅니다.
- 실행창에서 devmgmt.msc 를 입력하고 확인을 누릅니다.
- 네트워크 어댑터 항목 중 자신의 PC 에 맞는 네트워크 어댑터를 우클릭 하고 속성을 누릅니다.
- 고급설정 항목 또는, 전원 관리 옵션에 가서 Wake on Magic Packet, Wake on Pattern Match 등의 항목을 체크하거나 Enable 로 바꿉니다.
- 그 후 제어판의 전원 옵션의 기본 전원 관리 옵션에서 고성능으로 바꿉니다.
- 전원 옵션 항목의 왼쪽 부분읠 보면 전원 단추 작동 설정 버튼이 있는데, 그 버튼을 눌러줍니다.
- 현재 사용할 수 없는 설정 변경을 누르고, 빠른 시작 켜기 및 최대 절전 모드를 체크 해제 한 후 저장합니다.
- cmd 를 실행 시키고 ipconfig /all  을 타이핑 하여 IPv4 주소, 물리적주소 (MAC) 주소를 메모해 놓습니다.

### 중요사항

모든 장비는 동일한 내부 IP 에 연결되어있어야 합니다.

외부와 통신되는 장비(포트포워딩)는 라즈베리 파이와 같이 서버컴퓨터 한대 뿐입니다.

<hr>
