# class1.py

class Hello:
    def __init__(self, name):
        self.name = name

class HI(Hello):
    def __str__(self):
        return f"Hello, {self.name}!"
