#.update({_:_,_:_}) добавление нескольких пар
# .get(ключ) вывод значения, несуществующее значение ошибки не выдает
# .pop() удаляет ключ, можно сохранять значение a = x.pop()
# del x[] - удаление ключа
# .items() - вывод ключ и значение
# .values() - вывод значения
# .keys() - вывод ключа
# .add() - добавление элемента
# .discard() .remove() Удаляет элемент. .discard не выдает ошибку
# Множеста {} не повторяет элементы
my_dict = {'Ruslan': 1996, 'Nikita': 1998, 'Sara': 1990}
print(my_dict)
print(my_dict.get('Ruslan'))
print(my_dict.get('Jenya'))
my_dict.update({'Marina': 2000,
                'Jenya': 1996})
a = my_dict.pop('Ruslan')
print(a)
my_set = {123, 'Morgan', True, 789, 123, 'Misha', 'Morgan'}
print(my_set)
my_set.add(456)
my_set.add('Masha')
my_set.remove(123)
print(my_set)
