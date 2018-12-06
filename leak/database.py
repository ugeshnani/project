import MySQLdb
import csv
import sys

class SQLDatabase:

    def __init__(self):
        
        self.db = MySQLdb.connect(host="10.154.194.146",user="vrgdev",passwd="Redhat@12345",db="GRID")

    def add(self,task_name,task_date,task_status):

        print("inserting into task_table")
        cursor = self.db.cursor()
        sql = "INSERT INTO task_table (task_name,task_date,task_status) VALUES (%s,%s,%s)"
        cursor.execute(sql, (task_name,task_date,task_status))
        self.db.commit();
        cursor.close();
        self.db.close();


		
    def modify(self,task_name,task_date,task_status) :

        cursor=self.db.cursor()
        print("update task_table")
        sql="UPDATE task_table SET task_date =%s,task_status =%s  WHERE task_name=%s"
        cursor.execute(sql,(task_date,task_status,task_name))
        self.db.commit();
        cursor.close();
        self.db.close();
	return True



    def due(self,task_date) :
        print("fetching due tasks")
        cursor = self.db.cursor()
        sql="SELECT * FROM task_table where task_date <'%s'"%(task_date)
        cursor.execute(sql)
        duelist=cursor.fetchall()
        self.db.commit();
        cursor.close();
        self.db.close();
        return duelist

    def overdue(self,task_date) :

        print("fetching overdue tasks")
        cursor = self.db.cursor()
        sql="SELECT * FROM task_table where task_date >'%s'"%(task_date)
        cursor.execute(sql)
        overduelist=cursor.fetchall()
        self.db.commit();
        cursor.close();
        self.db.close();
        return overduelist


    def finished(self) :

        print("fetching finished tasks")
        cursor = self.db.cursor()
        sql="SELECT * FROM task_table where status ='finished'"
        cursor.execute(sql)
        finishedlist=cursor.fetchall()
        self.db.commit();
        cursor.close();
        self.db.close();
        return finishedlist

    def check_task_name(self,task_name) :

        print("fetching  task with task_name")
        cursor = self.db.cursor()
        sql="SELECT * FROM task_table where task_name ='%s'"%(task_name)
        cursor.execute(sql)
        tasklist=cursor.fetchall()
        self.db.commit();
        cursor.close();
        self.db.close();
        return tasklist
