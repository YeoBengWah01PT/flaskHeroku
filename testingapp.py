#import flask from Flask
from flask import Flask, render_template,request
import bcrypt
import re
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    data = request.args.get('data')
    pattern = "[a-zA-Z0-9]+@[a-zA-Z-]+\.[a-zA-Z0-9-.]+"
    user_input = data
    result = "Nothing"
   # if (re.search(pattern,data)):
    exp = re.compile(pattern)
    if (exp.match(data)):
        print("validemail")
        print('data', data)
        result = "valid data"
    else:   
        print("invalid dmail")
        print("result is invalid")
        result = "invalid"
    return result

@app.route('/bcrypt')
def bcryptfunc():
   
    Password = b"SecretPassword55"
    hashed = bcrypt.hashpw(password,bcrypt.getsalt())
    print(hashed)
    #salot is a a randomly string to hash the password
    if bcrypt.checkpw(password, hashed):
    	return ("it matches")
    else:
    	return ("Didn’t match")

   

@app.route('/test', methods=['GET'])
def test():

    return render_template('test.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])  

app.run()