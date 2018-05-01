from itertools import accumulate
from math import floor
from random import choice, sample, randint
from .config import MAX_INSTRUCTIONS, MIN_INSTRUCTIONS


class Initial_Simulation:
    def __init__(self, vertex_number, layers_distribution, dependency_distribution):
        self.size = vertex_number
        layers = [1] + [round((vertex_number - 2) * layer_dist) for layer_dist in layers_distribution] + [1]

        # Adjust layers
        self.layers = self.layers_adjusted(layers, vertex_number)
        self.layers_accum = [x for x in accumulate(layers)]
        self.edges = {'target': {0: []}, 'source': {self.size - 1: []}}
        self.dependency_distribution = dependency_distribution

        self.add_start_and_stop()
        self.create_connections()
        self.simulate_weights()

    def layers_adjusted(self, layers, vertex_number):
        sum_layers = sum(layers)
        max_layers = max(layers)
        difference = vertex_number - sum_layers
        layers[layers.index(max_layers)] = max_layers + difference

        return layers

    def _add_edge(self, source, target):
        if source not in self.edges['source']:
            self.edges['source'][source] = [target]
        else:
            self.edges['source'][source].append(target)
        if target not in self.edges['target']:
            self.edges['target'][target] = [source]
        else:
            self.edges['target'][target].append(source)

    def add_start_and_stop(self):
        # first layer connection
        for i in range(self.layers_accum[0], self.layers_accum[1]):
            self._add_edge(0, i)
        # last layer connection
        for i in range(self.layers_accum[-3], self.layers_accum[-2]):
            self._add_edge(i, self.layers_accum[-2])

    def add_random_target_edge(self, source, possible_connections):
        finished = False
        while not (finished):
            target = choice(list(set(possible_connections) - set(self.edges['source'].get(source, []))))
            finished = self.add_edge_if_possible(source, target)
        return finished

    def add_random_source_edge(self, target, possible_connections):
        finished = False
        while not (finished):
            source = choice(list(set(possible_connections) - set(self.edges['target'].get(target, []))))
            finished = self.add_edge_if_possible(source, target)
        return finished

    def add_edge_if_possible(self, source, target):
        sucess = False

        if not (self.is_connected(source, target)):
            self._add_edge(source, target)
            sucess = True

        return sucess

    def create_connections(self):
        # create one connection at least for every task
        for i in range(0, len(self.layers_accum) - 3):
            this_init = self.layers_accum[i]
            next_init = self.layers_accum[i + 1]
            next_finish = self.layers_accum[i + 2]
            next_values = [x for x in range(next_init, next_finish)]
            for j in range(this_init, next_init):
                self.add_random_target_edge(j, next_values)

        for i in range(0, len(self.layers_accum) - 3):
            this_init = self.layers_accum[i]
            z = 0
            for j in range(i, len(self.layers_accum) - 2):
                next_init = self.layers_accum[i + 1]
                next_finish = self.layers_accum[i + 2]
                possible_sources = [x for x in range(this_init, next_init)]
                possible_targets = [x for x in range(next_init, next_finish)]
                possible_connections = [[x, y] for x in possible_sources for y in possible_targets if
                                        x < y and y not in self.edges['source'][x]]
                new_connections = sample(possible_connections,
                                         floor(len(possible_connections) * self.dependency_distribution[i][z]))

                for source, target in new_connections:
                    self.add_edge_if_possible(source, target)

        # create one connection  backward at least for every task
        for i in range(1, len(self.layers_accum) - 2):
            this_init = self.layers_accum[i]
            next_init = self.layers_accum[i + 1]

            for j in range(this_init, next_init):
                if j not in self.edges['target']:
                    before_values = [x for x in range(1, j)]
                    self.add_random_source_edge(j, before_values)

    def is_connected(self, source, target):
        return target in self.edges['source'].get(source, [])

    def simulate_weights(self):
        self.weights = [0]
        for i in range(1, self.size - 1):
            self.weights.append(randint(MIN_INSTRUCTIONS, MAX_INSTRUCTIONS))
        self.weights.append(0)
