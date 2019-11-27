from threading import Lock
from time import sleep


class Resource:
    def __init__(self, speed, cost):
        self.speed = speed  # instructions per second
        self.cost = cost  # $ per second
        self.is_running = Lock()
        self.total_cost = 0
        self.total_time = 0
        self.lock = Lock()

    def run(self, instructions):
        time_execution = instructions / float(self.speed)
        cost_execution = time_execution * self.cost

        self.lock.acquire()
        self.total_cost += cost_execution
        self.total_time += time_execution
        self.lock.release()

    def emulate(self, instructions):
        time_execution = instructions / float(self.speed)
        cost_execution = time_execution * self.cost


        self.is_running.acquire()
        sleep(time_execution /100)
        self.is_running.release()

        self.lock.acquire()
        self.total_cost += cost_execution
        self.total_time += time_execution
        self.lock.release()
