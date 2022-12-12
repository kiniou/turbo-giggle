import time

def hello_user(user):
    return f"Hello {user}!!"

def hello_world():
    return f"Hello World!!"

def slow_hello():
    time.sleep(5)
    return hello_world()
