from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/lessons")
def second():
    return render_template("lessons.html")

@app.route("/quizzes")
def third():
    return render_template("quizzes.html")

@app.route("/ecotasks")
def fourth():
    return render_template("ecotasks.html")

@app.route("/progress")
def fifth():
    return render_template("progress.html")

@app.route("/leaderboards")
def sixth():
    return render_template("leaderboards.html")



if __name__ == "__main__":
    app.run(debug=True)

