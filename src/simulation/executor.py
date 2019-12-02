"""
policy = {
    task_id: Resource
}
"""
from multiprocessing import Process, Lock, Manager
from threading import Thread
from time import sleep, time
from multiprocessing.managers import BaseManager

def is_task_subset_of(parents, done_tasks):
    for parent in parents:
        try:
            done_tasks.index(parent)
        except ValueError:
            return False
    return True


def run_task(task, instructions, edges, resource, done_tasks, locks):
    locks[task].acquire()
    resource = resource[0]
    # print('acquired {0}'.format(task))
    resource.run(instructions)
    done_tasks.append(task)

    for child in edges['source'][task]:
        if is_task_subset_of(edges['target'][child], done_tasks):
            # print('releasing {0}'.format(child))
            locks[child].release()

def emulate_task(task, instructions, parents, resource, done_tasks):
    while not (set(parents) <= set(done_tasks)):
        sleep(.01)
    resource.emulate(instructions)
    done_tasks.append(task)


def calculate_time_routes(workflow, policy):
    routes = workflow.routes.copy()
    for route in workflow.routes:
        route['time'] = sum([workflow.weights[node] / policy[node].speed for node in route['path']])

    return max(routes, key=lambda x: x['time'])['time']

def calculate_cost_routes(workflow, policy):
    routes = workflow.routes.copy()
    for route in workflow.routes:
        route['cost'] = sum([(workflow.weights[node] / policy[node].speed)*policy[node].cost for node in route['path']])

    return sum(route['cost'] for route in routes)

class Executor:
    def run(self, workflow, resources, policy):
        start = time()
        total_cost = 0
        total_time = 0
        for resource in resources:
            resource.total_cost = 0
            resource.total_time = 0

        threads = []
        locks = [ Lock() for i in range(0, workflow.size) ] # locks
        manager = Manager()

        resource_manager = Manager()
        done_tasks = manager.list()

        for i in range(1, len(locks)): #init them acquired
            locks[i].acquire()

        for task in range(0, workflow.size):
            threads.append(Process(target=run_task, args=(
            task, workflow.weights[task], workflow.edges, policy[task], done_tasks, locks,)))
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        for resource in resources:
            total_cost += resource.total_cost
            total_time += resource.total_time

        return (time() - start)*100, total_cost

    def emulate(self, workflow, resources, policy):
        start = time()
        total_cost = 0
        total_time = 0
        for resource in resources:
            resource.total_cost = 0
            resource.total_time = 0

        done_tasks = []
        threads = []

        for task in range(0, workflow.size):
            threads.append(Thread(target=emulate_task, args=(
            task, workflow.weights[task], workflow.edges['target'][task], policy[task], done_tasks,)))
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        for resource in resources:
            total_cost += resource.total_cost
            total_time += resource.total_time

        return calculate_time_routes(workflow, policy), calculate_cost_routes(workflow,policy)
