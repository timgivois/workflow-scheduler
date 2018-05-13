"""
policy = {
    task_id: Resource
}
"""
from threading import Thread
from time import sleep


def run_task(task, instructions, parents, resource, done_tasks):
    while not (set(parents) <= set(done_tasks)):
        sleep(.1)
    resource.run(instructions)
    done_tasks.append(task)


class Executor:
    def run(self, workflow, resources, policy):
        total_cost = 0
        total_time = 0
        for resource in resources:
            resource.total_cost = 0
            resource.total_time = 0

        done_tasks = []
        threads = []
        for task in range(0, workflow.size):
            threads.append(Thread(target=run_task, args=(
            task, workflow.weights[task], workflow.edges['target'][task], policy[task], done_tasks,)))
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        for resource in resources:
            total_cost += resource.total_cost
            total_time += resource.total_time

        return total_time, total_cost
