dog ={
    'name'  :   'Eddy',
    'color' :  'broen',
    'breed' :  'Bulldog',
    'legs'  :   4,
    'age'   :    4
}

student = {
    'first_name'        :   'Eddy',
    'last_name'         :   'Wang',
    'gender'            :   'Male',
    'age'               :   '25',
    'marital_status'    :   'Single',
    'skills'            :   ['Java', 'Python', 'C++', 'SQL', 'HTML', 'CSS', 'JavaScript'],
    'country'           :   'Taiwan',
    'city'              :   'Taipei',
    'address'           :   'No.123, Sec. 1, Zhongxiao E. Rd., Taipei City'
}

print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('C++')
print(student['skills'])
student['skills'].remove('C++')
print(student['skills'])
keys = student.keys()
print(keys)
values = student.values()
print(values)
print(student.items())
student.pop('city')
print(student.items())
del dog