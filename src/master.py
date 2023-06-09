import traceback

from constants import *
from api import start_task


class Master:
    def __init__(self, default_config):
        self.task = default_config
        self.task_type = self.task['task_type']
        self.in_server = self.task['in_server']

    def start(self):
        try:
            if self.task_type == TaskType.API.value:
                start_task(self.task)
        except Exception:
            traceback.print_exc()
