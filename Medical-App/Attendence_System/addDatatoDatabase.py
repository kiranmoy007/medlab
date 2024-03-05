import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("Attendence_System\serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://medical-appointment-scheduler-default-rtdb.asia-southeast1.firebasedatabase.app/"
})


ref = db.reference('Doctors')   

data = {
    "1231":
    {
        'NAME': "Dr Abhishek Ghosh",
        'DEPT': "CARDIOLOGY",
        'YEARS': "14"
    },

    "1232":
    {
        'NAME': "Dr Ankit Bhattacharya",
        'DEPT': "ONCOLOGIST",
        'YEARS': "15"
    },
        "1233":
    {
        'NAME': "Dr Sneha",
        'DEPT': "Pathologist",
        'YEARS': "15"
    },
        "1234":
    {
        'NAME': "Dr Sneha Roy",
        'DEPT': "Cardiologist",
        'YEARS': "15"
    },
}


for key,value in data.items():
    ref.child(key).set(value)