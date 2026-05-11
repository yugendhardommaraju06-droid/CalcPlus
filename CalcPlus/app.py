from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    result = None
    error = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operator = request.form["operator"]

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                result = "Cannot divide by zero" if num2 == 0 else num1 / num2
        except:
            error = "Invalid input"

    return render_template("calculator.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)