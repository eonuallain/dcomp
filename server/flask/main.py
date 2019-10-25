from flask import Flask, jsonify

import logging
import logging.config
import mysql.connector
import yaml


with open('log.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

app = Flask(__name__)
log = logging.getLogger(__name__)

conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="dcomp")
log.debug("connect to mysql {}".format(conn))
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


@app.route('/tasks/encryption/next')
def get_next_task_payload():
	log.debug("route /tasks/encryption/next")

if __name__ == "__main__":
	app.run()
