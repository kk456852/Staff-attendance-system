from flask import Blueprint,request,json
from url.auth import loged_Veri
from model.Employee import Employee
bp = Blueprint('staff',__name__,url_prefix='/staff')

@bp.route('/checkinfo',methods = ('GET'))
def staff_checkinfo():
    request_data = json.loads(str(request.get_data(), 'utf-8'))
    try:
        if loged_Veri(request_data['StaffId']) == 0:
            employee = Employee(request_data['StaffId'])
            data = employee.getinfo()
            response_data = {
                'result' : True,
                'status' : 220,
                'data' : data
            }
        else:
            response_data = {
                'result' : False,
                'status' : 520
            }
    except:
        response_data = {
            'result': False,
            'status': 521
        }
    response_data = json.dumps(response_data)
    return response_data

@bp.route('/updateinfo',methods = ('POST'))
def staff_updateinfo():
    request_data = json.loads(str(request.get_data(), 'utf-8'))
    try:
        if loged_Veri(request_data['StaffId']) == 0:
            employee = Employee(request_data['StaffId'])
            employee.Updateinfo(request_data['data'])
            response_data = {
                'result': True,
                'status': 221
            }
        else:
            response_data = {
                'result': False,
                'status': 520
            }
    except:
        response_data = {
            'result': False,
            'status': 522
        }
    response_data = json.dumps(response_data)
    return response_data


@bp.route('/',methods = ('GET','POST'))
def staff_index():
    if loged_Veri(request.id) == 0:
        return "This is staff index page"

@bp.route('/checkschedule',methods = ('GET','POST'))
def staff_check_schedule():
    if loged_Veri(request.id) == 0:
        return "This page will show the schedule of staff"

@bp.route('/leave',methods = ('GET','POST'))
def staff_leave():
    if loged_Veri(request.id) == 0:
        return "This page will show the form of leave request!"

@bp.route('/leaveabense',methods = ('GET','POST'))
def staff_leave_abense():
    if loged_Veri(request.id) == 0:
        return "This functiom will getting hhe leave absense of some staff down"

@bp.route('/checkrecord',methods = ('GET','POST'))
def staff_check_record():
    if loged_Veri(request.id) == 0:
        return "This function will return the result of the staff_check_record"

@bp.route('/overtimeapply',methods = ('GET','POST'))
def staff_overtime_apply():
    if loged_Veri(request.id) == 0:
        return "staff apply for the overtime"

