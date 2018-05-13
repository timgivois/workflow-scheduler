from simulation.executor import Executor
from simulation.resource import Resource
from simulation.config import RESOURCES

class Scheduler:
    def __init__(self, time, cost, workflow):
        self.time = float(time)
        self.cost = float(cost)
        self.workflow = workflow

        self.resources = [Resource(**resource) for resource in RESOURCES]

    def run(self):
        executor = Executor()
        total_time, total_cost = executor.run(self.workflow, self.resources, self.policy)

        return total_time, total_cost
