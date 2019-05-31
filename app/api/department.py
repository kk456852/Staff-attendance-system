from flask import Blueprint, current_app

from ..model import Department
from .util import failed, login_required, success, Role

bp = Blueprint('departments', __name__, url_prefix='/departments')


@bp.route('/', methods=['GET'])
# @login_required()
def all_department():
    return success({"departments": [d.dict() for d in Department.All()]})
