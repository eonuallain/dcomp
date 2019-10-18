from flask import Flask, jsonify
app = Flask(__name__)


def build_task_list():
	# will be read from DB
	tasks = {
		"Encryption task" : "A dummy encryption method using ROT13",
		"Cohen-Sutherland" : "Cohen-Sutherland algorithm"
	}
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
