from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():  # put application's code here
    user = {
        'username': '沈奇男'
    }
    return render_template('login.html', user=user)


if __name__ == '__main__':
    app.run()
