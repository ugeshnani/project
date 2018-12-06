from database import *
from datetime import datetime
from validate import *


class Control:

    def add(self,task_name,task_date,task_status):
        print ("inside add")
#        print((Validate().check_task_name(task_name)))
	if (Validate().check_task_name(task_name)):
            return {"pdf1":"Success","pdf2": task_name+" is already added please change  Task Name "}

#        task_date=task_date.strftime('%Y-%m-%d %H:%M:%S')
        valid = SQLDatabase().add(task_name,task_date,task_status)
        print (valid)
	return {"pdf1":"Success","pdf2":"Task Added Sucessfully"}
      
    def modify(self,task_name,task_date,task_status):
        print ("inside control modify")
#        task_date=task_date.strftime('%Y-%m-%d %H:%M:%S')
	if not (Validate().check_task_name(task_name)):
            return {"pdf1":"Failure","pdf2": task_name+" is not yet added please add  Task Name "}
	
        valid = SQLDatabase().modify(task_name,task_date,task_status)
        print (valid)
        return valid
    def due(self,task_date):
        print ("inside control due")
#        run_date=task_date.strftime('%Y-%m-%d %H:%M:%S')
        valid = SQLDatabase().due(task_date)
        print (valid)
        return valid
    def overdue(self):
        print ("inside control overdue")
        run_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        valid = SQLDatabase().overdue(run_date)
        print (valid)
        return valid
    def finished(self):
        print ("inside control finished")
#        run_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        valid = SQLDatabase().finished()
        print (valid)
        return valid
