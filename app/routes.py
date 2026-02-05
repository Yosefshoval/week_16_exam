from fastapi import APIRouter, HTTPException
from pymongo import errors 
from dal import *

router = APIRouter()

@router.get(' /employees/engineering/high-salary')
def high_salary():
    try:
        result = get_engineering_high_salary_employees()
        return result
    except errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/employees/by-age-and-role')
def by_age_and_role():
    try:
        result = get_employees_by_age_and_role()
        return result
    except errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/employees/top-seniority')
def top_seniority():
    try:
        result = get_top_seniority_employees_excluding_hr()
        return result
    except errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/employees/age-or-seniority')
def age_or_seniority():
    try:
        result = get_employees_by_age_or_seniority()
        return result
    except errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/employees/managers/excluding-departments')
def excluding_departments():
    try:
        result = get_managers_excluding_departments()
        return result
    except errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get('/employees/by-lastname-and-age')
def by_lastname_and_age():
    try:
        result = get_employees_by_lastname_and_age()
        return result
    except errors.PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))
