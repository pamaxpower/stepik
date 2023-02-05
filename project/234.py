class President():

    def __init__(self, name):
        self.name = name


    def __str__(self):
        return f'{self.name} едет во главе кортежа'

print(President('Z'))