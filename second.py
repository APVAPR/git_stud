g = 1, 4, 5, 6, 7, 6
print('Secondgit')

for i in g:
    print(i)


def ppp(a: tuple):
    print(a[-1])


ppp(g)


def tt(b: int):
    print(b)


tt(4)


class Robot:
    count = 0

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self):
        return 'I am robot {} {}'.format(self.name, self.model)

