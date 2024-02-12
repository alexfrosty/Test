from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    benutzername = request.form['benutzername']
    return f'Der eingegebene Benutzername ist: {benutzername}'

if __name__ == '__main__':
    app.run(debug=True)
