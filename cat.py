from animal import animal


class cat(animal):
    hair = "短毛"

    def __init__(self, name, color, age, gender) -> object:
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender


def catchmouse(self):
    print(f'{self.name}会捉老鼠')


def shoot(self):
    print(f'{self.name}会喵喵叫')


cat = cat('KOOK','blue',2,'female')
print(f'猫的姓名是{self.name}','颜色是{self.color}','年龄是{self.age}','性别是{self.gender}')
