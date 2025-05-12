class Animal:
    def __init__(self, type, health, speed):
        self._type = type
        self._health = health
        self._speed = speed

class Prey(Animal):
    def __init__(self, type, health, speed):
        super().__init__(type ,health, speed)
    
    def flee(self):
        print(f"{self._type} is fleeing!")

class Predator(Animal):
    def __init__(self, type, health, speed):
        super().__init__(type, health, speed)


    def hunt(self):
        print(f"{self._type} is hunting!")

class Fish(Prey, Predator):
    def __init__(self, health, speed, type = "Fish"):
        super().__init__(type, health, speed)

def main():
    fish1 = Fish(500, 5.6)
    fish2 = Fish(800, 6.7)

    # fish1.hunt() 
    fish2.flee() 
    # This shouldn't be here!

if __name__ == '__main__':
    main()

