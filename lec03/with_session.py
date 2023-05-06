from flask import render_template, Flask, request, redirect, url_for, session

import typing as t
app = Flask(__name__)
app.secret_key = "secret_key"  # should be random bytes!


USERNAME: str = "juwoong"

@app.route('/login', methods=['POST', 'GET'])
def logins():
    if request.method == 'GET':
        return render_template('login.html')
    
    form_id = request.form.get('id')
    form_password = request.form.get('password')

    if form_id == "hello" and form_password == "world":
        session['username'] = USERNAME
    
    return redirect(url_for('index'))

@app.route('/logout')
def logout(): 
    session.pop('username')
    return redirect(url_for('index'))

@app.route('/')
def index():
    message = "로그인 상태가 아닙니다."
    is_login = 'username' in session
    if is_login:
        message = f"안녕하세요, {session['username']} 님!"

    return render_template('index.html', is_login=is_login, message=message)

if __name__ == "__main__":
    app.run(debug=True)
