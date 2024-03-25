def caching_fibonacci():
    cache = {}  # Створення порожнього словника для кешування результатів обчислень

    def fibonacci(n):
        # Базові випадки: 0-й елемент - 0, 1-й елемент - 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Перевірка чи число вже є у кеші
        if n in cache:
            return cache[n]

        # Обчислення числа Фібоначчі рекурсивно
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Приклад використання:
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
