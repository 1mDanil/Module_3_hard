data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_sum(data):
    total = 0
    if isinstance(data, int):
        total += data
    elif isinstance(data, str):
        total += len(data)
    elif isinstance(data, (list, tuple, set)):
        for item in data:
            total += calculate_sum(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            total += len(str(key))
            total += calculate_sum(value)
    return total

result = calculate_sum(data_structure)
print(result)