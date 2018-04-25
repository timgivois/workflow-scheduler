"""
policy = {
    task_id: Resource
}
"""
from threading import Thread
from time import sleep
from .resource import Resource
from .config import RESOURCES

def run_task(task, instructions, parents, resource, done_tasks):
    while not(set(parents)<=set(done_tasks)):
        sleep(1)
    resource.run(instructions)
    done_tasks.append(task)

class Executor:
    def init(self):
        resources = [ Resource(**resource) for resource in RESOURCES ]
        # create policy
        return resources

    def run(self, workflow, resources, policy):
        total_cost = 0
        total_time = 0

        done_tasks = []
        threads = []
        for task in range(0, workflow.size):
            threads.append(Thread(target=run_task, args=(task, workflow.weights[task], workflow.edges['target'][task], resources[policy[task]], done_tasks,)))
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        for resource in resources:
            total_cost += resource.total_cost
            total_time += resource.total_time

        print('Total time {0}'.format(total_time))
        print('Total Cost {0}'.format(total_cost))
