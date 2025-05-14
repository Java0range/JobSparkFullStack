from flask import Blueprint, request, abort, Response
from src.auth.dependencies import get_user_id
from src.employers.orm import EmployersORM
from src.employers.schemas import CreateEmployerSchema


blueprint = Blueprint("Employers", __name__, url_prefix="/employers")


@blueprint.route("", methods=["GET"])
async def get_employers():
    words_list = request.args.get('words').split(";") if request.args.get('words') else []
    remotely = request.args.get('remotely') if request.args.get('remotely') else False
    city = request.args.get('city') if request.args.get('city') else ""
    salary_from = int(request.args.get('salary')) if request.args.get('salary') else 0
    experience_from = int(request.args.get('experience')) if request.args.get('experience') else 0
    employers = await EmployersORM.get_employers_for_filter(
        words_list=words_list,
        remotely=remotely,
        city=city,
        experience_from=experience_from,
        expected_salary_from=salary_from
    )
    return employers


@blueprint.route("", methods=["POST"])
async def create_employer():
    data = request.json
    input_json = CreateEmployerSchema.model_validate(data)
    user_id = await get_user_id(request)
    if not user_id:
        abort(Response("Invalid user id", 406))
    if (
        input_json.name
        and input_json.city
    ):
        await EmployersORM.insert_employer(
            name=input_json.name,
            user_id=1,
            salary=input_json.salary,
            work_experience=input_json.work_experience,
            remotely=input_json.remotely,
            description=input_json.description,
            city=input_json.city,
            phone_number=input_json.phone_number,
            email=input_json.email,
            telegram_username=input_json.telegram_username
        )
        return "ok"
    abort(Response("Bad request", 400))