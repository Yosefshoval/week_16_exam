from fastapi import APIRouter, HTTPException
from dal import *

router = APIRouter()

@router.get(' /employees/engineering/high-salary')
def high_salary():
    pass


@router.get('/employees/by-age-and-role')
def by_age_and_role():
    pass


@router.get('/employees/top-seniority')
def top_seniority():
    pass


@router.get('/employees/age-or-seniority')
def age_or_seniority():
    pass


@router.get('/employees/managers/excluding-departments')
def excluding_departments():
    pass

@router.get('/employees/by-lastname-and-age')
def by_lastname_and_age():
    pass
