from flask import Flask, render_template, request, redirect, url_for
import scraping

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def data_get():
    web_array = []
    target = request.form['target']
    users = request.form['users']

    if target == 'はてなブックマーク':
        web_array = scraping.get_hatebu(users)

    return render_template('list.html', target=target, web_array=web_array)


if __name__ == '__main__':
    app.run(debug=True)