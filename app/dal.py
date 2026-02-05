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
            {'$or' : [
                {'job_role.department' : 'Engineer'}, 
                {'job_role.department' : 'Specialist'}
                ]}
            ]},
        {'employee_id': 1, 'name': 1, 'salary' : 1}
        )
    result = convert_multiple_doc(result)
    return result

    
