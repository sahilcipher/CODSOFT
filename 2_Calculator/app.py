from flask import Flask, request, render_template

app = Flask(__name__)

# route for website
@app.route('/', methods=["GET", "POST"])
def root():
    total = None
    if request.method == "POST":
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            # Condition for checking operation
            if operation == "add":
                total = num1 + num2
            elif operation == "sub":
                total = num1 - num2
            elif operation == "multi":
                total = num1 * num2
            elif operation == "div":
                total = num1 / num2
            else:
                print("Something wents wrong, please try again!")
        except (ValueError, KeyError):
            total = 'Invalid input'

    return render_template('index.html', total=total)

if __name__ == '__main__':
    app.run(debug=True)
