from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
@app.route("/")
def hello_world():
    day_of_week = datetime.today().strftime('%A')
    return render_template("index.html", day_of_week=day_of_week)

@app.route("/submit", methods=['POST'])
def submit():
    print('taking input from user')
    form_data = dict(request.form)

    return form_data

@app.route("/api/<name>")
def dynamic_route(name):
    result = "<p>Hello " +name+ "</p>"
    return result

@app.route("/query-params")
def query_param():
    name = request.values.get("user")
    result = "<p>Hello " +name+ "</p>"
    return result



if __name__ == '__main__':
    app.run(debug=True)