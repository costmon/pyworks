# AirPlane을 상속받을 SuperSonicAirplane
from day26.classlib.airplane import AirPlane

class SuperSonicAirplane(AirPlane):
    NORMAL = 1   #클래스 변수
    SUPERSONIC = 2

    def __init__(self):
        self.fly_mode = SuperSonicAirplane.NORMAL

    def fly(self):   #메서드 재정의(오버라이딩 - overriding)
        if self.fly_mode == SuperSonicAirplane.SUPERSONIC:
            print("초음속 비행합니다.")
        else:
            #print("비행기가 일반 비행합니다.")
            super().fly()   #부모 메서드 상속받음
