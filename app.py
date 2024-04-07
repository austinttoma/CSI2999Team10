from flask import Flask, session, render_template, request, redirect
import pyrebase
import googlemaps
from authentication import indexFirebase
import Levenshtein

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
    'databaseURL': "https://csi2999team10-f457b-default-rtdb.firebaseio.com/",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
app.secret_key = 'secret'


# Main page used to Login and navigate to Registeration and Reset Password
@app.route('/', methods=['POST','GET'])
def index():
    #  **************IMPORTANT*********************
    indexFirebase() #this is used to initialize the realtime database, if you uncomment this please delete what is in the database otherwise you WILL get duplicates in the database
    #as well if you are trying to change what is held run to homepage and restart the program as again you WILL get duplicates

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

# Recycle Tracker IN PROGRESS 
@app.route('/recycletracker', methods=['POST', 'GET'])
def recycletracker():
    user_email = session.get('user')
    if not user_email:
        # Redirect to login if no user in session
        return redirect('/')
    
    # Normalize the user email to use as a Firebase database key
    user_email_key = user_email.replace('.', ',')

    # Reference to the user's recycle count in the database
    recycle_count_ref = db.child("recycleCounts").child(user_email_key)

    if request.method == 'POST':
        # Fetch the current count, increment it, and update the database
        current_count = recycle_count_ref.get().val()
        if current_count is None:
            # If the count doesn't exist yet, start with 1
            new_count = 1
        else:
            # If the count exists, increment it
            new_count = current_count + 1
        recycle_count_ref.set(new_count)
    else:
        # For a GET request, just fetch the current count without incrementing
        new_count = recycle_count_ref.get().val() or 0

    # Render the template with the current or updated count
    return render_template('recycletracker.html', count=new_count)




# Teaches User about Recycling
@app.route('/modules', methods=['POST','GET'])
def modules():
    return render_template('modules.html')


@app.route('/search', methods=['POST','GET'])
def search():
    if request.method == 'POST':
        search_query = request.form['search']
        search_results = perform_search(search_query) #function call
        return render_template('search.html', search_query=search_query, search_results=search_results)
    else:
        return render_template('search.html')

#actual work and search logic
def perform_search(query):
    #retrieves all the names of items
    items_ref = db.child("items").order_by_child("name").get()
    search_results = []
    max_distance = 3
    
    for items in items_ref.each():
    #test to see if names and the query are similar and if they are add them to the results list
        item_name = items.val().get('name', '') 
        distance_to_query = Levenshtein.distance(query.lower(), item_name.lower())
        if query.lower() in item_name.lower() or distance_to_query <= max_distance:
            search_results.append({'name': item_name, 'id': items.key()})
            
    return search_results

@app.route('/info/<item_id>')
def show_item_info(item_id):
    #getting item based of its item_id
    item_ref = db.child("items").child(item_id).get()
    #routing to info page with all of the items information from database
    if item_ref is not None:
        item_info = item_ref.val()  
        return render_template('item.html', item_id=item_id, item_info=item_info)
    else:
        return "Item not found", 404


  

if __name__ == '__main__':
    app.run(port=1111)