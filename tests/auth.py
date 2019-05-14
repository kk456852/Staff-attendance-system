from flask import request,json

login_test_data = {
    'UserId':123,
    'password':'123'
}

def login_test():
    s = request
    r = s.post('http://127.0.0.1:5000/auth/login',json.dumps(login_test_data))
    print(r.text)

login_test()