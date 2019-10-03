from flask import Flask, render_template

app = Flask(__name__)

# トップメニュー
@app.route('/')
def index():
    html = render_template('index.html')
    return html

# 詳細メニュー
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()
