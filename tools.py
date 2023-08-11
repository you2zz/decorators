import datetime
from functools import wraps
import time

def printable(any_funсtion):
    @wraps(any_funсtion)
    def new_function(*args, **kwargs):
        print(f'Сейчас будет вызвана функция {any_funсtion.__name__}')
        print(f'С аргументами {args} и {kwargs}')
        result = any_funсtion(*args, **kwargs)
        print(f'Получен результат {result}')
        return result
    return new_function

def speed_check(any_function):
    @wraps(any_function)
    def new_function(*args, **kwargs):
        start = datetime.datetime.now()
        result = any_function(*args, **kwargs)
        work_time = datetime.datetime.now() - start
        print(f'work time {new_function.__name__}: {work_time}')
        return result
    return new_function


def cached(max_size):
    def cached_(any_function):

        cache = {}
        call_number = 0
        @wraps(any_function)
        def new_function(*args, **kwargs):

            nonlocal call_number
            call_number += 1

            key = f'{args}{kwargs}'
            if key in cache:
                return cache[key]

            if len(cache) >= max_size:
                cache.popitem()
            cache[key] = result

            return result

        return new_function
    return cached_

def with_attempts(max_attempts=3, timeout=0.1):
    def _with_attempts(any_function):

        def new_function(*args, **kwargs):
            error = None
            for i in range(1, max_attempts + 1):
                try:
                    result = any_function(*args, **kwargs)
                    error = None
                    break
                except Exception as err:
                    error = err
                    time.sleep(timeout)
            if error is not None:
                raise error
            return result
        return new_function()
    return _with_attempts()