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

    def accelerae(self):
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



class Cycle :

    def start(self):
        print("Starting Cycle")

    def accelerate(self):
        print("Accelerating Cycle")

    def stop(self):
        print("Stopping Cycle")



class Person():

    def drive(self,  car):
        car.start()
        car.accelerate()
        car.stop()


def main():

    p1 = Person()
    c1 = Nano()
    c2 = Alto()
    c3 = Cycle ()

    p1.drive(c1)
    p1.drive(c2)
    p1.drive(c3)
main()