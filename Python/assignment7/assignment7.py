# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#practise level 1
print(f"it_companies have {len(it_companies)} items.")
it_companies.add('Twitter')
print(f"After add 'Twitter' it_companies have this items:\n {it_companies}\n")
it_companies.update(['Samsung', 'Tencent', 'Salesforce', 'Adobe', 'Cisco'])
print(f"after update it_companies have this items: \n{it_companies}\n")
it_companies.remove('Google')
print(f"after remove 'Google' it_companies have this items: \n{it_companies}\n")
print(f"We can remove an item from a set using 'remove()' method. If the item is not found 'remove()' method will raise errors, so it is good to check if the item exist in the given set. However, 'discard()' method doesn't raise any errors.\n")

# Level 2 - use non-mutating operations for display
union_ab = A.union(B)
intersection_ab = A.intersection(B)
is_a_subset_b = A.issubset(B)
are_disjoint = A.isdisjoint(B)
sym_diff = A.symmetric_difference(B)

print("A union B:", union_ab)
print("A intersection B:", intersection_ab)
print("Is A subset of B?", is_a_subset_b)
print("Are A and B disjoint?", are_disjoint)
print("Symmetric difference between A and B:", sym_diff)

# If you want to delete both sets:
del A, B

#practise level3
Age_set = set(age)
print("Length of 'Age set' : %d" %len(Age_set))
print("Length of 'age list' : %d" %len(age))

if len(Age_set)>len(age) :
    print("'Age set' is bigger")
if len(Age_set)<len(age) :
    print("'Age list' is bigger")
else :
    print(f"'Age set' and 'Age list' are the same")

print("Explain the difference data types:")
print("字串(String/str)")
print("中文解釋 :由字元組成的有序序列,用於表示文字,不可變")
print("English Explain : An ordered sequence of characters used to represent text,immutable")
print("陣列(List)")
print("中文解釋 : 有序且可變的元素集合,允許不同型別與重複元素,支援索引與切片")
print("English Explain : An ordered, mutable collection of elements that can contain different types and duplicates, supports indexing and slicing")
print("元組(Tuple)")
print("中文解釋 : 有序且不可變的元素集合，常用於固定長度的資料或作為函式回傳多個值")
print("English Explain : An ordered, immutable collection of elements, often used for fixed-size data or returning multiple values from functions.")
print("集合(Set)")
print("中文解釋 : 無序且元素唯一的集合，適合去重與高效的成員查詢與集合運算（交集、聯集等）。")
print("Englist Expalin : An unordered collection of unique elements, suitable for deduplication and efficient membership tests and set operations (intersection, union, etc.).")

sentence = "I am a teacher and I love to inspire and teach people"
sentence_set = sentence.split()
print("I am a teacher and I love to inspire and teach people.")
print("This sentence have %d unique words" %len(sentence_set))