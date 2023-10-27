import json

with open('values.json', 'r') as values_file, open('tests.json', 'r') as tests_file:
    values_data = json.load(values_file)
    tests_data = json.load(tests_file)

values_dict = {}
def get_values_dict(data):
    for item in data:
        id = item['id']
        value = item['value']
        values_dict[id] = value
        if 'values' in item:
            get_values_dict(item['values'])

get_values_dict(values_data['values'])

def update_values(data):
    for item in data:
        id = item['id']
        if id in values_dict:
            item['value'] = values_dict[id]
        if 'values' in item:
            update_values(item['values'])

update_values(tests_data['tests'])

with open('report.json', 'w') as report_file:
    json.dump(tests_data, report_file, indent=4)

print("Файл report.json создан.")
