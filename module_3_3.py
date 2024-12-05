calls = 0
def count_calls():
    global calls
    calls += 1
    return None

def string_info(string):
    count_calls()
    argument = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return argument, upper_case, lower_case

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    return any(item.lower() == string_lower for item in list_to_search)

print(string_info('cat'))
string_info('dog')
print(string_info('home'))
print(is_contains('cake', ['cool', 'cak', 'CAKE']))
print(is_contains('Urban', ['ban', 'Urban', 'rba']))
is_contains('work', ['home', 'Homework', 'me'])
count_calls()
print(calls)


