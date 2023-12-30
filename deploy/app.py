from flask import Flask, request, url_for
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        print(name)
        input = request.form.get('model_input')
        print(input)
        loai = request.form.get('loai')
        print(loai)
        return '<h1>Xin chào, {}!</h1>'.format(name)
    return '''
        <html>
        <head>
            <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='style.css') + '''">
        </head>
        <body>
            <form method="POST">
                Tên của bạn: <input type="text" name="name">
                Input cho mô hình: <input type="text" name="model_input">
                Loại: <select name="loai">
                    <option value="a">a</option>
                    <option value="b">b</option>
                    <option value="c">c</option>
                </select>
                <input type="submit" value="Gửi">
            </form>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
