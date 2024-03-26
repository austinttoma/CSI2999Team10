import pyrebase

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
auth = firebase.auth()
db = firebase.database()
def indexFirebase():
    # Define the item data
    item_data_list = [
        {
            'name': 'Water bottle',
            'info': 'Made of PET plastic, widely recyclable in most facilities. However many of these bottles are downsized into one use goods that go straight to landfills.',
            'bool': 1,
            
        },
        {
            'name': 'Cardboard Box',
            'info': 'Made of cardboard, usually recyclable but check with local facilities.',
            'bool': 0.5,
            
        },
        {
            'name': 'Styrofoam Cup',
            'info': 'Made of polystyrene, not recyclable in most facilities.',
            'bool': 0,
            
        }
        
    ]
    
    # Push each item data to Firebase
    for item_data in item_data_list:
        db.child("items").push(item_data)

