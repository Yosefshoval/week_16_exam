from connection import Collection

def conver_id_to_string(doc):
    if not doc:
        return None
    if "_id" in doc:
        doc["_id"] = str(doc["_id"])

def convert_multiple_doc(docs):
    return [conver_id_to_string(doc) for doc in docs]


def get_engineering_high_salary_employees():
    result = Collection.find(
        {'$and' [
            {'job_role.department' : 'Engineering'}, 
            {'salary': {'$gt':65000}}
            ]},
        {'employee_id': 1, 'name': 1, 'salary' : 1}
        )
    result = convert_multiple_doc(result)
    return result



def get_employees_by_age_and_role():
    result = Collection.find(
        {'$and' [
            {{'age' : {'$gte' : 30}}, 
             {'age' : {'$lte' : 45}}
             }, 
            {'job_role.title' : 
                {'$in' : ['Engineer', 'Specialis']}}
            ]},
        {'employee_id': 1, 'name': 1, 'salary' : 1}
        )
    result = convert_multiple_doc(result)
    return result

    
def get_top_seniority_employees_excluding_hr():
    result = Collection.find(
        {'$ne' : {'job_role.department' : 'HR'}}
    ).sort('years_at_company', -1).limit(7)

    result = convert_multiple_doc(result)
    return result


def get_employees_by_age_or_seniority():
    result = Collection.find(
        {'$or' [
            {'age' : {'$gt' : 50}}, 
            {'years_at_company' : {'$lt' : 3}}
            ]},
        {'employee_id' : 1, 'name' : 1, 'age' : 1, 'years_at_company' : 1}
        )

    result = convert_multiple_doc(result)
    return result


def get_managers_excluding_departments():
    result = Collection.find(
        {'$and': [
            {'job_role.title' : 'Manager'}, 
            {'$nin' : ['Sales', 'Marketing']
             }
             ]}
        )
    
    result = convert_multiple_doc(result)
    return result
