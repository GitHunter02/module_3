# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(2)

# 2.Распаковка параметров:
values_list = [True, 5, 'Marshall']
values_dict = {'a': 22, 'b': 'Marshall', 'c': False}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list2 = ['book', 2]
print_params(*values_list2, 42)
