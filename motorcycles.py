class Motorcycles:
    def __init__(self, engine, speed, gears, lights):
        self.set_engine(engine)
        self.set_speed(speed)
        self.set_gears(gears)
        self.set_lights(lights)

    def set_engine(self, engine):
        if type(engine) != bool:
            raise TypeError("Engine type is not right")
        else:
            self.__engine = engine

    def get_engine(self):
        return self.__engine

    def set_speed(self, speed):
        if type(speed) != int:
            raise Exception("speed is not right")
        if speed < 0:
            raise Exception("speed value is not valid")
        if self.__engine:
            self.__speed = speed
        else:
            raise Exception("Engine is Off")

    def get_speed(self):
        return self.__speed

    def set_gears(self, gears):
        if type(gears) != int:
            raise Exception("gears is not right")
        if gears < 0 and gears > 5:
            raise Exception("gears are invalid")
        if self.__engine:
            self.__gears = gears
        else:
            raise Exception("gears is neutral")

    def get_gears(self):
        return self.__gears

    def set_lights(self, lights):
        if type(lights) != bool:
            raise Exception("lights are off!!")
        else:
            self.__lights = lights

    def get_lights(self):
        return self.__engine

    def check_engine(self):
        return f'Engine is {self.__engine}'

    def __str__(self):
        return f'Engine is {self.__engine}  and Speed is {self.__speed}'
