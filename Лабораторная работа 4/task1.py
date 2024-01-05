import json

INPUT_FILENAME = 'input.json'


# TODO решите задачу
def task() -> float:
    with open(INPUT_FILENAME) as file:
        json_file = json.load(file)
    counter = 0
    for dictionary in json_file:
        counter += dictionary['score'] * dictionary['weight']
    return round(counter, 3)


print(task())
