from flask import Blueprint, current_app

from ..model import Department
from .util import failed, login_required, success, Role

bp = Blueprint('departments', __name__, url_prefix='/departments')


@bp.route('/', methods=['GET'])
# @login_required(Role.Manager)
def all_department():
    try:
        return success('所有的部门信息')
    except Exception as e:
        current_app.logger.exception(e)
        return failed()


