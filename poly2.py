from abc import  ABC, abstractmethod


class Car (ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Nano(Car):
    def start(self):
        print("Starting Nano")

    def accelerate(self):
        print("Accelerating Nano")

    def stop (self):
        print ("stop Nano")



class Alto(Car):
    def start(self):
        print("Starting Alto")

    def accelerate(self):
        print("Accelerating Alto")

    def stop(self):
        print("Stopping Alto")


class Person():

    def drive(self, car):
        car.start()
        car.accelerate()
        car.stop()


def main():
    p1 = Person()
    c1 = Nano()
    c2 = Alto()

    p1.drive(c1)
    p1.drive(c2)



main()



