import mysql.connector

sql = "insert into task_encryption (text_unencrytped) values (%s)"

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
		cursor.execute(sql, (line,))		
		db.commit()
		count = count + 1

db.close()
print("inserted {} lines".format(count))
