def print_params(a=1, b='строка', c=True):
  print(a, b, c)

# 1. Вызовы с разным количеством аргументов
print_params()
print_params(10)
print_params(10, 'str')
print_params(10, 'str', False)

# Проверка вызова с ключевыми аргументами
print_params(b = 25)
print_params(c = [1, 2, 3])

# 2. Распаковка параметров
values_list = [4, 'text', False]
values_dict = {'a': 100, 'b': 'new text', 'c': True}
print_params(*values_list)
print_params(**values_dict)

# 3. Распаковка + отдельны параметры
values_list_2 = [54.32, 'str']
print_params(*values_list_2, 42)
