class Dog:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"Hi, I'm {self.name} the dog!")


for _ in range(10):
    dog = Dog("Willie")
    dog.say_hi()
