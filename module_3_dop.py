data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(data):
    sum = 0
    for elem in data:
        if isinstance(elem, (int, float)):
            sum += elem
        elif isinstance(elem, str):
            sum += len(elem)
        elif isinstance(elem, (tuple, set, list)):
            sum += calculate_structure_sum(elem) #Ведет подсчет elem внутри последовательностей, проходя по верхним if elif
        elif isinstance(elem, dict):
            sum += calculate_structure_sum(elem.items()) #Ведет подсчет elem внутри словаря, проходя по верхним if elif
    return sum


print(calculate_structure_sum(data_structure))
