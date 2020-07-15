import random

class Dog:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        if self.sex == "M":
            return f"{self.name} is a good boy!!!"
        elif self.sex == "F":
            return f"{self.name} is a good girl!!!"
        else:
            return f"{self.name} is a good puppy!!!"
    def __repr__(self):
        return f"Dog(name='{self.name}', age='{self.age}', sex='{self.sex}')"

    def __add__(self, obj):
        if self.sex != obj.sex:
            return [Dog(name="Noname", age=0, sex=random.choice(['M', 'F'])) for _ in range(1, random.randint(1, 5))]
        else:
            raise TypeError('Types are not supported!!!')
            

