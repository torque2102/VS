from flask import Flask, render_template, redirect, url_for, request, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace 'your_secret_key' with a secure key

# Hardcoded credentials for demo purposes
USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials, please try again.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
