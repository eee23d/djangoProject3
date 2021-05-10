from flask import Flask, render_template
#allow to call the page instead of writing functions
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/article')
def article():
    return render_template('article.html')


if __name__ == '__main__':
    app.run(port=3000)
