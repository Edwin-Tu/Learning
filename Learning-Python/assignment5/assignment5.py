empty_list = list()
print(len(empty_list))

fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_techs = ['HTML', 'CSS', 'JavaScript', 'React', 'Redux', 'Node', 'MongDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print('Fruits:', fruits)
print('Number of fruitsL', len(fruits))
print('Vegetables:' ,len(vegetables))
print('Number of vegetables:', len(vegetables))
print('Animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

fruits = ['banana', 'orange', 'mango','lemon']
fitst_fruit = fruits[0]
print(fitst_fruit)
second_fruits = fruits[1]
print(second_fruits)
last_fruit = fruits[3]
print(last_fruit)

last_index = len(fruits) - 1
last_fruit = fruits[last_index]

fruits = ['banana', 'orange', 'mango', 'lemon']
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)
print(second_last)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3]
orange_mango_lemon = fruits[-3:]

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'Avocado'
print(fruits)
fruits[1] = 'apple'
print(fruits)
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)
does_exist = 'lime' in fruits
print(does_exist)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
fruits.append('lime')
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')
print(fruits)
fruits.insert(3, 'llime')
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)

del fruits[1]
print(fruits)
del fruits
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2 , -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomanto', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4 , 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Frruits and vegetables:', fruits)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))
ages=[22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)
ages = [22, 19, 24, 25 ,26, 24 ,25, 24]
ages.reverse()
print(ages)

fruits = ['banana', 'orange', 'mange', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24 , 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)


