from flask import Flask, request, render_template
import pandas as pd
from process import handle_input

app = Flask(__name__)

def format_number(num):
    return '{:,}'.format(num).replace(',', ' ')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form
        result = handle_input(data)
        result = format_number(result)
        return f'<h1>Giá xe dự đoán bằng RandomForestRegression là: {result} EUR</h1>'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)



