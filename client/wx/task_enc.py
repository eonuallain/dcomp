import datetime
from task_base import TaskBase

class TaskEncryption(TaskBase):

    def run(self, task):
      print(self)
      print(task)
      print(datetime.datetime.now(), flush=True)

