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


@app.route('/Assignment9', methods=['GET', 'POST'])
def Assignment9():
    name = 'NONE'
    Users = {"Yaara": "Cohen", "Roni": "Dalumy", "Itamar": "Shmitamar", "Shira": "Levi", "Daniel": "Zehavi","Or": "Bor"}
    username = ' '
    logged_in = True


    if request.method == 'GET':
        if 'name' in request.args:
            name = request.args['name']

    if request.method == 'POST':
        username = request.form['username']
        session['logged_in'] = True
        session['username'] = username


    return render_template('Assignment9.html',
                           request_method=request.method,
                           name = name,
                           Users = Users,
                           username = username)

@app.route('/log_out')
def log_out():
    session.pop('username')
    session['logged_in'] = False
    return redirect('/Assignment9')


@app.route('/Class10', methods=['GET', 'POST'])
def class10_func():
    username = ''
    second_name = ''
    if request.method == 'POST':
        # way to get to secured data - check in DB of the website
        session['logged_in'] = True
        username = request.form['username']
        session['username'] = username

    if request.method == 'GET':
        if 'second_name' in request.args:
            second_name = request.args['second_name']

    return render_template('Class10.html',
                           request_method=request.method,
                           username=username,
                           second_name=second_name)


if __name__ == '__main__':
    app.run(debug=True)
