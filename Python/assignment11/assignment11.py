def add_two_numbers(a ,b):
    return a + b

def circle_area(r):
    pi = 3.14
    return pi * r * r

def add_all_nums (*number):
    total = 0
    for num in number:
        total += num
    return total

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def check_season(month):
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Invalid month'

def solve_quadratic_eqn(a, b, c):
    import cmath
    d = (b**2) - (4*a*c)
    sol1 = (-b + cmath.sqrt(d)) / (2*a)
    sol2 = (-b - cmath.sqrt(d)) / (2*a)
    return sol1, sol2

def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(lst):
    return lst[::-1]

def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

def add_item(lst, item):
    lst.append(item)
    return lst

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i
    return total

def sum_of_evens(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total

def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def is_empty(lst):
    return len(lst) == 0

def count_average(lst):
    if len(lst) == 0:
        return 0
    return sum(lst) / len(lst)

def count_median(lst):
    n = len(lst)
    if n == 0:
        return 0
    sorted_lst = sorted(lst)
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        median = sorted_lst[mid]
    return median

def count_mode(lst):
    from collections import Counter
    if len(lst) == 0:
        return None
    count = Counter(lst)
    max_count = max(count.values())
    modes = [k for k, v in count.items() if v == max_count]
    return modes

def count_scope(lst):
    if len(lst) == 0:
        return 0
    return max(lst) - min(lst)

def variation_number(lst):
    if len(lst) == 0:
        return 0
    mean = count_average(lst)
    var = sum((x - mean) ** 2 for x in lst) / len(lst)
    return var

def standard_deviation(lst):
    import math
    var = variation_number(lst)
    return math.sqrt(var)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_unique(lst):
    return len(lst) == len(set(lst))

def is_valid_variable(name):
    import keyword
    if not name.isidentifier() or keyword.iskeyword(name):
        return False
    return True

def generate_random_ip():
    import random
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

