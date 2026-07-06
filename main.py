

#export 
import json 
with open("JSON/employees.json", 'r') as f:
    x = json.load(f)


#Transform 

for emp in x:
    if (emp["department"] == ""):
        emp["department"] = "GENERAL"
    # print(emp["department"])


for emp in x:
    emp["name"] = emp["name"].strip().title()
    department = str(emp.get("department") or "").strip().upper()
    emp['email'] = emp["email"].strip().lower()
    # print(department)
    # print(emp['email '])


y = set()    # y = {101,102,103, 104, 105}
cleaned_data = []     # lst = [{1},{2},{3},{4},{5}]
for i in x:
    if i['id'] not in y:
        y.add(i["id"])
        cleaned_data.append(i)
total_records = len(x)
valid_records = len(cleaned_data)


for i in cleaned_data:
    if i['salary'].isdigit():
        i["salary"] = int(i["salary"])
    else:
        i['salary'] = 0

# def increment():
#     for i in cleaned_data:
        # old_salary = i["salary"] 
        # increment = old_salary * 0.10     
        # new_salary = old_salary + increment
#         lst1 = [old_salary , increment , new_salary]
#     return lst1
# for i in cleaned_data:
#     print(increment(i["salary"]))

for i in cleaned_data:
    old_salary = i["salary"] 
    increment = old_salary * 0.10     
    new_salary = old_salary + increment
    i["old_salary"] = old_salary
    i["new_salary"] = new_salary
    i["increment"] = increment
# print(cleaned_data)

for i in cleaned_data:
    if "@" not in i['email']:
        i["email"] = "Invaid email"
    # print(i["email"])

for i in cleaned_data:
   high_rating = list(filter(lambda emp: emp["rating"]>=80,cleaned_data))
print(len(high_rating))

for i in cleaned_data:
    print(i)
from functools import reduce  

Total_increment = reduce( lambda total,emp : total + emp["increment"],cleaned_data,0)
print(Total_increment)

Total_salary = reduce( lambda total,emp : total + emp["new_salary"],cleaned_data,0)
# print(Total_salary)

Highest_salary = max(list(i["new_salary"] for i in cleaned_data))
Highest_salary = min(list(i["new_salary"] for i in cleaned_data))
avg_inc = Total_increment // valid_records
print(avg_inc)
# Highest_salary = avg(list(i["new_salary"] for i in cleaned_data))
# print(Highest_salary)
# lowest_salary = 
