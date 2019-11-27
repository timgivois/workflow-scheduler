from .scheduler import Scheduler
from simulation.config import RESOURCES
from simulation.resource import Resource
import numpy as np

def find_nearest_zero(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

FASTER_RESOURCE = RESOURCES[-1]

class DepthScheduler(Scheduler):
    def schedule(self):
        weight_per_depth = {}
        nodes_per_depth = {}
        policy = {}

        for depth in self.workflow.depth:
            nodes = self.workflow.depth[depth] # I know, I'm sorry
            weight_per_depth[depth] = sum([self.workflow.weights[x] for x in nodes])
            nodes_per_depth[depth] = len(self.workflow.depth[depth])

        total_weight = sum(weight_per_depth.values())
        total_nodes = sum(nodes_per_depth.values())

        for depth in self.workflow.depth:
            nodes = self.workflow.depth[depth]
            nodes_sorted = sorted([[x, self.workflow.weights[x]] for x in nodes], key=lambda x: x[1], reverse=True)
            target = 10000
            for i in range(0, len(nodes_sorted)):
                sorted_node = nodes_sorted[i]

                if i == 0:
                    target = sorted_node[1] / FASTER_RESOURCE['speed']
                    policy[sorted_node[0]] = self.resources[-1]
                    continue
                resource = find_nearest_zero([sorted_node[1] / resource['speed'] for resource in RESOURCES], target)

                policy[sorted_node[0]] = self.resources[resource]

        self.policy = policy
