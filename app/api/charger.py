from flask import Blueprint, request
from app.api.auth import loged_Veri
bp = Blueprint('charger', __name__, url_prefix='/charger')


@bp.route('/', methods=('GET', 'POST'))
def charger_index():
    if loged_Veri(request.id) == 1:
        return "This is staff index page"


@bp.route('/checkstaff', methods=('GET', 'POST'))
def check_staff():
    if loged_Veri(request.id) == 1:
        return "This page will show the schedule of staff"


@bp.route('/arrangestaff', methods=('GET', 'POST'))
def arrange_staff():
    if loged_Veri(request.id) == 1:
        return "This function will arrange timetable of staff"


@bp.route('/apppro', methods=('GET', 'POST'))
def application_process():
    if loged_Veri(request.id) == 1:
        return "This is funcction will process the applicaiton of leave of staff "


@bp.route('/arrangeschedual', methods=('GET', 'POST'))
def arrange_schedual():
    if loged_Veri(request.id) == 1:
        return "This url is for arrangeschedual"


@bp.route('/checkcktable', methods=('GET', 'POST'))
def checktable():
    if loged_Veri(request.id) == 1:
        return "This url is for checktable"

