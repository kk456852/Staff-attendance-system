from flask import Blueprint, json, jsonify, request, current_app

from ..model import User
from .util import failed, login_required, success, Role

bp = Blueprint('staff', __name__, url_prefix='/staff')


@bp.route('/all', methods=['GET'])
# @login_required(Role.Manager)
def all_staffs():
    try:
        return success({
            "staffs": [x.dict() for x in User.All() if x.role is not Role.MANAGER]
        })
    except Exception as e:
        current_app.logger.debug(e)
        return failed()


@bp.route('/<int:ID>', methods=['GET'])
# @login_required(Role.Manager)
def staff_info(ID):
    try:
        return success(User.ByID(ID).dict())
    except Exception as e:
        current_app.logger.debug(e)
        return failed()


@bp.route('/<int:ID>', methods=['POST'])
# @login_required(Role.Manager)
def staff_updateinfo():
    try:
        request_data = request.get_json()
    except Exception as e:
        pass


@bp.route('/', methods=('GET', 'POST'))
def staff_index():
    if loged_Veri(request.id) == 0:
        return "This is staff index page"


@bp.route('/checkschedule', methods=('GET', 'POST'))
def staff_check_schedule():
    if loged_Veri(request.id) == 0:
        return "This page will show the schedule of staff"


@bp.route('/leave', methods=('GET', 'POST'))
def staff_leave():
    if loged_Veri(request.id) == 0:
        return "This page will show the form of leave request!"


@bp.route('/leaveabense', methods=('GET', 'POST'))
def staff_leave_abense():
    if loged_Veri(request.id) == 0:
        return "This functiom will getting hhe leave absense of some staff down"


@bp.route('/checkrecord', methods=('GET', 'POST'))
def staff_check_record():
    if loged_Veri(request.id) == 0:
        return "This function will return the result of the staff_check_record"


@bp.route('/overtimeapply', methods=('GET', 'POST'))
def staff_overtime_apply():
    if loged_Veri(request.id) == 0:
        return "staff apply for the overtime"
