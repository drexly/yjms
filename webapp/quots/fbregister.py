import pyrebase
config = {
  "apiKey": "AIzaSyDGnjM4jjWuStsCElq6QE31IuOLZH1ee9Q",
  "authDomain": "yjms-ad1e5.firebaseapp.com",
  "databaseURL": "https://yjms-ad1e5.firebaseio.com",
  "storageBucket": "yjms-ad1e5.appspot.com"
}
firebase = pyrebase.initialize_app(config)

def initialize():
    db = firebase.database()
    db.push({'info',{'name',"juhyeon"}})
