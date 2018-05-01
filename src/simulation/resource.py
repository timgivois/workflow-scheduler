from threading import Lock


class Resource:
    def __init__(self, speed, cost):
        self.speed = speed  # instructions per second
        self.cost = cost  # $ per second
        self.is_running = False
        self.total_cost = 0
        self.total_time = 0
        self.lock = Lock()

    def run(self, instructions):
        time_execution = instructions / float(self.speed)
        cost_execution = time_execution * self.cost

        # not necessary yet but could be
        # self.is_running = True
        # sleep(time_execution)
        # self.is_running = False
        self.lock.acquire()
        self.total_cost += cost_execution
        self.total_time += time_execution
        self.lock.release()
