from time import sleep,time
def measure_time(func):
    def wrapper(*args):
        start_time= time()
        print(start_time)
        result=func(*args)
        end_time=time()
        print(end_time)
        
        print(f"total execution time taken by {func.__name__} function:{start_time-end_time}")
        return result
    
    return wrapper

@measure_time 
def add(a,b):
    return a+b

print(add(5,7))

