from flask import Flask, render_template, request, redirect, redirect, session,url_for
from datetime import timedelta
import random
import string
from flask.templating import render_template_string
import psycopg2
import db
import hashlib

app = Flask(__name__)
app.secret_key = "".join(random.choices(string.ascii_letters, k=256))
@app.route("/")
def top():
    return render_template('top.html')

@app.route("/system")
def system():
    return render_template('system.html')

@app.route("/map")
def map():
    return render_template('iwate.html')

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/login", methods=['POST'])
def login():
    id = request.form.get("id")
    pw = request.form.get("pw")

    result = db.login(id)

    b_pw = bytes(pw,"utf-8")
    b_salt = bytes(result[2],"utf-8")

    if result == None:
        print("ログイン失敗")
        return redirect(url_for("login"))
    elif result[1] == hashlib.pbkdf2_hmac("sha256",b_pw,b_salt,2560).hex():
        print("ログイン成功")
        session.permanent = True   
        app.permanent_session_lifetime = timedelta(minutes=30) 
        result = db.shopRegistRequist()
        print(result[0][0])
        print(result[0][1])
        return render_template("registerReq.html",shop=result)
    else:
        print("ログイン失敗")
        return redirect(url_for("login"))

@app.route("/shopRegist")
def shopRegist():
    id = request.args.get("id")
    result = db.embedRegist(id)
    print(result[0])
    shopname = result[1]
    product = result[2]
    return render_template("shopEmbed.html",shopname=shopname,product=product)



if __name__ == "__main__":
    app.run(debug=True)