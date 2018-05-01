import numpy as np


class Random:
    def schedule(self, workflow, resources):
        policy = {x: np.random.choice(resources) for x in range(workflow.size)}

        return policy
