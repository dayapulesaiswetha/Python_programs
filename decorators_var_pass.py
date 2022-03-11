#passing function variables to decorators

def log_func(func):
    def inner_func(x):
        print("log starts" +str(x))        
        func(x)
        print("log ends" +str(x))
    return inner_func

@log_func
def func(*args):
    print("Function start")
    
func(1)