from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
 
conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="dcomp")
cursor = conn.cursor(dictionary=True)

def build_task_list():
	sql_select_tasks = "select task_name, task_description from tasks"
	cursor.execute(sql_select_tasks)
	records = cursor.fetchall()
	tasks = dict()

	for row in records:
		tasks[row['task_name']] = row['task_description'] 
		
	return tasks

@app.route("/")
def index():
	return "dcomp"

@app.route('/tasks')
def tasks():
	tasks = build_task_list()
	return jsonify(tasks)

if __name__ == "__main__":
	app.run()
