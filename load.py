import json 
from database import connect_db
# from database import connect_db

def save_json(data):

    with open("output/cleaned_employees.json","w") as file:

        json.dump(data,file,indent=4)

def save_kpi(kpi):

    with open("output/employee_kpi.json","w") as file:

        json.dump(kpi,file,indent=4)



def insert_employee(employees):

    connection = connect_db()
    cursor = connection.cursor()

    query = """
    INSERT INTO employees
    (id, name, department, old_salary, increment, new_salary, rating, email)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    for emp in employees:
        cursor.execute(query, (
            emp["id"],
            emp["name"],
            emp["department"],
            emp["old_salary"],
            emp["increment"],
            emp["new_salary"],
            emp["rating"],
            emp["email"]
        ))

    connection.commit()
    cursor.close()
    connection.close()

