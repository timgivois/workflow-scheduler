from .scheduler import Scheduler

class MaxResource(Scheduler):
    def schedule(self):
        self.policy = {x: self.resources[-1] for x in range(0, self.workflow.size)}


class MinResource(Scheduler):
    def schedule(self):
        self.policy = {x: self.resources[0] for x in range(0, self.workflow.size)}
