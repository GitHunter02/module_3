def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    elif first == 0:
        return get_multiplied_digits(str_number[1:])
    else:
        return first * get_multiplied_digits(str_number[1:]) if first * get_multiplied_digits(
            str_number[1:]) != 0 else first


result1 = get_multiplied_digits(40203)
print(result1)
result2 = get_multiplied_digits(402030)
print(result2)
