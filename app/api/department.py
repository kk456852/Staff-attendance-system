from flask import Blueprint, current_app

from ..model import Department
from .util import failed, login_required, success, Role, url

bp = Blueprint('departments', __name__, url_prefix='/departments')


@bp.route('/', methods=['GET'])
@url
def all_department():
    return [d.dict() for d in Department.All()]
