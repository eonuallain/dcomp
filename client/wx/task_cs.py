import datetime
from task_base import TaskBase

# Cohen-Sutherland implementation
class TaskCS(TaskBase):

    def run(self, task):
      print(self)
      print(task)
      print(datetime.datetime.now(), flush=True)  