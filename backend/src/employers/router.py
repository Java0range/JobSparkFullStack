from flask import Blueprint


blueprint = Blueprint("Employers", __name__, url_prefix="/employers")


@blueprint.route("", methods=["GET"])
async def get_employers():
    pass