class Book:
    def __init__(self,t,au,pa):
        self.title=t
        self.author=au
        self.pages=pa
    def __str__(self):
        return f'{self.title} by {self.author}'
    def __len__(self):
        return self.pages
    def __del__(self):
        print('book object is deleted')
b=Book('python','someone',200)
print(b)
print(str(b))
print(len(b))
del b