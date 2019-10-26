from flask import Flask, jsonify

import logging
import logging.config
import mysql.connector
import yaml


with open('./config/log.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

app = Flask(__name__)
app.config.from_envvar('APP_CONFIG_FILE')

log = logging.getLogger(__name__)

conn = mysql.connector.connect(
	host=app.config["DB_HOST"], 
	user=app.config["DB_USER"], 
	passwd=app.config["DB_PASSWORD"],
	database=app.config["DB_SCHEMA"]
)

log.info("connect to mysql {}".format(conn))
cursor = conn.cursor(dictionary=True)

def build_task_list():
	sql_select_tasks = "select task_name, task_description from tasks"
	cursor.execute(sql_select_tasks)
	records = cursor.fetchall()
	log.info("records: {}".format(records))
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


@app.route("/task/encryption/next")
def get_next_task_payload():
	log.debug("route /tasks/encryption/next")
	sql = "select id, text_unencrytped from task_encryption where processed=0 order by rand() limit 1"
	cursor.execute(sql)
	records = cursor.fetchall()
	log.debug("records -> {}".format(records))

	text = ""
	pk = 0

	for row in records:
		text = row['text_unencrytped']
		pk = row['id']

	payload = dict()
	payload['id'] = pk
	payload['text'] = text

	return jsonify(payload)

if __name__ == "__main__":
	app.run(
		host=app.config["FLASK_HOST"],
		debug=app.config["FLASK_DEBUG"]
	)
