from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("template.html")


@app.route("/get_cunt", methods=["GET"])
def template():
    get_cunt += 1
    return render_template("template.html", get_cunt)


def main():
    get_cunt = 0


if __name__ == "__main__":
    app.run(debug=True)
