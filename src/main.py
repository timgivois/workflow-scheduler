from simulation.workflow import Initial_Simulation
from simulation.executor import Executor
from workflow.workflow import Workflow
from scheduler.simplistic import Simplistic
from scheduler.random import Random

sim = Initial_Simulation(50, [0.2, 0.3, 0.2, 0.2, 0.2], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]])
workflow = Workflow(sim.edges, sim.weights)
executor = Executor()
resources = executor.init()

policy = {x: resources[-1] for x in range(0, workflow.size)}
print('Max scheduling')
executor.run(workflow, resources, policy)

resources = executor.init()
policy = {x: resources[0] for x in range(0, workflow.size)}
print('Min scheduling')
executor.run(workflow, resources, policy)


resources = executor.init()
simplistic = Simplistic()
policy = simplistic.schedule(workflow, resources)
print('\n\nSimple scheduling')
executor.run(workflow, resources, policy)

resources = executor.init()
simplistic = Random()
policy = simplistic.schedule(workflow, resources)
print('\nRandom scheduling')
executor.run(workflow, resources, policy)
