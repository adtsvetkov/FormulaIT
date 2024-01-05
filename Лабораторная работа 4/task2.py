# TODO импортировать необходимые молули
from csv import DictReader
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as csv_file:
        read_csv = DictReader(csv_file)
        json_file = []
        for row in read_csv:
            json_file.append(row)
    with open(OUTPUT_FILENAME, 'w') as f:  # TODO Сериализовать в файл с отступами равными 4
        json.dump(json_file, f, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
