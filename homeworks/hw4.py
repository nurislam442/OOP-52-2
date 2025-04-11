def check_type(func):
    def wrapper(x):
        if isinstance(x, (int, float)):
            return func(x)
        else:
            print("Ошибка: ожидалось число")
    return wrapper

@check_type
def square(x):
    return x * x

print(square(4))      
print(square("hi"))

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Функция вызвана {wrapper.calls} раз")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def hello():
    print("Привет!")

hello()
hello()
hello()
