"""
# Функция проверяет, является ли слово палиндромом
def is_palindrome(word: str) -> bool:
    # Возвращаем True, если слово равно своему перевёрнутому варианту
    return word[::-1] == word

# Проверяем функцию на слове "hello"
print(is_palindrome('hello'))

Напиши функцию, которая принимает список чисел и возвращает новый список, где каждое число умножено на 2.
Например,
вход: [1, 2, 3]
выход: [2, 4, 6]

nums = [1,2,3]
x = map(lambda x: x *2, nums)
print(list(x))

#Дан список строк. Используя filter и лямбда-функцию,
# отфильтруй только те строки, длина которых больше 4 символов.
words = ['apple', 'bat', 'car', 'dolphin', 'egg']

x = filter(lambda a: len(a) > 4, words)
print(list(x))

#Дан список чисел. Нужно с помощью функции filter и лямбда-функции выбрать только положительные числа.
#Например, из списка [-3, 0, 5, -1, 8, -7] должно получиться [5, 8].

num = [-3,0,5,-1,8,-7]
x = filter(lambda a: a > 0, num)
print(list(x))

#Дан список чисел. Используй функцию map с лямбда-функцией, чтобы создать новый список,
# в котором каждое число возведено в куб (в третью степень).

num = [-3,0,5,-1,8,-7]
result = map(lambda x: x ** 3, num)
print(list(result))

#Напиши функцию, которая принимает число и возвращает строку:
# "Положительное", если число > 0
# "Отрицательное", если число < 0
# "Ноль", если число == 0

def num_da(num):
    if num > 0:
        return 'Положительное'
    elif num < 0:
        return 'Отрицательное'
    else:
        return 'Ноль'
print(num_da(-7))


#Напиши функцию is_leap_year(year: int) -> bool, которая принимает год и возвращает True, если год високосный, иначе False.
# Правила високосного года:
# Год делится на 4, но не делится на 100, или
# Год делится на 400.
# Например:
# is_leap_year(2000) -> True
# is_leap_year(1900) -> False
# is_leap_year(2024) -> True
# is_leap_year(2023) -> False

def is_leap_year(year:int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


print(is_leap_year(1900))

#Напиши функцию, которая принимает число и возвращает сумму всех чисел от 1 до этого числа включительно.
# Например:
# sum_up_to(5) должно вернуть 15 (1+2+3+4+5).

def sum_up_to(num):
    total = 0
    for i in range(1, num + 1):  # проходим от 1 до num включительно
        total = i + total        # накапливаем сумму
    return total

print(sum_up_to(5))  # выводит 15

#Напиши программу, которая с помощью вложенных циклов рисует прямоугольник 4 строки на 7 символов:
#######
#######
#######
#######

for i in range(4):
    for j in range(1,8):
        print('#', end='')
    print()

#Создай декоратор log_args, который будет выводить аргументы, с которыми вызывается функция.

def log_args(func):
    def decorator(*args, **kwargs):
        # Выводим имя функции и переданные аргументы
        print(f'Вызов функции {func.__name__} с аргументами: {args} {kwargs}')
        result = func(*args, **kwargs)
        return result
    return decorator

@log_args
def greet(name_2):
    print('Hello', name_2)

greet('Isa')


#Напиши декоратор benchmark, который будет:
# Принимать название операции как аргумент (например, "Сложение", "Загрузка данных" и т.д.).
# Засекать и выводить время выполнения функции.
# Выводить сообщение в виде:

import time

def benchmark(operation_time):
    def decorator(func):
            def wrapper(*args, **kwargs):
                start = time.time()
                res = func(*args, **kwargs)
                end = time.time()
                print(f'Операция: {operation_time} - выполнена за {end - start} секунд')
                return res
            return wrapper
    return decorator

@benchmark('Сложение')
def add_numbers(a,b):
    return a + b

print(add_numbers(5,7))

#Задача 1: отфильтровать чётные числа от 1 до 20
# Попробуй сам написать List Comprehension, который создаёт список только из чётных чисел от 1 до 20.

x = [x for x in range(1, 21) if x % 2 == 0]
print(x)

#Сформируй список из чисел от 1 до 10, где чётные числа заменяются на 'четное', а нечётные — на 'нечетное'
for i in range(1, 21):
    if i % 2 == 0:
        print('ч')
    else:
        print('не')

x = ['Четное' if i % 2 == 0 else 'Нечетное' for i in range(1,11)]
print(x)


#Создай список квадратов всех чисел от 1 до 10, но только для нечётных чисел.
#x = map[lambda x: x if % 2 != 0 x ** 2 ]


for i in range(1, 11):
    if i % 2 != 0:
        res = i ** 2
        print(res)

x = [ i ** 2 for i in range(1,11) if i % 2 != 0 ]
print(x)


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

print(count_elements(['a', 'b', 'a', 'c', 'b', 'a']))

#A pangram is a sentence that contains every single letter
# of the alphabet at least once. For example, the sentence
# "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram.
# Return True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(st):
    sentence = st.lower()
    return all(sentence for i in string.ascii_letters if i in sentence)

print(is_pangram('The quick brown fox jumps over the lazy dog'))

#Implement a function which convert the given boolean value into its string representation.
# Note: Only valid inputs will be given.

def boolean_to_string(b):
    #your code here
    return str(b)

boolean_to_string(False)


#Some numbers have funny properties. For example:
# 89 --> 8¹ + 9² = 89 *
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 *
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the digits of n raised to consecutive powers starting from p is equal to k * n.
# In other words, writing the consecutive digits of n as a, b, c, d ..., is there an integer k such that :
# If it is the case we will return k, if not return -1.
# Note: n and p will always be strictly positive integers.

def dig_pow(n, p):
    # your code
    digits = str(n)
    total = 0
    for i, digit in enumerate(digits):
        total += int(digit) ** (p + i)
    if total % n == 0:
        return total // n
    else:
        return -1
print(dig_pow(92, 1))

#Задача: Найти "числа Нарцисса" (Armstrong numbers)
# Условие:
# Число называется нарциссическим числом (или числом Армстронга),
# если сумма его цифр, возведённых в степень количества цифр, равна самому числу.

def is_armstrong(n):
    digits_str = str(n)              # строка вида '153'
    num_digits = len(digits_str)     # количество цифр = 3
    total = 0
    for digit in digits_str:         # перебираем символы строки
        total += int(digit) ** num_digits
    return total == n

print(is_armstrong(153))   # True
print(is_armstrong(9474))  # True
print(is_armstrong(123))   # False


#Introduction
# The first century spans from the year 1 up to and including the year 100, the second
# century - from the year 101 up to and including the year 200, etc.
# Task
# Given a year, return the century it is in.

def century(year):
    # Finish this :)
    return (year + 99) // 100

print(century(1705))

#Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
# Note: The function accepts an integer and returns an integer.
# Happy Coding!
def square_digits(num):
    # Your code here
    total = ''
    for i in str(num):
        i = int(i)
        total += str(i ** 2)
    return int(total)

print(square_digits(9119))


#Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit, there are 3 multiplications)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2, there are 4 multiplications)
# 4 --> 0 (because 4 is already a one-digit number, there is no multiplication)
def persistence(n):
    total = 0
    while n >= 10:
        prod = 1
        for i in str(n):
            prod *= int(i)
        n = prod
        total += 1
    return total

print(persistence(39))

#iven an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
# Return your answer as a number.

def sum_mix(arr):
    #your code here
    return sum(int(n) for n in arr)

print(sum_mix([9, 3, '7', '3']))



#You were camping with your friends far away from home, but when it's time to go back,
# you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average,
# your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    return (True if mpg * fuel_left >= distance_to_pump else False)

print(zero_fuel(100, 50, 1))
def remove_every_other(my_list):
    return my_list[::2]

print(remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"]))


import re
with open('', 'r') as file:
    data = file.read().strip()

res = re.findall(r'([a-zA-Z])', data)
doc = ''.join(char * int(num) for char, num in res)

with open('', 'w') as file:
    file.write(doc)





with open('', 'r') as file:
    data = file.read().lower().split()

word_counts = {}

for word in data:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Находим слово с максимальной частотой (если несколько — выбираем минимальное по алфавиту)
most_common = max(word_counts.items(), key=lambda x: (x[1], -ord(x[0][0])))

# Все слова с максимальной частотой
max_freq = most_common[1]
candidates = [word for word, count in word_counts.items() if count == max_freq]

# Выводим лексикографически первое слово и его частоту
result = min(candidates)
print(result, max_freq)


def find_uniq(arr):
    # your code here
    if arr[0] != arr[1] and arr[0] != arr[2]:
        return arr[0]
    elif arr[1] != arr[0] and arr[1] != arr[2]:
        return arr[1]

    com = arr[0]
    for num in arr:
        if num != com:
            return num

print(find_uniq([1, 1, 1, 2, 1, 1]))

def find_uniq(arr):
    uniq_set = set(arr)
    return [x for x in  uniq_set if arr.count(x) == 1][0]

print(find_uniq([1, 1, 1, 2, 1, 1]))



def number_to_string(num):
    return str(num)

print(number_to_string(123))


def friend(x):
    #Code
    return [i for i in x if len(i) == 4]

print(friend(["Ryan", "Kieran", "Jason", "Yous"]))



def summation(num):
    total = 0
    for i in range(1, num + 1):
        total += i
        print(f'{i}: {total}')
    return total

print(summation(10))

def summation(num):
    return sum(range(1, num + 1))
print(summation(5))

def litres(time):
    return int(time * 0.5)
print(litres(11.8))


def feast(beast, dish):
    # your code here
    return beast[0] == dish[0] and beast[-1] == dish[-1]

print(feast("great blue heron", "garlic naan"))



def area_or_perimeter(l , w):
    # return your answer
    return l * 2 + w *2 if l != w else l * w

print(area_or_perimeter(3, 3))
def count_sheep(n):
    # your code
    return ''.join(f"{i} sheep..." for i in range(1, n + 1)) if n > 0 else ''
print(count_sheep(5))



def min_max(lst):
  return [min(lst), max(lst)]


print(min_max([1]))

def cube_odd(arr):
    #your code here - return None if at least a value is not an integer
    total = 0
    for num in arr:
        if not isinstance(num, int) or isinstance(num, bool):
            return None
        if num % 2 != 0:
            num = num ** 3
            total += num
    return total
print(cube_odd([1, 2, 3,4,5]))

def cube_odd(arr):
    return sum(i**3 for i in arr if i % 2 != 0) if all(type(i) == int for i in arr) else None

print(cube_odd([1, 2, '3',4,5]))




def tower_builder(n_floors):
    tower = []
    width = n_floors * 2 - 1
    for i in range(1, n_floors + 1):
        stars = "*" *( 2 * i- 1)
        floor = stars.center(width)
        tower.append(floor)
    return tower


print(tower_builder(3))"""