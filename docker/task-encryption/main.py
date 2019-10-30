import json
import sys
import urllib.request

def get_task_encryption_payload():
	data = ""
	try:
		url = sys.argv[1]
		print("opening {}".format(url))
		with urllib.request.urlopen(url) as url:
			data = json.loads(url.read().decode())
	except urllib.error.HTTPError as e:
		print(e.code)
	except urllib.error.URLError as e:
		print(e.reason)

	return data

print(get_task_encryption_payload())
