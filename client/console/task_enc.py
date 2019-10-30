import json
import time
import urllib.request

from task_base import TaskBase

class TaskEncryption(TaskBase):

	def run(self):
		print(self)

		for x in range(0, 2000):
			self.get_plain_text()
			#don't kill the server
			print("sleeping for 2 seconds ...")
			time.sleep(2)

	def get_plain_text(self):
		url_enc = "http://localhost:5000/task/encryption/next"
		with urllib.request.urlopen(url_enc) as url:
			data = json.loads(url.read().decode())
			print(data)

