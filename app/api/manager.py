from flask import Blueprint, json, jsonify, request

from .util import login_required

bp = Blueprint('manager', __name__, url_prefix='/manager')


@bp.route('/checkstaff', methods=['GET'])
def check_staff():
    pass


@bp.route('/updatestaff', methods=['PUT'])
def update_staff():
    pass
