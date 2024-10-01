def create_cubes(n):

    for i in range(n):
        yield i**3
print(list(create_cubes(10)))

# or
# for i in create_cubes(10):
#     print(i)