import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        print(f"{func.__name__} 耗时 {time.time()-start:.4f} 返回值:{res if res else None}")
        return res
    return wrapper
@timer
def print_time(x):
    time.sleep(x)
    return x
print(print_time.__name__)
print_time(1)