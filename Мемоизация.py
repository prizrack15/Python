#Мемоизация (Кэш) (англ. memoization от англ. memory и англ. optimization) —
# пример использования кэша при разработке программного обеспечения, в
# программировании сохранение результатов выполнения функций для предотвращения
# повторных вычислений. Это один из способов оптимизации,
# применяемый для увеличения скорости выполнения компьютерных программ.

from time import time


def timed(func):
    def timed_func(*args, **kwargs):
        tmp = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'executed, time:', time() - tmp)
        return result

    return timed_func


def memoized(func):
    memory = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in memory:
            memory[key] = func(*args, **kwargs)
        return memory[key]

    return wrapper


@timed
@memoized
def collatz_sequence(n):
    while n != 1:
        print(n)
        n = (3 * n + 1) if n % 2 else (n // 2)

collatz_sequence(3634636457745737575776)