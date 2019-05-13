from flask import Flask
from url import auth,charger,manager,staff

app = Flask(__name__)
app.secret_key = 'TKK123'
app.register_blueprint(auth.bp)
app.register_blueprint(charger.bp)
app.register_blueprint(manager.bp)
app.register_blueprint(staff.bp)

@app.route("/hello")
def index():
    return "This is an index page"

if __name__ == "__main__":
   app.env = "development"
   app.debug = True
   app.run(port=5500)
