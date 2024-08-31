
# without using decor
def new_decorator(original_func):
    def wrap_func():
        print('some extra code ,before the original function')
        original_func()
        print('some extra code ,before the original function')
    return wrap_func

def func_needs_decorator():
    print("i want to be decorated")
func_needs_decorator()
# o/p=i want to be decorated
decorated_func=new_decorator(func_needs_decorator)
decorated_func()


#o/p=
# i want to be decorated
# some extra code ,before the original function
# i want to be decorated
# some extra code ,before the original function




#  USING DECOR
def new_decorator(original_func):
    def wrap_func():
        print('some extra code ,before the original function')
        original_func()
        print('some extra code ,before the original function')
    return wrap_func
@new_decorator
def func_needs_decorator():
    print("i want to be decorated")
func_needs_decorator()

#o/p=
# i want to be decorated
# some extra code ,before the original function
# i want to be decorated
# some extra code ,before the original function




