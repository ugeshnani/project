from flask import Flask,Response,send_file, render_template,request,jsonify,session,app,redirect
from control import *


from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='template')


@app.route("/")
def start():
        return render_template("task.html")

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
        valid = Control().modify(task_name,task_date,task_status)
        print (valid)
        return jsonify(valid)

@app.route('/due', methods = ['POST'])
def due():
        print ("inside due")
        rcvData=request.get_json()
        task_date=rcvData['date']
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
        return jsoify(valid)

if (__name__ == "__main__"):
        app.secret_key = 'mysecret'
        app.run(host="10.154.194.146",port = 6007,debug=True)
