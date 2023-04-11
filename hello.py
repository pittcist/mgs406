from flask import Flask, url_for, redirect, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template('login.htm')

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello {0}!'.format(name)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number {0} '.format(postID)

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number {0} '.format(revNo)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello {0} as Guest'.format(guest)

@app.route('/user/<name>')
def hello_user(name):
    if name =='admin':
        return redirect(url_for('hello_admin')) 
    else:
        return redirect(url_for('hello_guest',guest = name))

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

@app.route('/greeting/<user>')
def greeting(user):
   return render_template('greeting.htm', name = user)

@app.route('/result/<int:score>')
def result(score):
   return render_template('result.htm', marks = score)

if __name__ == '__main__':
    app.run(debug = True)
