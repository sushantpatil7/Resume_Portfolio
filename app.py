from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test")
def test():
    return "hello testing is in "

@app.route("/personal")
def personal():
    return render_template("personal.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/work")
def work():
    return render_template("work.html")


if __name__ == '__main__':
    app.run(debug=True)