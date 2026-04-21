from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print('Car engine is started')
    
    def move(self):
        print('Car is moving')

c = Car()
c.start_engine()
c.move()