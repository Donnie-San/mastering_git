class Animal:
    def __init__(self):
        pass

class Prey(Animal):
    def __init__(self):
        super().__init__()

class Predator(Animal):
    def __init__(self):
        super().__init__()

class Fish(Prey, Animal):
    def __init__(self):
        super().__init__()

def main():
    pass

if __name__ == '__main__':
    main()