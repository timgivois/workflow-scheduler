import numpy as np
from .scheduler import Scheduler


class Random(Scheduler):
    def schedule(self):
        while True:
            self.policy = {x: np.random.choice(self.resources) for x in range(self.workflow.size)}
            time, cost = self.run()
            if time <= self.time and cost <= self.cost:
                break
