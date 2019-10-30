import json
import time
import urllib.request

from task_base import TaskBase

class TaskEncryption(TaskBase):

	def run(self, enc_url):
		print(self)

		for x in range(0, 5):
			self.get_plain_text(enc_url)
			#don't kill the server
			print("sleeping for 2 seconds ...")
			time.sleep(2)

	def get_plain_text(self, enc_url):
		with urllib.request.urlopen(enc_url) as url:
			data = json.loads(url.read().decode())
			print(data)

