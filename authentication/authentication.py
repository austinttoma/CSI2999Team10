import pyrebase

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

# email = 'test@gmail.com'
# password = '123456'

#user = auth.create_user_with_email_and_password(email, password)
#print(user)

user = auth.sign_in_with_email_and_password(email, password)
