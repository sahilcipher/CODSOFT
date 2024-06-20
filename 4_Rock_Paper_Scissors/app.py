from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Website Routes
@app.route('/', methods=["GET", "POST"])
def root():
    if request.method == "POST":
        comp = random_value()
        user = request.form['name'].upper()
        choice = request.form['choice']
        result = check_result(comp, choice)
        return render_template('index.html',computer = comp, user = user, choice = choice, result = result)
    else:
        return render_template('index.html')


# For finding random choice from computer
def random_value():
    choice = random.choice([1, 2, 3])
    if choice == 1:
        value = "Rock"
    elif choice == 2:
        value = "Paper"
    elif choice == 3:
        value = "Scissor"
    else:
        print("Something went wrong, please refresh the page!")
    return value

# Method for Result Check
def check_result(comp, choice):
    if comp == choice:
        return "Draw!"
    elif (comp == "Rock" and choice == "Scissor") or \
            (comp == "Paper" and choice == "Rock") or \
            (comp == "Scissor" and choice == "Paper"):
        return "You Lose!"
    else:
        return "You Win!"




if __name__ == '__main__':
    app.run(debug=True)
