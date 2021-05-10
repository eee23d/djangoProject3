from flask import Flask,render_template,request,url_for,redirect
app=Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/',methods=['GET','POST'])
def login():
        error=None
        if request.method=="POST":
            if request.form['username']!='admin' or request.form['password']!='admin':
                error='invalid username or password'
            else:
                return redirect(url_for('home'))

        return render_template('login.html',error=error)

if __name__=='__main__':
    app.run(debug=True)
