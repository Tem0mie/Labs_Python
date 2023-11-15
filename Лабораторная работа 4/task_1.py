# TODO решите задачу
import json
def task() -> float:
    input_file = 'input.json'
    with open(input_file, "r") as f:
        data = json.load(f)
        proisv = 0
        sum = 0
        score = [line["score"] for line in data]
        weight = [line["weight"] for line in data]
        for a in range(0, len(score)):
            proisv = score[a] * weight[a]
            sum += proisv
    return (sum)

print(round(task(),3))
