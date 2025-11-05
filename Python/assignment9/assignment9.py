print("Enter your age:")
age = int(input())
if age >= 18:
    print("You age old enough to drive.")
elif age < 18:
    print("You are not old enough to drive.")
    print(f"You need to wait {18 - age} years to drive.")

print("Enter your age:")
age = int(input())
print("Enter my age:")
my_age = int(input())
if my_age > age:
    print(f"I am {my_age - age} years older than you.")
elif my_age < age:
    print(f"You are {age - my_age} years older than me.")
else:
    print("We are the same age.")

print("Enter number one:")
input1 = int(input())
print("Enter number two:")
input2 = int(input())
if input1 > input2:
    print(f"{input1} is greater than {input2}.")
elif input1 < input2:
    print(f"{input2} is greater than {input1}.")
else:
    print(f"{input1} is equal to {input2}.")

print("Enter student score:")
score = int(input())
if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score < 80:
    grade = 'B'
elif 60 <= score < 70:
    grade = 'C'
elif 50 <= score < 60:
    grade = 'D'
elif 0 <= score < 50:
    grade = 'F'
print(grade)
print(f"Please enter your season:")
season = input().lower()
if season == 'autumn' or season == 'fall':
    print("The season is Autumn")
elif season == 'winter':
    print("The season is Winter")
elif season == 'spring':
    print("The season is Spring")
elif season == 'summer':
    print("The season is Summer")

print("Input a fruit name:")
fruit = input().lower()
fruits = ['banana', 'orange', 'mango', 'lemon']
if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print("Fruit added to the list.")
    print(fruits)

person={
    'first_name'    :  'Asabeneh',
    'last_name'     :  'Yetayeh',
    'age'           :   250,
    'country'       :  'Finland',
    'is_married'    :   True,
    'skills'        :  ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address'       :  {
        'street'    :  'Space street',
        'zipcode'   :   '02210'
    }
}

if 'skills' in person:
    if 'Python' in person['skills']:
        print("You have Python skills.")
    else:
        print("You don't have Python skills.")
if ('JavaScript' in person['skills']) and ('React' in person['skills']):
    print("He is a front end developer.")
elif ('Node' in person['skills']) and ('Python' in person['skills']) and ('MongoDB' in person['skills']):
    print("He is a backend developer.")
elif ('React' in person['skills']) and ('Node' in person['skills']) and ('MongoDB' in person['skills']) and ('Python' in person['skills']):
    print("He is a fullstack developer.")
else:
    print("unknown title")

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")