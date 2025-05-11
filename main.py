class Animal:
    def __init__(self, health, speed):
        self._health = health
        self._speed = speed

class Prey(Animal):
    def __init__(self, health, speed):
        super().__init__(health, speed)

class Predator(Animal):
    def __init__(self, health, speed):
        super().__init__(health, speed)

class Fish(Prey, Predatorl):
    def __init__(self, health, speed):
        super().__init__(health, speed)