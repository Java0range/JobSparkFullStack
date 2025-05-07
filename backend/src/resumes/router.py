from flask import Blueprint, request
from src.resumes.orm import ResumeORM


blueprint = Blueprint("Resumes", __name__, url_prefix="/resumes")


@blueprint.route("", methods=["GET"])
async def get_resumes():
    words_list = request.args.get('words').split(";") if request.args.get('words') else []
    city = request.args.get('city') if request.args.get('city') else ""
    salary_from = int(request.args.get('expected_salary_from')) if request.args.get('expected_salary_from') else 0
    salary_to = int(request.args.get('expected_salary_to')) if request.args.get('expected_salary_to') else 1_000_000_000
    experience_from = int(request.args.get('experience_from')) if request.args.get('experience_from') else 0
    resumes = await ResumeORM.get_resumes_for_filter(
        words_list=words_list,
        city=city,
        experience_from=experience_from,
        expected_salary_from=salary_from,
        expected_salary_to=salary_to
    )
    return resumes