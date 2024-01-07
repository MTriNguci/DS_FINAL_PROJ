from flask import Flask, request, render_template
from process import handle_input

app = Flask(__name__)

def format_number(num):
    return '{:,}'.format(num).replace(',', ' ')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form
        result_rf, result_knn = handle_input(data)
        result_rf = format_number(result_rf)
        result_knn = format_number(result_knn)
        return  (
        f'<h1>Giá xe dự đoán bằng RandomForestRegression là: {result_rf} EUR</h1>'
        f'<h1>Giá xe dự đoán bằng KNNRegression là: {result_knn} EUR</h1>'
        )
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)



