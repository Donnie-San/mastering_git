class Animal:
    def __init__(self, type, health, speed):
        self.type = type
        self._health = health
        self._speed = speed

class Prey(Animal):
    def __init__(self, type, health, speed):
        super().__init__(type ,health, speed)
    
    def flee(self):
        print(f"{self.type} is fleeing!")

class Predator(Animal):
    def __init__(self, type, health, speed):
        super().__init__(type, health, speed)


    def hunt(self):
        print(f"{self.type} is hunting!")

class Fish(Prey, Predatorl):
    def __init__(self, health, speed, type = "Fish"):
        super().__init__(type, health, speed)

class Fish(Prey, Animal):
    def __init__(self):
        super().__init__()

def main():
    fish1 = Fish()
    fish2 = Fish()
    # Ya'll stop messing with the code

if __name__ == '__main__':
    main()

