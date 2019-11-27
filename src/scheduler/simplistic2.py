from .scheduler import Scheduler
import numpy as np
from simulation.config import RESOURCES

def find_nearest_zero(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

FASTER_RESOURCE = RESOURCES[-1]

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


class Simplistic2(Scheduler):

    @staticmethod
    def order_routes(routes):
        return sorted(routes, key=lambda x: x['weight'], reverse=True)

    @staticmethod
    def order_resources(resources):
        return sorted(resources, key=lambda x: x.speed, reverse=True)

    def schedule(self):
        routes = self.workflow.routes.copy()

        routes = self.order_routes(routes)

        policy = {0: self.resources[0]}

        resources = self.resources.copy()
        resources = self.order_resources(resources)
        resources_size = len(resources)

        routes_len = len(routes)

        divide = round(routes_len / resources_size)

        target = 0

        for i in range(0, len(routes)):
            route = routes[i]

            if target == 0:
                target = route['weight'] / FASTER_RESOURCE['speed']
                for node in route['path']:
                    policy[node] = self.resources[-1]
                continue
            resource = find_nearest_zero([route['weight'] / resource['speed'] for resource in RESOURCES], target)

            for node in route['path']:
                if node not in policy.keys():
                    policy[node] = self.resources[resource]

        self.policy = policy
