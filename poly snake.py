class Animal():
    def move(self):
        print('animal is moving')
class Snake(Animal):
    def move(self):
        print('snake is crawling')
s=Snake()
s.move()

