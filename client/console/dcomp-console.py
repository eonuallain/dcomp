#!/usr/bin/env python3

from task_cs import TaskCS
from task_enc import TaskEncryption

if __name__ == '__main__':

	choice = ''
	tasks = dict()

	TASK_ENC = '1'
	TASK_CS = '2'

	task_cohen_sutherland = TaskCS()
	task_encryption = TaskEncryption()
	tasks[TASK_ENC] = task_encryption
	tasks[TASK_CS] = task_cohen_sutherland

	while choice not in (TASK_ENC, TASK_CS):
		print("Choose one of the following, enter 1 or 2")
		print("   1 Encryption task")
		print("   2 Cohen-Sutherland task")
		choice = input()        

	print("running task {}".format(choice))
	print("running {}".format(tasks[choice]))
	
	url_enc = "http://localhost:5000/task/encryption/next"
	tasks[choice].run(url_enc)