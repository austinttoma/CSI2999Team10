from flask import Flask, session, render_template, request, redirect
import pyrebase
import googlemaps

app = Flask(__name__)
gmaps = googlemaps.Client(key='AIzaSyA1iSAck_5NWCRTnAoN8yv6g20Xg4jZZiI')
config = {
    'apiKey': "AIzaSyD3Ax_l85vk3U5P5h2hAEIWdASguZAHcXs",
    'authDomain': "csi2999team10-f457b.firebaseapp.com",
    'projectId': "csi2999team10-f457b",
    'storageBucket': "csi2999team10-f457b.appspot.com",
    'messagingSenderId': "639473870266",
    'appId': "1:639473870266:web:a9a97e2ffe8c548f63e983",
    'measurementId': "G-7NCQG5M9FB",
    'databaseURL': "",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
app.secret_key = 'secret'


# Main page used to Login and navigate to Registeration and Reset Password
@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] =email
            return redirect('/main')
        except:
            return 'Failed to login'
    return render_template('home.html')

# Registration Page & Function
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session['user'] =email
            return redirect('/main')
        except:
            return 'Failed to login'
    return render_template('register.html')

# Logout redirectory to Login Page
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

# Reset Password  
@app.route('/reset', methods=['POST', 'GET'])
def reset():
    if request.method == 'POST':
        email = request.form.get('email')
        try:
            auth.send_password_reset_email(email)
            return redirect('/')
        except:
            return 'Failed to reset'
    return render_template('reset.html')

# Main page navigation
@app.route('/main')
def mainpage():
    return render_template('mainpage.html')

# Quizzes Navigation
@app.route('/quizzes', methods=['POST','GET'])
def quizzes():
    return render_template('quizzes.html')

# Userfeed Navigation
@app.route('/userfeed', methods=['POST','GET'])
def userfeed():
    return render_template('userfeed.html')

# Navigation to the Map showing recycling centers
@app.route('/map', methods=['POST','GET'])
def map():
    return render_template('map.html')

# Recycle Tracker
@app.route('/recycletracker', methods=['POST','GET'])
def recycletracker():
    return render_template('recycletracker.html')

# Teaches User about Recycling
@app.route('/modules', methods=['POST','GET'])
def modules():
    return render_template('modules.html')

@app.route('/search', methods=['POST','GET'])
def search():
    search = request.form['search']
    return render_template('search.html')

if __name__ == '__main__':
    app.run(port=1111)