from constants import *
from src.api import start_task


class Master:
    def __init__(self, default_config):
        self.task = default_config
        self.task_type = self.task['task_type']
        self.in_docker = self.task['in_docker']

    def start(self):
        if self.task_type == TaskType.API.value:
            start_task()
