import json
from datetime import date


def extract_date(date):
    year = date.split('-')[0]
    month = date.split('-')[1]
    day = date.split('-')[2]

    return int(year), int(month), int(day)


try:
    result = open('result.json')
    config = json.load(result)
except IOError:
    print('Arquivo inexistente')
    config = []

diffs = []

for repo in config:
    code_date = extract_date(repo['code'])
    bdd_date = extract_date(repo['bdd'])

    dcode = date(code_date[0], code_date[1], code_date[2])
    dbdd = date(bdd_date[0], bdd_date[1], bdd_date[2])

    diff = dcode - dbdd

    delta = {"project": repo['project'], "delta": diff.days}
    diffs.append(delta)

with open('result_delta.json', 'w') as f:
    json.dump(diffs, f)


