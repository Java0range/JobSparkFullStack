from flask import Blueprint, request, abort, Response
from src.resumes.orm import ResumeORM
from src.schemas.schemas import CreateResumeSchema
from src.auth.dependencies import get_user_id


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


@blueprint.route("/<resume_id>", methods=["GET"])
async def get_resume_by_id(resume_id: int):
    resume_id = int(resume_id)
    if resume_id and resume_id > 0:
        return await ResumeORM.get_resumes_for_id(resume_id=resume_id)
    abort(Response("Bad request", 406))


@blueprint.route("", methods=["POST"])
async def create_resume():
    data = request.json
    input_json = CreateResumeSchema.model_validate(data)
    user_id = await get_user_id(request)
    if not user_id:
        abort(Response("Invalid user id", 406))
    if (input_json.name
        and user_id
        and input_json.surname
        and input_json.job_name
        and input_json.education
        and input_json.edu_institution
        and input_json.city
    ):
        ans = await ResumeORM.insert_resume(
            name=input_json.name,
            user_id=user_id,
            surname=input_json.surname,
            job_name=input_json.job_name,
            description=input_json.description,
            education=input_json.education,
            experience=input_json.experience,
            educational_institution=input_json.edu_institution,
            faculty=input_json.faculty,
            expected_salary=input_json.expected_salary,
            city=input_json.city,
            phone_number=input_json.phone_number,
            email=input_json.email,
            telegram_username=input_json.telegram_username
        )
        if ans is None:
            return "ok"
        abort(Response(ans, 406))
    abort(Response("Bad request", 400))


@blueprint.route("", methods=["PUT"])
async def update_resume():
    data = request.json
    input_json = CreateResumeSchema.model_validate(data)
    user_id = await get_user_id(request)
    if not user_id:
        abort(Response("Invalid user id", 406))
    await ResumeORM.update_resume(
        name=input_json.name,
        user_id=user_id,
        surname=input_json.surname,
        job_name=input_json.job_name,
        description=input_json.description,
        education=input_json.education,
        experience=input_json.experience,
        educational_institution=input_json.edu_institution,
        faculty=input_json.faculty,
        expected_salary=input_json.expected_salary,
        city=input_json.city,
        phone_number=input_json.phone_number,
        email=input_json.email,
        telegram_username=input_json.telegram_username
    )
    return "ok"