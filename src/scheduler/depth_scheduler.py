from .scheduler import Scheduler


class DepthScheduler(Scheduler):
    def schedule(self):
        weight_per_depth = {}
        policy = {}

        for depth in self.workflow.depth:
            nodes = self.workflow.depth[depth] # I know, I'm sorry
            weight_per_depth[depth] = sum([self.workflow.weights[x] for x in nodes])

        total = sum(weight_per_depth.values())
        time_parts = self.time / total
        cost_parts = self.cost / total
        time_per_depth = {x: weight_per_depth[x]*time_parts for x in weight_per_depth}
        cost_per_depth = {x: weight_per_depth[x]*cost_parts for x in weight_per_depth}

        for depth in self.workflow.depth:
            nodes = self.workflow.depth[depth]
