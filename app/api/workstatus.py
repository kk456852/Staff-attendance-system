from flask import Blueprint, json, jsonify, request, current_app

from ..model import User
from .util import failed, login_required, success, Role, url
from ..model import SignSheet

bp = Blueprint('workstatus', __name__, url_prefix='/workstatus')

@bp.route('/', methods=['GET'])
@url
def workstatus():
    if request.method == 'GET':#根据ID查看
        staffID = request.args.get('staffID')
        date = request.args.get('date')
        staffArrengement = SignSheet.ByStaffIDandDate(staffID, date)[0]
        return success(staffArrengement.dict())
