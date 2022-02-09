from day26.classlib.supersonic_airplane import SuperSonicAirplane

sa = SuperSonicAirplane()
sa.take_off()
sa.fly()
sa.fly_made = SuperSonicAirplane.SUPERSONIC
sa.fly()
sa.fly_made = SuperSonicAirplane.NORMAL
sa.fly()
sa.land()