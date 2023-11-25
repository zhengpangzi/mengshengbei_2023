class haha:
    def __init__(self):
        self.name = 'haha'
        self.age = 18
    def say(self):
        print('my name is %s,my age is %d' % (self.name,self.age))
    def __del__(self):
        print('del')
h = haha()
h.say()
