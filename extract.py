import json

def extract_data(file_name):

    with open("JSON/employees.json", 'r') as f:
        employees = json.load(f)

    return employees