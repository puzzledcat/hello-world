#数组， 字典， 元组， 集合

all_in_list = [
    1,
    1.0,
    'a word',
    print(1),
    True,
    [1,2],
    (1,2), #元组
    {'key':'value'}#字典
]
print(all_in_list[-1])

fruit = ['pineapple','pear']
fruit.insert(1,'grape')
print(fruit)

fruit[0:0] = ['Orange']
print(fruit)

del fruit[0:2]
print(fruit)

#推倒时
b = [i for i in range(1,10)]
print(b)

a = [i**2 for i in range(1,10)]
print(a)
k = [n for n in range(1,10) if n % 2 == 0]
print(k)

d = {i:i+1 for i in range(1,4)}
g = {i:j for i,j in zip(range(1,4),'abc')}

letters = ['a','b','c']
for num,letter in enumerate(letters):
    print(letter,'is', num + 1)

