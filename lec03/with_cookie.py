from flask import render_template, Flask, request, redirect, url_for

import typing as t
app = Flask(__name__)


USERNAME: str = "juwoong"

@app.route('/login', methods=['POST', 'GET'])
def logins():
    if request.method == 'GET':
        return render_template('login.html')
    
    form_id = request.form.get('id')
    form_password = request.form.get('password')

    resp = redirect(url_for('index'))
    if form_id == "hello" and form_password == "world":
        resp.set_cookie('username', USERNAME)
    
    return resp

@app.route('/logout')
def logout(): 
    resp = redirect(url_for('index'))
    resp.set_cookie('username', "", expires=0)

    return resp

@app.route('/')
def index():
    username: t.Optional[str] = request.cookies.get('username')
    is_login: bool = username is not None

    message = "로그인 상태가 아닙니다."
    if is_login:
        message = f"안녕하세요, {username} 님!"

    return render_template('index.html', is_login=is_login, message=message)

if __name__ == "__main__":
    app.run(debug=True)
