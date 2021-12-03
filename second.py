import hello

print('Secondgit')
print('Third')
print('Haha')
hello.a = 33

print(hello.a)

class Robot:
    count = 0

    def __init__(self, name, model):
        self.name = name
        self.model = model
        Robot.count += 1

    def __str__(self):
        return 'I am robot {} {}. We have {} person'.format(self.name, self.model, Robot.count)

class Cyborg(Robot):
    count = 0

    def __init__(self, name, model, type_c, death_date):
        super().__init__(name, model)
        self.type_c = type_c
        self.death_date = death_date
        Cyborg.count += 1

    def __str__(self):
        return f'I am cyborg {self.name}. We have {self.count} person'


r1 = Robot('Chester', 'xfr123')
r2 = Robot('Molihut', 'ccrf43')
r3 = Robot('Turifost', 'fff321')

print(r1)
r4 = Robot('Ruru', 'trv13')
print(r4)


x = Cyborg('Gugu', 'dfe', 'rubuti', 2076)
print(x)

