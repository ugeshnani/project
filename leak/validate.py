from control import *
from database import *

class Validate:

    def check_task_name(self,task_name):
	print(SQLDatabase().check_task_name(task_name))
        if len(SQLDatabase().check_task_name(task_name)) == 1:
		print(SQLDatabase().check_task_name(task_name))
            	return True
        else:
            return False
