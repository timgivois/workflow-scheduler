from graph_tool.all import Graph, graph_draw

class Workflow:
    def __init__(self, edges, weights):
        self.edges = edges
        self.graph = Graph()
        self.size = len(edges['target'])
        self.graph.add_vertex(self.size)
        self.weights = weights

        # init weights part
        self.graph.vp.weights = self.graph.new_vertex_property('int16_t')
        for index in range(0, self.size):
            self.graph.vp.weights[index] = weights[index]

        for source in self.edges['source'].keys():
            for target in  self.edges['source'][source]:
                self._add_edge(source, target)

        self.depth_per_node = {x:0 for x in range(0, self.size)}
        self.accum_weights = {x:0 for x in range(0, self.size)}
        self.find_depth()
        self.find_accum_weights(self.size-1)
        self.depth = {x: [] for x in set(self.depth_per_node.values())}

        for node, depth in self.depth_per_node.items():
            self.depth[depth].append(node)

    def _add_edge(self, source, target):
        self.graph.add_edge(self.graph.vertex(source), self.graph.vertex(target))


    def show(self, size=1500):
         return graph_draw(self.graph, vertex_text=self.graph.vertex_index, vertex_font_size=18,
                    output_size=(size, size), output="graph.png")

    def find_accum_weights(self, actual_node, accum_weight=0):
        already_accum_weight = self.accum_weights[actual_node]
        self.accum_weights[actual_node] = max(already_accum_weight, accum_weight+self.weights[actual_node])

        for fathers in self.edges['target'][actual_node]:
            self.find_weights(fathers, self.accum_weights[actual_node])

    def find_depth(self, actual_node=0, actual_depth=0):
        self.depth_per_node[actual_node] = max(self.depth_per_node[actual_node], actual_depth)
        for next_node in self.edges['source'][actual_node]:
            self.find_depth(next_node, actual_depth+1)
