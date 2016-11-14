class CocaCola:
    formula = ['a','b','c','d']

    def __init__(self):
        print('init')

    def drink(self):
        print('Energy!')


c = CocaCola()
c.tile = '可口可乐'
print(c.formula)
print(c.tile)

d = CocaCola()
print(d.formula)
d.drink()

#inheritance
class subCocaCola(CocaCola):
    taste = ['good']

e = subCocaCola()
print(e.taste)
e.drink()

class TestA:
    attr = 1
    def __init__(self):
        self.attr = 42
obj_a = TestA
