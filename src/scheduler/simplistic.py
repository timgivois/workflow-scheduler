# Simplistic scheduler that maps the best resource to critical path

class Simplistic:

    def order_routes(routes):
        return sorted(routes, key=lambda x: x['weight'], reverse=True)

    def order_resources(resources):
        return sorted(resources, key=lambda x: x['speed'], reverse=True)

    def schedule(self, workflow, resources):

        routes - workflow.routes.copy()
        routes = self.order_routes(routes)

        policy = {x: -1 for x in range(0, workflow.size)}

        resources = resources.copy()
        resources = self.order_resources(resources)

        resources_size = len(resources)
