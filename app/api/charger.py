from flask import Blueprint, request

from .auth import login_required

from ..model import Role

bp = Blueprint('charger', __name__, url_prefix='/charger')


@bp.route('/', methods=('GET', 'POST'))
@login_required(Role.CHARGE)
def charger_index():
    pass


@bp.route('/checkstaff', methods=('GET', 'POST'))
@login_required(Role.CHARGE)
def check_staff():
    pass


@bp.route('/arrangestaff', methods=('GET', 'POST'))
@login_required(Role.CHARGE)
def arrange_staff():
    pass


@bp.route('/apppro', methods=('GET', 'POST'))
@login_required(Role.CHARGE)
def application_process():
    pass


@bp.route('/arrangeschedual', methods=('GET', 'POST'))
def arrange_schedual():
    pass


@bp.route('/checkcktable', methods=('GET', 'POST'))
@login_required(Role.CHARGE)
def checktable():
    pass
