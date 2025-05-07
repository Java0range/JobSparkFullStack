from flask import Blueprint, request
from src.employers.orm import EmployersORM


blueprint = Blueprint("Employers", __name__, url_prefix="/employers")


@blueprint.route("", methods=["GET"])
async def get_employers():
    words_list = request.args.get('words').split(";") if request.args.get('words') else []
    remotely = request.args.get('remotely') if request.args.get('remotely') else False
    city = request.args.get('city') if request.args.get('city') else ""
    salary_from = int(request.args.get('salary_from')) if request.args.get('salary_from') else 0
    salary_to = int(request.args.get('salary_to')) if request.args.get('salary_to') else 1_000_000_000
    experience_from = int(request.args.get('experience')) if request.args.get('experience') else 0
    employers = await EmployersORM.get_employers_for_filter(
        words_list=words_list,
        remotely=remotely,
        city=city,
        experience_from=experience_from,
        expected_salary_from=salary_from,
        expected_salary_to=salary_to
    )
    return employers