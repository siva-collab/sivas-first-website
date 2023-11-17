from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': "Data Analyst",
    'location': "Coimbatore",
    'salary': "1,00,000"
}, {
    'id': 2,
    'title': "Data Engineer",
    'location': "Erode",
}, {
    'id': 3,
    'title': "Data Scientist",
    'location': "Chennai",
    'salary': "1,50,000"
}, {
    'id': 4,
    'title': "Data Manager",
    'location': "Noida",
    'salary': "1,25,000"
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name='Siva')


@app.route("/a/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
