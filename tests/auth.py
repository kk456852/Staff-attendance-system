from flask import request,json

login_test_data = {
    'UserId':123,
    'password':'123'
}

def login_test():
    s = request
    s.post('http://127.0.0.1:5501/auth/login',json.dumps(login_test_data))
