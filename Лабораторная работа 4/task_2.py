# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as f:
        data = csv.DictReader(f, delimiter=",")
        with open(OUTPUT_FILENAME, 'w',) as w:
            output = []
            for line_ in data:
                output.append(line_)
            json.dump(output, w, indent=4)



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
