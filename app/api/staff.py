from flask import Blueprint, request

from .auth import loged_Veri

bp = Blueprint('staff', __name__, url_prefix='/staff')


@bp.route('/', methods=['GET','POST'])
def staff_index():
    if loged_Veri(request.id) == 0:
        return "This is staff index page"


@bp.route('/checkschedule', methods=['GET','POST'])
def staff_check_schedule():
    if loged_Veri(request.id) == 0:
        return "This page will show the schedule of staff"


@bp.route('/leave', methods=['GET','POST'])
def staff_leave():
    if loged_Veri(request.id) == 0:
        return "This page will show the form of leave request!"


@bp.route('/leaveabense', methods=['GET','POST'])
def staff_leave_abense():
    if loged_Veri(request.id) == 0:
        return "This functiom will getting hhe leave absense of some staff down"


@bp.route('/checkrecord', methods=['GET','POST'])
def staff_check_record():
    if loged_Veri(request.id) == 0:
        return "This function will return the result of the staff_check_record"


@bp.route('/overtimeapply', methods=['GET', 'POST'])
def staff_overtime_apply():
    if loged_Veri(request.id) == 0:
        return "staff apply for the overtime"


@bp.route('/updateinfo', methods=['GET', 'POST'])
def staff_updateinfo():
    if loged_Veri(request.id) == 0:
        return "update information of the user and refresh the page"
