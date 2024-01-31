from flask import Flask, render_template
from datetime import datetime as dt
import requests

app = Flask(__name__)


@app.route("/guess/<name>")
def age(name):
    request_age = requests.get(f"https://api.agify.io?name={name}")
    age = request_age.json()["age"]

    request_gender = requests.get(f"https://api.genderize.io/?name={name}")
    gender = request_gender.json()["gender"]

    return render_template(
        'index.html',
        name=name.title(),
        age=age,
        gender=gender,
        current_year=dt.now().year
    )


if __name__ == '__main__':
    app.run(debug=True)
