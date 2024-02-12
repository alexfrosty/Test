from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        number = float(request.form['number'])
        # Hier kannst du die Verarbeitung durchführen, z.B.:
        result = number * 2
        return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
