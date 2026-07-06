from extract import extract_data
from transform import * 
from load import *
import logging

employees = extract_data("employees.json")
total_records = len(employees)
employees = list(map(clean_text,employees))
employees = remove_duplicates(employees)
# employees = validate_duplicate
employees = validate_salary(employees)
employees = validate_email(employees)
employees = list(map(increment_salary,employees))
kpi = generate_kpi(employees,total_records)

save_json(employees)

save_kpi(kpi)

insert_employee(employees)