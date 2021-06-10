import json

from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/login",methods= ["GET","POST"])
def login():
    headers = [("Content-Type","application/json")]
    if request.method == "GET":
        return render_template("login/login.html")
    if request.method == "POST":
        if request.json:
            username =  request.json.get("username")
            password = request.json.get("password")
            if username == "admin" and password == "123456":
                login_sucess_message = {"status": 0,"data":{"token":"abcd1234","user":username}}
                return (json.dumps(login_sucess_message,ensure_ascii=False),200,headers)
            else:
                login_fail_message = {"status":1,"errorCode":"001"}
                return (json.dumps(login_fail_message, ensure_ascii=False), 200, headers)
        else:
            return (json.dumps({"status":1,"errorMess":"NOT FOUND ANY PARAMS"},ensure_ascii=False),400,headers)

