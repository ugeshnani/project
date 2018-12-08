from flask import Flask,Response,send_file, render_template,request,jsonify,session,app,redirect
from control import *


from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='template')


@app.route("/")
def start():
        return render_template("login.html")



@app.route('/login',methods=['POST'])
def login():
                print(request.path)
                rcvData=request.get_json()
		print(rcvData)
                username=str(rcvData['username'])
                password=str(rcvData['password'])
                #       if 'username' in session:
                #               return jsonify({'pdf1':'Failure','pdf2':session['username']})
		if (username == 'user' and password == 'user') or (username== 'admin' and password =='admin'):
			session['username'] = username
			return jsonify({'pdf1':'Success'})
                else :
                	return jsonify({'pdf1':'Failure','pdf2':'UserName or Password is Invalid'})




@app.route('/signout',methods=['POST'])
def signout():
        session.pop('username', None)
        return jsonify({'pdf1':'Success'})



@app.route('/check_session', methods=['POST'])
def check_session():
                print("inside check_session")
                username=session['username']
		print(username)
		return jsonify({'pdf1':'Success','pdf2':str(username)})



@app.route('/add', methods = ['POST'])
def add():
        print ("inside add in flask")
        rcvData=request.get_json()
	print(rcvData)
        task_name=str(rcvData['name'])
	print(task_name)
        task_date=(rcvData['date'])
	print(task_date)
        task_status=str(rcvData['status'])
	print(task_status)
	if session['username'] == 'user':
		return jsonify({'pdf1':'Failure','pdf2':'Your are not authorized to Add Task'})
        valid = Control().add(task_name,task_date,task_status)
        print (valid)
        return jsonify(valid)

@app.route('/modify', methods = ['POST'])
def modify():
        print ("inside modify in flsak")
        rcvData=request.get_json()
        task_name=str(rcvData['name'])
        task_date=rcvData['date']
        task_status=str(rcvData['status'])
	if session['username'] == 'user' :
		return jsonify({'pdf1':'Failure','pdf2':'Your are not authorized to Modify Task'})
        valid = Control().modify(task_name,task_date,task_status)
        print (valid)
        return jsonify(valid)

@app.route('/due', methods = ['POST'])
def due():
        print ("inside due")
        rcvData=request.get_json()
        task_date=rcvData['date']
        print(task_date)
        valid = Control().due(task_date)
        print (valid)
        return jsonify(valid)
@app.route('/overdue', methods = ['POST'])
def overdue():
        print ("inside overdue")
        valid = Control().overdue()
        print (valid)
        return jsonify(valid)
@app.route('/finished', methods = ['POST'])
def finished():
        print ("inside finished")
        valid = Control().finished()
        print (valid)
        return jsonify(valid)

if (__name__ == "__main__"):
        app.secret_key = 'mysecret'
        app.run(host="127.0.0.1",port = 6007,debug=True)
