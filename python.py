'''
#Задача 1: отфильтровать чётные числа от 1 до 20
# Попробуй сам написать List Comprehension, который создаёт список только из чётных чисел от 1 до 20.

x = [x for x in range(1, 21) if x % 2 == 0]
print(x)'''


'''
#Сформируй список из чисел от 1 до 10, где чётные числа заменяются на 'четное', а нечётные — на 'нечетное'
for i in range(1, 21):
    if i % 2 == 0:
        print('ч')
    else:
        print('не')

x = ['Четное' if i % 2 == 0 else 'Нечетное' for i in range(1,11)]
print(x)

'''



'''
#Создай список квадратов всех чисел от 1 до 10, но только для нечётных чисел.
#x = map[lambda x: x if % 2 != 0 x ** 2 ]


for i in range(1, 11):
    if i % 2 != 0:
        res = i ** 2
        print(res)

x = [ i ** 2 for i in range(1,11) if i % 2 != 0 ]
print(x)'''

'''

#🔸 1. Условные операторы
# Задача: Напиши функцию, которая принимает число и возвращает "Fizz",
# если делится на 3, "Buzz" — если на 5, и "FizzBuzz", если на 3 и на 5.

def fizz_buzz(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)

print(fizz_buzz(15))  # FizzBuzz
print(fizz_buzz(9))   # Fizz
print(fizz_buzz(10))  # Buzz
print(fizz_buzz(7))   # 7

#🔸 2. Работа со строками

# Задача: Сделай из строки список слов, переверни каждое слово и собери обратно.

def one_les(s):
    text = s.split()
    word = [text[::-1] for text in text]
    return ' '.join(word)

print(one_les('hello world'))

#🔸 3. Работа с функциями
# Напиши функцию, которая принимает список чисел и возвращает только чётные.

def filter_even(nums: list[int]) -> list[int]:
    return [num for num in nums if num % 2 == 0]


print(filter_even([1, 2, 3]))

#🔸 4. Вложенные циклы
# Нарисуй прямоугольник из символов `#` размером 5 строк и 10 столбцов
# (используй вложенные циклы)

for i in range(5):
    for l in range(10):
        print("#", end=' ')
    print()


#🔸 5. Декоратор
# Напиши декоратор, который выводит "Функция вызвана!" перед вызовом любой функции.

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Функция вызвана')
        res = func(*args, **kwargs)
        return res
    return wrapper



@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Ожидается:
# Функция вызвана!
# Hello!


def count_elements(lst):
    result = {}
    for item in lst:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

print(count_elements(['a', 'b', 'a', 'c', 'b', 'a']))'''

