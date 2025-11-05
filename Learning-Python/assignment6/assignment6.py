brother = ('Eddy',)
sister = ('',)
siblings = brother + sister
print(len(siblings))
parent = ('father', 'mother')
family_members = parent + siblings
print(len(family_members))
print(family_members)
# 安全的 unpack：目前 family_members 長度固定為 4，可直接 unpack
a, b, c, d = family_members
print(f'parent: {a}, {b}')
print(f'brother: {c}')
print(f'sister: {d}')


fruit = ('banana', 'orange', 'mango', 'lemon')
vegetable = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_product = ('milk', 'egg', 'meat', 'butter')
food_stuff_tp = fruit + vegetable + animal_product
food_stuff_lt = list(food_stuff_tp)

def print_food_examples(food_list):
	"""示範如何取中間項、前 3 項與後 3 項（處理偶數/奇數長度）。"""
	n = len(food_list)
	# 中間元素：若長度為奇數則單一中間項，偶數則顯示中間兩項
	if n % 2 == 1:
		mid = n // 2
		middle = food_list[mid]
	else:
		mid1 = n // 2 - 1
		mid2 = n // 2
		middle = food_list[mid1:mid2 + 1]
	print(f'Food stuff middle: {middle}')

	# 取前 3 個（用 [:3] 更清楚）
	print(f'Food stuff first three items: {food_list[:3]}')

	# 取最後 3 個（[-3:]）
	print(f'Food stuff last three items: {food_list[-3:]}')


print_food_examples(food_stuff_lt)
del food_stuff_lt

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print(f'Is "Estonia" a nordic country?\t {"Estonia" in nordic_countries}')