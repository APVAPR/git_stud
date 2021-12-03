class Robot:
    count = 0

    def __init__(self, name, model):
        self.name = name
        self.model = model
        Robot.count += 1

    def __str__(self):
        return 'I am robot {} {}. We have {} person'.format(self.name, self.model, Robot.count)



r1 = Robot('Chester', 'xfr123')
r2 = Robot('Molihut', 'ccrf43')
r3 = Robot('Turifost', 'fff321')
