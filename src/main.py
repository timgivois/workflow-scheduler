from simulation.workflow import Initial_Simulation
from simulation.executer import Executor
from workflow.workflow import Workflow
from scheduler.simplistic import Simplistic

sim = Initial_Simulation(50, [0.2, 0.3, 0.2, 0.2, 0.2], [[.05, .07, .03, .03], [.05, .04, .04], [.04, 0.05], [0.01]])
workflow = Workflow(sim.edges, sim.weights)
executer = Executor()
resources = executer.init()

policy = {x: resources[-1] for x in range(0, workflow.size)}
print('Max scheduling')
executer.run(workflow, resources, policy)

resources = executer.init()
policy = {x: resources[0] for x in range(0, workflow.size)}
print('Min scheduling')
executer.run(workflow, resources, policy)


resources = executer.init()
simplistic = Simplistic()
policy = simplistic.schedule(workflow, resources)
print('\n\nSimple scheduling')
executer.run(workflow, resources, policy)
