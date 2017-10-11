class test:
    def __init__(self):
        self.type = 'TEST'

class tank:
    def __init__(self):
        self.type = 'tank'

class bullet:
    def __init__(self):
        self.type = 'bullet'

c = bullet()

t = c.__class__.__name__

print('class name', t)

f = t()

print('created object', f)


2240
3840