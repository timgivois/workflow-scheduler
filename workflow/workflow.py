from graph_tool.all import Graph, graph_draw
from random import choice, sample
from math import floor
from itertools import accumulate

class Workflow:
    def __init__(self, simulate_workflow, vertex_number=None, layers_distribution=None, dependency_distribution=None):
        if simulate_workflow:
            self._create_random_workflow(vertex_number, layers_distribution, dependency_distribution)

    def _create_random_workflow(self, vertex_number, layers_distribution, dependency_distribution):
                self.graph = Graph()
                self.layers = [1] + [ floor((vertex_number-2) * layer_dist) for layer_dist in layers_distribution] + [1]
                self.layers_accum = [x for x in accumulate(self.layers)]
                self.graph.add_vertex(self.layers_accum[-1])
                self.length = self.layers_accum[-1]
                self.edges = {'target':{}, 'source': {}}

                # init Workflow
                # first layer connection
                for i in range(self.layers_accum[0], self.layers_accum[1]):
                    self._add_edge(0, i)
                # last layer connection
                for i in range(self.layers_accum[-3], self.layers_accum[-2]):
                    self._add_edge(i, self.layers_accum[-2])

                # create one connection at least for every task
                for i in range(0, len(self.layers_accum)-3):
                    this_init = self.layers_accum[i]
                    next_init = self.layers_accum[i+1]
                    next_last = self.layers_accum[i+2]
                    next_values = [ x for x in range(next_init, next_last+1)]
                    for j in range(this_init, next_init):
                        self.add_random_target_edge(j, next_values)

                # create one receiving connection
                for i in range(1, len(self.layers_accum)-2):
                    this_init = self.layers_accum[i]
                    before_init = self.layers_accum[i-1]
                    next_init = self.layers_accum[i+1]
                    before_values = [ x for x in range(before_init, this_init-1)]
                    for j in range(this_init, next_init):
                        self.add_random_source_edge(j, before_values)

                # create additional possible_connections
                for i in range(0, len(self.layers_accum)-3):
                    possible_sources = range(self.layers_accum[i], self.layers_accum[i+1])
                    next_layer = 0
                    for j in range(i+1, len(self.layers_accum)-2):
                        possible_target = range(self.layers_accum[i+1], self.layers_accum[i+2])
                        possible_connections = self._get_possible_edges(possible_sources, possible_target)
                        self._connect_random_connections(possible_connections, dependency_distribution[i][next_layer])
                        next_layer=next_layer+1

    def _add_edge(self, source, target):
        if source not in self.edges['source']:
            self.edges['source'][source] = [target]
        else:
            self.edges['source'][source].append(target)
        if target not in self.edges['target']:
            self.edges['target'][target] = [source]
        else:
            self.edges['target'][target].append(source)

        self.graph.add_edge(self.graph.vertex(source), self.graph.vertex(target))

    def _get_possible_edges(self, possible_sources, possible_targets):
        possible_connections = []
        for source in possible_sources:
            possible_connections.extend([source, target] for target in possible_targets if target not in self.edges['source'].get(source, []))
        return possible_connections

    def _connect_random_connections(self, possible_connections, probability):
        sample_size = floor(len(possible_connections) * probability)
        connections = sample(possible_connections, sample_size)
        print(connections)
        for connection in connections:
            self._add_edge(connection[0], connection[1])

        return True

    def add_edge_if_possible(self, source, target):
        sucess = False

        if not(self.is_connected(source, target)):
            self._add_edge(source, target)
            sucess = True

        return sucess

    def add_random_source_edge(self, target, possible_connections):
        finished = False
        while not(finished):
            source = choice(list(set(possible_connections) - set(self.edges['target'].get(target, []))))
            finished = self.add_edge_if_possible(source, target)
        return finished

    def add_random_target_edge(self, source, possible_connections):
        finished = False
        while not(finished):
            target = choice(list(set(possible_connections) - set(self.edges['source'].get(source, []))))
            finished = self.add_edge_if_possible(source, target)
        return finished

    def is_connected(self, source, target):
        return target in self.edges['source'].get(source, [])

    def show(self, size=1500):
         return graph_draw(self.graph, vertex_text=self.graph.vertex_index, vertex_font_size=18,
                    output_size=(size, size), output="graph.png")
