letter = 'P'
print(letter)
print(len(letter))
greeting = 'Hello, World!'
print(greeting)
print(len(greeting))
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name + space + last_name
print(full_name)

print(len(first_name))
print(len(last_name))
print(len(first_name) >(len(last_name)))
print(len(full_name))

language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) -1
last_letter = language[last_index]
print(last_letter)

language = 'Python'
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

language = 'Python'
first_tree = language[0:3]
last_tree = language[3:6]
print(last_tree)

language = 'Python'
pto = language[0:6:2]
print(pto)

print('I hope every one enjoying the python challenge.\nDo you?')
print('Days\tTopices\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash symbol (\\)')
print('In every programming language it starts with \"Hello, World!\"')

challenge = 'thirty days of python'
print(challenge.capitalize())

challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7,14))
print(challenge.count('th'))

challenge = 'thirty days of python'
print(challenge.endswith('on'))
print(challenge.endswith('tion'))

challenge = 'thirty\tdays\tog\tphthon'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence)

radius = 10
pi = 3.14
area = pi
result = 'The area of circle with {} is {}'.format(str(radius),str(area))
print(result)

challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

challenge = 'ThirtyDaysPython'

challenge = '30DaysPython'
print(challenge.isalnum())

challenge = 'thirty days of python'

print(challenge.isalnum())

challenge = 'thirty days of python'
print(challenge.isalpha())
num = '123'
print(num.isalpha)

challenge = 'thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

challenge = 'Thirty'
print(challenge.isdigit())
challenge = '30'
print(challenge.isdigit())

num = '10'
print(num.isdecimal())
num ='10.5'
print(num.isdecimal())

challenge = '30DaysOfPython'
print(challenge.isidentifier())
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())

challenge = 'thirty days of python'
print(challenge.islower())
challenge = 'Thirty days of python'
print(challenge.islower())

challenge = 'thirty days of python'
print(challenge.isupper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())

num = '10'
print(num.isnumeric())
print('ten'.isnumeric())

web_tech = ['HTML','CSS','JavaScript','React']
result = '#, '.join(web_tech)
print(result)

challenge = ' thirty days of python'
print(challenge.strip('y'))

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'))

challenge = 'thirty days of python'
print(challenge.split())

challenge = 'thirty days of python'
print(challenge.title())

challenge = 'thirty days of python'
print(challenge.swapcase())
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())

challenge = 'thirty days of python'
print(challenge.startswith('thirty'))
challenge = '30 days of python'
print(challenge.startswith('thirty'))
