About
Cloud leak task Program.

Required Resources
    1. Required python 2.7
    2. Required MYSQL RDBMS.

Third Party Libraries and Dependencies

    1. Install Flask using pip.
    2. Install pymysql using pip.
    3. Install datetime using pip.

How to run Application
    -python test.py


Description about appliction.

1.   create schema as Grid in MYSQL RDBMS, create a table with table name 'task_table' with following feilds
task_name,task_date,task_status. or just run this query in mysql console
("CREATE TABLE table_task (task_name VARCHAR(20), task_date datetime,task_name VARCHAR(20)")

2.    created user(read-only access) and admin(read-write access) as two user for this application.
 use username-user and password-user for read-only access,
 use username-admin and password-admin for read-write access,



