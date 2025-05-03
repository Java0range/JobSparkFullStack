from flask import Blueprint


blueprint = Blueprint("Resumes", __name__, url_prefix="/resumes")


@blueprint.route("", methods=["GET"])
async def get_resumes():
    pass