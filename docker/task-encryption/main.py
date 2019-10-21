import json
import urllib.request

def get_task_encryption_payload():
	data = ""
	try:
		url = "http://localhost:5000/tasks/encryption/next"
		print("opening {}".format(url))
		with urllib.request.urlopen(url) as url:
			data = json.loads(url.read().decode())
	except urllib.error.HTTPError as e:
		print(e.code)
	except urllib.error.URLError as e:
		print(e.reason)

	return data

print(get_task_encryption_payload())
