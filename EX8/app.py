from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/open')
@app.route('/')
def openPage():
    return render_template('cv.html')

@app.route('/contactMe')
def ContactMe():
    return render_template('ContactMe.html')

@app.route('/UserList')
def UsersList():
    return render_template('UsersList.html')

@app.route('/Assignment8')
def Assignment8():
    return render_template('Assignment8.html', hobby2='Cooking', name="Itamar", hobbies=['Crossfit','TV','Swimming'])

@app.route('/Assignment8New')
def Assignment8New():
    return render_template('Assignment8New.html', hobby2='Cooking', name="Itamar", hobbies=['Crossfit','TV','Swimming'])


if __name__ == '__main__':
    app.run(debug=True)
