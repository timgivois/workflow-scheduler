from graph_tool.all import Graph, graph_draw

class Workflow:
    def __init__(self, edges, weights):
        self.edges = edges
        self.graph = Graph()
        self.size = len(edges['target'])
        self.graph.add_vertex(self.size)

        # init weights part
        self.graph.vp.weights = self.graph.new_vertex_property('int16_t')
        for index in range(0, self.size):
            self.graph.vp.weights[index] = weights[index]

        for source in self.edges['source'].keys():
            for target in  self.edges['source'][source]:
                self._add_edge(source, target)

        self.depth_per_node = {x:0 for x in range(0, self.size)}
        self.weight_per_node = {x:0 for x in range(0, self.size)}
        self.find_depth()
        self.depth = {x: [] for x in set(self.depth_per_node.values())}

        for node, depth in self.depth_per_node.items():
            self.depth[depth].append(node)

    def _add_edge(self, source, target):
        self.graph.add_edge(self.graph.vertex(source), self.graph.vertex(target))


    def show(self, size=1500):
         return graph_draw(self.graph, vertex_text=self.graph.vertex_index, vertex_font_size=18,
                    output_size=(size, size), output="graph.png")

    def find_depth(self, actual_node=0, actual_depth=0):
        self.depth_per_node[actual_node] = max(self.depth_per_node[actual_node], actual_depth)
        for next_node in self.edges['source'][actual_node]:
            self.find_depth(next_node, actual_depth+1)

    def find_routes(self, father, route_id):
        for child in self.edges['source'][father]:
            self.find_routes(child)

    def find_critical_route(self):
        for index, child in enumerate(self.edges['source'][0]):
            self.find_routes(child)
