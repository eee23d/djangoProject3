from flask import Flask,render_template,request,url_for,redirect


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def login():
        error=None
        if request.method=="POST":
            if request.form['username']!='admin' or request.form['password']!='admin':
                error='invalid username or password'
            else:
                return redirect(url_for('index'))

        return render_template('login.html',error=error)




@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/articles')
def articles():
    return render_template('articles.html')

if __name__ == '__main__':
    app.run(debug=True,port=3000)