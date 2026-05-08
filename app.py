from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    hcf = None
    lcm = None

    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        hcf = math.gcd(num1, num2)
        lcm = (num1 * num2) // hcf

    return render_template('index.html', hcf=hcf, lcm=lcm)

if __name__ == '__main__':
    app.run(debug=True)
