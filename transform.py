from extract import * 
import re
from functools import reduce 


#celaned Text
def clean_text(employee):

    employee["name"] = employee["name"].strip().title()

    if employee["department"]:
        employee["department"] = employee["department"].strip().upper()
    else:
        employee["department"] = "GENERAL"

    employee["email"] = employee["email"].strip().lower()

    return employee
# print(clean_text(x))

def remove_duplicates(employees):

    seen = set()

    cleaned = []

    for emp in employees:

        if emp["id"] not in seen:

            cleaned.append(emp)

            seen.add(emp["id"])

    return cleaned

def validate_salary(employees):

    valid = []

    for emp in employees:

        if emp["salary"].isdigit():

            emp["salary"] = int(emp["salary"])

            valid.append(emp)

    return valid

def validate_email(employees):

    valid = []

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    for emp in employees:

        if re.match(pattern, emp["email"]):

            valid.append(emp)

    return valid

def increment_salary(employee):

    employee["old_salary"] = employee["salary"]

    employee["increment"] = employee["salary"] * 0.10

    employee["new_salary"] = employee["salary"] + employee["increment"]

    return employee
def get_high_performers(employees):

    return list(filter(lambda x: x["rating"] >= 80, employees))
    
def generate_kpi(employees, total_records):

    total_increment = reduce(
        lambda total, emp: total + emp["increment"],
        employees,
        0
    )

    highest_salary = max(emp["new_salary"] for emp in employees)

    lowest_salary = min(emp["new_salary"] for emp in employees)

    return {
        "total_records": total_records,
        "valid_records": len(employees),
        "high_performers": len(get_high_performers(employees)),
        "total_increment": total_increment,
        "highest_salary": highest_salary,
        "lowest_salary": lowest_salary
    }