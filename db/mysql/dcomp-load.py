import mysql.connector

sql_encryption = "insert into task_encryption (text_unencrytped) values (%s)"
sql_tasks = "insert into tasks (task_name, task_description) values (%s, %s)"

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="dcomp"
)

cursor = db.cursor()

file = open("data.txt", "r")
count = 0

for line in file:
	line = str.strip(line)
	if line:
		cursor.execute(sql_encryption, (line,))		
		db.commit()
		count = count + 1

print("inserted {} lines".format(count))

cursor.execute(sql_tasks, ("Encryption task", "A dummy encryption method using ROT13"))
cursor.execute(sql_tasks, ("Cohen-Sutherland", "Cohen-Sutherland algorithm"))

db.commit()
db.close()
