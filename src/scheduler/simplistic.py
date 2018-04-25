# Simplistic scheduler that maps the best resource to critical path

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

class Simplistic:

    def order_routes(self, routes):
        return sorted(routes, key=lambda x: x['weight'], reverse=True)

    def order_resources(self, resources):
        return sorted(resources, key=lambda x: x.speed, reverse=True)

    def schedule(self, workflow, resources):

        routes = workflow.routes.copy()
        routes = self.order_routes(routes)

        policy = {x: None if x>0 else resources[0] for x in range(0, workflow.size)}

        resources = resources.copy()
        resources = self.order_resources(resources)
        resources_size = len(resources)

        routes_len = len(routes)

        divide = round(routes_len / resources_size)

        i = 0
        for chunk in chunks(routes, divide):
            for route in chunk:
                for task in route['path']:
                    if policy[task] is None:
                        policy[task] = resources[i]
            if i < len(resources) -1:
                i+=1

        return policy
