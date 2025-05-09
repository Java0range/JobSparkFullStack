from flask import Blueprint, request
from src.resumes.orm import ResumeORM


blueprint = Blueprint("Resumes", __name__, url_prefix="/resumes")


@blueprint.route("", methods=["GET"])
async def get_resumes():
    words_list = request.args.get('words').split(";") if request.args.get('words') else []
    city = request.args.get('city') if request.args.get('city') else ""
    salary_from = int(request.args.get('salary')) if request.args.get('salary') else 0
    experience_from = int(request.args.get('experience')) if request.args.get('experience') else 0
    resumes = await ResumeORM.get_resumes_for_filter(
        words_list=words_list,
        city=city,
        experience_from=experience_from,
        expected_salary_from=salary_from
    )
    return resumes