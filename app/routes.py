from flask import Flask

app = Flask(_name_)

@app.get("/")
def home():
    me = {
        "first name": "Rafael",
        "last_name": "GPL",
        "hobbies": "DIY stuff",
        "is_online": True
    }
    return me